from django.shortcuts import render, get_object_or_404
from stores.models import Store
from reviews.models import Review
import json
import pandas as pd
import numpy as np
import os
import shutil
import pickle
from lightfm.data import Dataset
from scipy.io import mmwrite
from lightfm.cross_validation import random_train_test_split
from hyperopt import fmin, hp, tpe, Trials
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from .serializers import StoreInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

global model,train,item_features,train_weights
global all_store_frame
global reviews_source, item_feature_source
global dataset
# Create your views here.
# @api_view(['GET'])
# def get_stores(request, store_pk):
#     # stores = Store.objects.all();
#     store = get_object_or_404(Store, pk=store_pk)
#     print(type(store))
#     print(store)
#     print(store.store_id)
#     serializer = StoreInfoSerializer(store)

#     return Response(serializer.data)
#     # return Response({'message': '여기요'})


@api_view(['GET'])
def recommend_food(request):
    # 전체 데이터를 불러온다. 
    stores = Store.objects.all()
    reviews = Review.objects.all()

    # 음식점 데이터 
    all_store_frame = pd.DataFrame(list(stores.values('id', 'store_id','store_name', 'category',
    'address','latitude','longitude','average_rating')))

    # 리뷰 데이터 
    reviews_frame = pd.DataFrame(list(reviews.values('id', 'storeid','userid', 'score','reg_time')))

    # 평점 희소행렬 만들기 . . .
    reviews_source = [(reviews_frame['userid'][i], reviews_frame['storeid'][i]) for i in range(reviews_frame.shape[0])]
    
    # 음식점 데이터 
    item_meta =all_store_frame
    item_feature_source = [(item_meta['store_id'][i], [ item_meta['category'][i],item_meta['address'][i],item_meta['latitude'][i],item_meta['longitude'][i], item_meta['average_rating'][i]] ) for i in range(item_meta.shape[0]) ]
    
    dataset = Dataset()
    dataset.fit(users=reviews_frame['userid'].unique(),
           items=reviews_frame['storeid'].unique(),
           item_features=item_meta[item_meta.columns[1:]].values.flatten())

    interactions, weights = dataset.build_interactions(reviews_source)
    item_features = dataset.build_item_features(item_feature_source)

    # Split Train, Test data
    train, test = random_train_test_split(interactions, test_percentage=0.1)
    train, test = train.tocsr().tocoo(), test.tocsr().tocoo()
    train_weights = train.multiply(weights).tocoo()

    # Define Search Space
    trials = Trials()
    space = [hp.choice('no_components', range(10, 50, 10)), hp.uniform('learning_rate', 0.01, 0.05)]

    # Define Objective Function
    def objective(params):

        no_components, learning_rate = params
        global model
        model = LightFM(no_components=no_components,
                        learning_schedule='adagrad',
                        loss='warp',
                        learning_rate=learning_rate,
                        random_state=0)

        model.fit(interactions=train,
                item_features=item_features,
                sample_weight=train_weights,
                epochs=3,
                verbose=False)

        test_precision = precision_at_k(model, test, k=5, item_features=item_features).mean()
        print("no_comp: {}, lrn_rate: {:.5f}, precision: {:.5f}".format(
        no_components, learning_rate, test_precision))
        # test_auc = auc_score(model, test, item_features=item_features).mean()
        output = -test_precision

        if np.abs(output+1) < 0.01 or output < -1.0:
            output = 0.0

        return output
    # max_evals가 몇번 반복실행 할껀지. 
    best_params = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=1, trials=trials)

    # Find Similar Items
    def make_best_items_report(item_embeddings, src_store_id, num_search_items=10):
        src_idx = all_store_frame[all_store_frame['store_id']==src_store_id].index[0]

        # Cosine similarity
        scores = item_embeddings.dot(item_embeddings[src_idx])  # (10000, )
        item_norms = np.linalg.norm(item_embeddings, axis=1)    # (10000, )
        item_norms[item_norms == 0] = 1e-10
        scores /= item_norms

        # best: score가 제일 높은 item의 id를 num_search_items 개 만큼 가져온다.
        best = np.argpartition(scores, -num_search_items)[-num_search_items:]
        similar_item_id_and_scores = sorted(zip(best, scores[best] / item_norms[src_idx]),
                                            key=lambda x: -x[1])
        print(similar_item_id_and_scores)
        # Report를 작성할 pandas dataframe
        best_items = pd.DataFrame(columns=['store_id','category','score'])

        for tar_idx, score in similar_item_id_and_scores:
            # all_store_frame.iloc[4:5,].values
            tar_store_id = all_store_frame.iloc[tar_idx,1]
            category = all_store_frame[all_store_frame['store_id']==tar_store_id].values[0][3]
            row = pd.Series([tar_store_id, category, score], index=best_items.columns)
            best_items = best_items.append(row, ignore_index=True)

        return best_items


    item_biases, item_embeddings = model.get_item_representations(features=item_features)
    # report01 = make_best_items_report(item_embeddings, 1258, 10) # 순대국밥 
    # report01 = make_best_items_report(item_embeddings, 54044, 10) # 스파게티
    report01 = make_best_items_report(item_embeddings, 1127, 10) # 피자

    # print("1258번 가게(순대국밥)과 유사한 음식점! ")
    # print("54044번 가게(스파게티)와 유사한 음식점! ")
    print("1127 가게(피자)와 유사한 음식점! ")
    print(report01)

    serializer = StoreInfoSerializer(report01)
    # serializer = StoreInfoSerializer(reviews_frame.iloc[:1,])
    # return Response(serializer.data)
    return Response({'message': '여기요'})


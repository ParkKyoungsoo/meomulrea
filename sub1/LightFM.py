import json
import pandas as pd
import numpy as np
from lightfm.data import Dataset
from scipy.io import mmwrite
from lightfm.cross_validation import random_train_test_split
from hyperopt import fmin, hp, tpe, Trials
from lightfm import LightFM
from lightfm.evaluation import precision_at_k

# 평점 데이터 
ratings = pd.read_csv('../data/ratings.csv')
print("리뷰 데이터 형태 : ",ratings.shape)
print("리뷰 데이터 5개 : ",ratings.head())

ratings_source = [(ratings['user_id'][i], ratings['book_id'][i]) for i in range(10000)]

# 책 데이터
item_meta = pd.read_csv('../data/books.csv')
item_meta = item_meta[['book_id', 'authors', 'average_rating', 'original_title']]

item_feature_source = [(item_meta['book_id'][i],
                       [item_meta['authors'][i],
                       item_meta['average_rating'][i]]) for i in range(item_meta.shape[0])]

dataset = Dataset()
dataset.fit(users=ratings['user_id'].unique(),
           items=ratings['book_id'].unique(),
           item_features=item_meta[item_meta.columns[1:]].values.flatten())

interactions, weights = dataset.build_interactions(ratings_source)
item_features = dataset.build_item_features(item_feature_source)

# Split Train, Test data
train, test = random_train_test_split(interactions, test_percentage=0.1)
train, test = train.tocsr().tocoo(), test.tocsr().tocoo()
train_weights = train.multiply(weights).tocoo()

# Define Search Space
trials = Trials()
space = [hp.choice('no_components', range(10, 50, 10)),
         hp.uniform('learning_rate', 0.01, 0.05)]


# Define Objective Function
global model
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

best_params = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=10, trials=trials)

# Find Similar Items

def make_best_items_report(item_embeddings, book_id, num_search_items=10):
    item_id = book_id - 1

    # Cosine similarity
    scores = item_embeddings.dot(item_embeddings[item_id])  # (10000, )
    item_norms = np.linalg.norm(item_embeddings, axis=1)    # (10000, )
    item_norms[item_norms == 0] = 1e-10
    scores /= item_norms

    # best: score가 제일 높은 item의 id를 num_search_items 개 만큼 가져온다.
    best = np.argpartition(scores, -num_search_items)[-num_search_items:]
    similar_item_id_and_scores = sorted(zip(best, scores[best] / item_norms[item_id]),
                                        key=lambda x: -x[1])

    # Report를 작성할 pandas dataframe
    best_items = pd.DataFrame(columns=['book_id', 'title', 'author', 'score'])

    for similar_item_id, score in similar_item_id_and_scores:
        book_id = similar_item_id + 1
        title = item_meta[item_meta['book_id'] == book_id].values[0][3]
        author = item_meta[item_meta['book_id'] == book_id].values[0][1]

        row = pd.Series([book_id, title, author, score], index=best_items.columns)
        best_items = best_items.append(row, ignore_index=True)

    return best_items

item_biases, item_embeddings = model.get_item_representations(features=item_features)

report01 = make_best_items_report(item_embeddings, 2, 10)
report02 = make_best_items_report(item_embeddings, 9, 10)
print("해리포터와 마법사의 돌(book_id:2) 과 유사한 도서 ! ")
print(report01)
print("============")
print("천사와 악마 (book_id:9) 과 유사한 도서 ! ")
print(report02)

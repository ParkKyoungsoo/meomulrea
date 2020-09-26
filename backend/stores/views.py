import json
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Store
from .serializers import StoreSerializer, StoreDetailSerializer

def save_store(request):
    # json_data = open('C:\\Users\\multicampus\\Desktop\\dining_data.json').read()
    json_data = open('stores/dining_data.json').read()
    json_d = json.loads(json_data)
    # print(json_d['data'][0]['store_id'])
    for i in range(10):
        store = Store()
        # item = json_d['data'][0][y]
        # store.storeid = item.get('store_id')
        # store.category = item.get('category')
        # store.average_rating = item.get('average_rating')
        store.storeid = json_d['data'][i]['store_id']
        store.category = json_d['data'][i]['category']
        store.average_rating = json_d['data'][0]['average_rating']
        store.save()
    return
# def save_stores(request):
#     URL = 'data.json'
#     for i in range(100):
#         response = requests.get(URL)
#         json = response.json()
#         print(json)
#         for item in json:
#             store = Store()
#             storeid = item.get('id')
#             store_name = item.get('name')
#             category = item.get('category_list')[0].category[0]
#             address = item.get('address')
#             latitude = item.get('latitude')
#             longtitude = item.get('longtitude')
#             start_time = item.get('bhour_list').start_time
#             end_time = item.get('bhour_list').end_time
#             mon = item.get('bhour_list')[0].mon
#             tue = item.get('bhour_list')[0].tue
#             wed = item.get('bhour_list')[0].wed
#             thu = item.get('bhour_list')[0].thu
#             fri = item.get('bhour_list')[0].fri
#             sat = item.get('bhour_list')[0].sat
#             sun = item.get('bhour_list')[0].sun
#     return
@api_view(['GET'])
# @permission_classes(IsAuthenticated)
def store_list(request):
    # 요청온 데이터의 카테고리 정보를 category로 프론트에서 담았다고 가정했을 때
    # Store 모델에서 카테고리가 요청온 category 정보가 같은 가게 리스트를 stores 변수에 담는다.
    if request.user.is_authenticated:
        # 유저 집주소 조회?
        user_address = request.user.address
        print(user_address)
        # stores = Stores.objects.filter(category=request.data['category'] and address__contains=user_address[:10]).order_by('-average_rating')
        # stores = Store.objects.filter(category=request.data['category']).filter(address__contains=user_address[:2]).order_by('-average_rating')
        stores = Store.objects.filter(category=request.data['category']).order_by('-average_rating')
        print(stores)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': '로그인하세요'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def store_detail(request, storeid):
    # print(request.data['storeid'])
    # storeid = request.data['storeid']
    # store = Store.objects.get(storeid=storeid)
    store = get_object_or_404(Store, storeid=storeid)
    serializer = StoreDetailSerializer(store)
    return Response(serializer.data)


# @api_view(['GET'])
# def review_list(request):
#     reviews = Review.objects.all()
#     serializer = ReviewListSerializer(reviews, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def review_detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     serializer = ReviewSerializer(review)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated]) # 인증된 사용자의 요청인지 검사하는 데코레이터
# def create_review(request, store_pk):
#     serializer = ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user, store_id=store_id)
#         return Response(serializer.data)

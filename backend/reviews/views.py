from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Review
import json
from collections import defaultdict
import re

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

def deEmojify(text):
    regrex_pattern = re.compile(pattern = u'[\U0001f300-\U0001f650]|[\u2000-\u3000]|[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]', flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def deEmojify3(text):
    regrex_pattern = re.compile(pattern = u'[\ud800-\udbff][\udc00-\udfff]', flags = re.UNICODE)
    
    return regrex_pattern.sub(r'',text)

def input_data(request):
    json_data = open('reviews/reviews.json').read()
    json_d = json.loads(json_data)
    for i in range(len(json_d['data'])):
        review = Review()
        review.storeid = json_d['data'][i]['store_id']
        review.userid = json_d['data'][i]['user_id']
        review.score = json_d['data'][i]['score']
        review.reg_time = json_d['data'][i]['reg_time']
        try:
            review.content = deEmojify(json_d['data'][i]['content'])
            review.save()
        except:
            review.content = "맛있어요";
            review.save()
    return

# @api_view(['POST'])
# def review_list(request):
#     reviews = Review.objects.all()
#     serializer = ReviewListSerializer(reviews, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def review_detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     serializer = ReviewSerializer(review)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated]) # 인증된 사용자의 요청인지 검사하는 데코레이터
# def create_review(request):
#     serializer = ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data)
from .serializers import WholeReviewSerializer, StoreReviewSerializer, ReviewDetailSerializer, ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

def input_data(request):
    json_data = open('reviews/reviews.json').read()
    json_d = json.loads(json_data)
    for i in range(len(json_d['data'])):
        review = Review()
        review.storeid = json_d['data'][i]['store_id']
        review.userid = json_d['data'][i]['user_id']
        review.score = json_d['data'][i]['score']
        # review.content = json_d['data'][i]['content']
        review.reg_time = json_d['data'][i]['reg_time']
        review.save()
    return

# Review 전체
@api_view(['POST'])
def whole_review_list(request):
    reviews = Review.objects.all()
    serializer = WholeReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 특정 Store에 대한 Review 전체
@api_view(['POST'])
def store_review_list(request):
    reviews = Review.objects.filter(storeid=request.data['storeid'])
    serializer = StoreReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 특정 Review에 대한 자세히 보기
@api_view(['POST'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewDetailSerializer(review)
    return Response(serializer.data)

# Review 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자의 요청인지 검사하는 데코레이터
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

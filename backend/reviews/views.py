from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Review
import json
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response


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

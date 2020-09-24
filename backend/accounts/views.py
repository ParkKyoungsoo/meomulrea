from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserDetailSerializer

# 닉네임 중복 여부 체크
@api_view(['GET'])
def user_username(request):
    User = get_user_model()
    try:
        user = User.objects.get(username=request.data.get('username'))
        return Response({'message': '이미 존재하는 닉네임입니다.'})
    except:
        return Response({'message': '사용가능한 닉네임입니다.'})

# 이메일 중복 여부 체크
@api_view(['GET'])
def user_email(request):
    User = get_user_model()
    try:
        user = User.objects.get(email=request.data.get('email'))
        return Response({'message': '이미 존재하는 이메일입니다.'})
    except:
        return Response({'message': '사용가능한 이메일입니다.'})

# res.data.message로 프론트에서 받으면 된다.

# user 모델 추가사항들 저장
# 프론트는 headers에 Token 값 담아서 보내야함
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    serializer = UserDetailSerializer(data=request.data, instance=request.user)
    print(request.data.get('address'))
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

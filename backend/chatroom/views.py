from django.shortcuts import render
from .serializers import ChatRoomSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def create_chatroom(request): # 채팅방 생성
    print(request.data)
    serializer = ChatRoomSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


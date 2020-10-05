from django.shortcuts import render
from .models import makeChatroom
from .serializers import ChatRoomSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chatroom(request):  # 채팅방 생성
    print(request.data)
    serializer = ChatRoomSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def store_chatroom_list(request):
    rooms = makeChatroom.objects.filter(store_id=request.data['store_id'])
    if request.method == 'POST':
        if len(rooms) > 0:
            serializer = ChatRoomSerializer(rooms, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': '해당 식당의 채팅방이 존재하지 않습니다.'})
    else:
        room = makeChatroom.objects.get(user=request.user)
        try:
            room.delete()
            return Response({'message': '채팅방이 삭제되었습니다.'})
        except:
            return Response({'message': '본인이 만든 방이 아닙니다.'})

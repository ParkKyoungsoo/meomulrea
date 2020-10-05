# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from chatroom.views import user_minuscount, user_pluscount,delete_chatroom
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    messagelist = {}

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_name,' 방에 접속하였습니다. ', self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # chatroom DB테이블에 참여인원수 update
        room_info = self.room_name
        room_info = room_info.split("_")
        store_info = room_info[0]
        user_info = room_info[1]
        a = user_pluscount(self, store_info, user_info)
        print(a)

        self.accept() # 연결 수락 
        if self.messagelist.get(self.room_name):
            for msg in self.messagelist[self.room_name]:
                self.send(text_data=json.dumps({
                    'message': msg
                }))

        

    def disconnect(self, close_code):
        print("disconnect!!!")

        # chatroom DB테이블에서 참여인원수 update -1 
        # 참여인원수 0명이면 delete 해주기 
        # messagelist= {}
        room_info = self.room_name
        room_info = room_info.split("_")
        store_info = room_info[0]
        user_info = room_info[1]

        a = user_minuscount(self, store_info, user_info)
        if a==0 :
            delete_chatroom(self, store_info, user_info)
            self.messagelist[self.room_name] = []
            print("채팅방이 삭제되었습니다. ")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 클라이언트로부터 메세지를 받는다.
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if self.messagelist.get(self.room_name) == None :
            self.messagelist[self.room_name]= []
        self.messagelist[self.room_name].append(message) # 여기에 메세지를 차곡차곡 쌓기. 
        print('receive!!!')
        print(self.messagelist)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # 연결된 사용자들에게 메세지를 보낸다.
    def chat_message(self, event):
        message = event['message']
        print('chat_message!!!')
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
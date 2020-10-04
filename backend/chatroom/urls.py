from django.urls import path

from . import views

app_name = 'chatroom'

urlpatterns = [

#   path('/makechatroom', views.makeChatroom, name='chatroom'),
    path('/createchatroom',views.create_chatroom, name='makechatroom')
]
  
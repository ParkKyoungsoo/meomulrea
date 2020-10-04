from django.db import models
from django.conf import settings

class makeChatroom(models.Model):

    store_id = models.IntegerField(null = False)
    user_id = models.IntegerField(null = False, unique=True)
    room_name = models.CharField(max_length=100, null=True)
    usercount =  models.IntegerField(default=1)

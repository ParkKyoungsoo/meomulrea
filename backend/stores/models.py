from django.db import models
from django.conf import settings

class Store(models.Model):
    storeid = models.IntegerField()
    
    bizid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    store_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=50, null=True)
    longtitude = models.CharField(max_length=50, null=True)
    start_time = models.CharField(max_length=50, null=True)
    end_time = models.CharField(max_length=50, null=True)
    min_price = models.IntegerField()


class Workday(models.Model):
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE)
    mon = models.IntegerField()
    tue = models.IntegerField()
    wed = models.IntegerField()
    thu = models.IntegerField()
    fri = models.IntegerField()
    sat = models.IntegerField()
    sun = models.IntegerField()
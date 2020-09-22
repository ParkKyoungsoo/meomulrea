from django.shortcuts import render
from .models import Store, Workday
import requests

def save_stores(request):
    URL = 'data.json'
    for i in range(100):
        response = requests.get(URL)
        json = response.json()
        print(json)
        for item in json:
            store = Store()
            storeid = item.get('id')
            store_name = item.get('name')
            category = item.get('category_list')[0].category[0]
            address = item.get('address')
            latitude = item.get('latitude')
            longtitude = item.get('longtitude')
            start_time = item.get('bhour_list').start_time
            end_time = item.get('bhour_list').end_time
            mon = item.get('bhour_list')[0].mon
            tue = item.get('bhour_list')[0].tue
            wed = item.get('bhour_list')[0].wed
            thu = item.get('bhour_list')[0].thu
            fri = item.get('bhour_list')[0].fri
            sat = item.get('bhour_list')[0].sat
            sun = item.get('bhour_list')[0].sun
    return

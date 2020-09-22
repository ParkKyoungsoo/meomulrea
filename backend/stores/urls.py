from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.save_store, name='save_store')
]
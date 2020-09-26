from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('input_data/', views.input_data)
]
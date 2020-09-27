from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('input_data/', views.input_data),
    path('whole_review_list/', views.whole_review_list),
    path('store_review_list/', views.store_review_list),
]
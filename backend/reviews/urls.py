from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list),
    path('create/', views.create_review),
    path('<int:review_pk>/', views.review_detail),
]
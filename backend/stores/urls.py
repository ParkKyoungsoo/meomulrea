from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.save_store, name='save_store'),
    path('store_list/', views.store_list, name='store_list'),
    path('<int:storeid>/', views.store_detail, name='store_detail'),
    # path('review_list/', views.review_list),
    # path('<int:storeid>/create_review/', views.create_review),
    # path('<int:storeid>/<int:review_pk>/', views.review_detail),
]
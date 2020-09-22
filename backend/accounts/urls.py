from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user_email/', views.user_email, name='user_email'),
    path('user_detail/', views.user_detail, name='user_detail'),
]
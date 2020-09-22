from rest_framework import serializers
from .models import Review
from accounts.serializers import UserSerializer

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)   # is_valid() 에서 유무검증 안한다
    class Meta:
        model = Review
        fields = '__all__'
from rest_framework import serializers
<<<<<<< HEAD
from .models import Review, Reply
from accounts.serializers import UserProfileSerializer
=======
from .models import Review
>>>>>>> 4439bf900e6e12304853cf4396b65d34d2566f43

class WholeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class StoreReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
<<<<<<< HEAD
=======


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
>>>>>>> 4439bf900e6e12304853cf4396b65d34d2566f43

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Review
        fields = ['id', 'content', 'storeid', 'userid', 'score', 'reg_time', 'created_at', 'user']


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class ReviewReplySerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    class Meta:
        model = Reply
        fields = ['id', 'content', 'created_at', 'review']

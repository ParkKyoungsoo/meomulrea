from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# MyUser 모델은 User 객체의 OneToOneField 로 생성했다.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        # extra_kwargs = {
        #                 "password": {"write_only": True},
        #                 }


class UserDetailSerializer(UserSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'usertype', 'gender', 'address', 'date_of_birth', 'biznumber', 'bizname', 'bizimage', 'bizaddress']
        fields = ['id', 'username', 'email', 'usertype', 'gender', 'address', 'birth_year', 'biznumber', 'bizname', 'bizcategory', 'bizimage', 'bizaddress']

from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff')


class UserAllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('__all__')


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone', 'address', 'user_image')


class UserProfileListSerializer(serializers.ModelSerializer):
    user = UserAllDataSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'phone', 'address', 'user_image')

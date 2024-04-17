from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
from rest_framework.views import APIView
# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         if data['username']:
#             if User.objects.filter(username = data['username']).exists():
#                 raise serializers.ValidationError('Username is already Taken.')
#             return data
#
#     def create(self, validated_data):
#         user = User.objects.create(username = validated_data['username'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return validated_data

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'password', 'name', 'phone_number', 'username', 'created_at', 'updated_at', 'role']
#         extra_kwargs = {
#             'password': {},  # Ensure password is write-only
#         }
#     password = serializers.CharField(max_length=50, write_only=True, required=True)
#
#
#
class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('email is taken')
        return data

    def create(self, validated_data):
        validated_data['role'] = User.CUSTOMER  # Set the role to CUSTOMER when creating a new user
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user







from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    id = serializers.IntegerField(read_only=True, source='pk')
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'phone_number', 'username', 'role']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email is taken')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            phone_number=validated_data.get('phone_number', ''),
            username=validated_data.get('username', ''),
            role=validated_data.get('role', User.CUSTOMER)
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

#Forgot Password
class ForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ForgotpasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()
    
class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

# To change Email, Name, PhoneNumber
class UserDetailSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    email = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    
#Address
class RegisterAddress(serializers.Serializer):  
    id = serializers.IntegerField(read_only=True, source='pk')
    token = serializers.CharField(write_only=True)
    street = serializers.CharField()
    apt_name = serializers.CharField()
    business_name = serializers.CharField()
    zip_code = serializers.IntegerField()
    

class EditAddressSerializer(serializers.Serializer):
    id = serializers.CharField()
    street = serializers.CharField()
    apt_name = serializers.CharField()
    business_name = serializers.CharField()
    zip_code = serializers.IntegerField()
    
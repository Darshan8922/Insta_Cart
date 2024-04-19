from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer, ForgotSerializer, ChangePasswordSerializer, ForgotpasswordSerializer, RefreshTokenSerializer
from django.contrib.auth import authenticate
from datetime import datetime
from django.conf import settings
import jwt
from accounts.models import User
from .helpers import send_forget_password_mail
import uuid
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'User created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                current_time = datetime.now().isoformat()
                # auth_token = jwt.encode({'email': user.email, 'time': current_time}, settings.JWT_SECRET_KEY)
                auth_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user).access_token
                
                user.access_token=auth_token
                user.refresh_token=refresh_token
                user.save()
                print(user.access_token)
                print(user.refresh_token)
                serializer = UserRegistrationSerializer(user)
                return Response({'status': True, 'access_token': str(auth_token), 'refresh_token': str(refresh_token), 'user': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': False, 'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPI(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            user = authenticate(request, email=email, password=old_password)
            if user:
                if new_password == confirm_password:
                    # Validate the new password
                    user.set_password(new_password)
                    user.save()
                    return Response({'status': True, 'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status': False, 'message': 'Both passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'status': False, 'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': False, 'message': 'Enter valid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#Forgot Password

class ForgotAPI(APIView):
    def post(self, request):
        serializer = ForgotSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            if not User.objects.filter(email=email).first():
                return Response({'status': False, 'message': 'User does not exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            user_obj = User.objects.get(email=email)
            token = str(uuid.uuid4())
            user_obj.forgot_password_token = token
            print(user_obj)
            print(user_obj.forgot_password_token)
            user_obj.save()
            send_forget_password_mail(user_obj, token)
            print(token)
            return Response({'status': True, 'message': 'An email has been sent'}, status=status.HTTP_200_OK)

class ForgotChangePassword(APIView):
    def post(self, request):
        serializer = ForgotpasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            if not User.objects.filter(forgot_password_token = token).first():
                return Response({'status': False, 'message': 'Token is not Valid'}, status=status.HTTP_400_BAD_REQUEST)
                
            user_obj = User.objects.get(forgot_password_token = token)
            print(user_obj)
            password = serializer.validated_data['password']
            user_obj.set_password(password)
            user_obj.save()
            return Response({'status': True, 'message': 'Password has been updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': False, 'message': 'Enter valid credentials'}, status=status.HTTP_400_BAD_REQUEST)
             
        
class ValidateRefreshToken(APIView):
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['refresh_token']
            
            try:
                user_obj = User.objects.get(refresh_token=token)
            except User.DoesNotExist:
                return Response({'status': False, 'message': 'Token is not valid'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Generate a new access token for the user
            access_token = AccessToken.for_user(user_obj)
            
            # Update the user's access token in the database
            user_obj.access_token = access_token
            user_obj.save()
            
            return Response({'status': True, 'access_token': str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'status': False, 'message': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
            
            


 




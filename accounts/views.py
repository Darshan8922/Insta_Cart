from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, LoginSerializer, ForgotSerializer
from django.contrib.auth import authenticate
from datetime import datetime
from django.conf import settings
import jwt

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
            print(user)
            if user is not None:
                current_time = datetime.now().isoformat()
                auth_token = jwt.encode({'email': user.email, 'time': current_time}, settings.JWT_SECRET_KEY)
                serializer = UserRegistrationSerializer(user)
                return Response({'status': True, 'token': auth_token, 'user': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': False, 'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordAPI(APIView):
    def post(self, request):
        serializer = ForgotSerializer(data=request.data)
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

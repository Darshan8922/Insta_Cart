from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status' : False,
                'message' : serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'status' : True, 'message' : 'user created'}, status.HTTP_201_CREATED)

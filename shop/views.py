from django.shortcuts import render
from rest_framework import generics
from .serializers import ShopSerializer, ShopCategorySerializer
from .models import *
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ShopCategoryList(generics.ListCreateAPIView):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializer

class ShopList(APIView):

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            category_id = serializer.validated_data['id']
            try:
                shops = Shop.objects.filter(category_id=category_id)
                serializer = ShopSerializer(shops, many=True)
                return Response({'status': True, 'Shops': serializer.data}, status=status.HTTP_201_CREATED)
            except ShopCategory.DoesNotExist:
                raise Http404("Category does not exist")
        else:
            return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

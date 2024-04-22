from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.

class ShopCategoryList(generics.ListCreateAPIView):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializer

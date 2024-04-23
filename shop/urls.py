from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.


urlpatterns = [
    #CategoryList
    path("list-category/", ShopCategoryList.as_view()),
    path("list-shop/", ShopList.as_view()),
]

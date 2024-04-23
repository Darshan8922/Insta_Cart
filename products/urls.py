from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.


urlpatterns = [

    path("ListProduct/", ListProduct.as_view()),
]

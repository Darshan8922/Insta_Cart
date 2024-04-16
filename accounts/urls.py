from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
]

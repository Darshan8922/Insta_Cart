from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view()),
    path("forgot_password/", ForgotPasswordAPI.as_view()),
]

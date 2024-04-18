from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view()),
    path("change_password/", ChangePasswordAPI.as_view()),
    path("forgot_password/", ForgotAPI.as_view()),
]

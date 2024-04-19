from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view()),
    path("change_password/", ChangePasswordAPI.as_view()),
    path("user-detail/", GetUserDetail.as_view()),
    #Forgot Password
    path("forgot_password/", ForgotAPI.as_view()),
    path("change-password/", ForgotChangePassword.as_view()),
    
    path("refresh-token/", ValidateRefreshToken.as_view()),
    
    #ChangeDetail
    path("change-details/", ChangeDetail.as_view()),
    
]

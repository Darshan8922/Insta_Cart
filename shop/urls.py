from django.urls import path
from .views import *

urlpatterns = [
    #CategoryList
    path("list-category/", ShopCategoryList.as_view()),
]
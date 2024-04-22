from rest_framework import serializers
from .models import *


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = ['id', 'title', 'logo']
from rest_framework import serializers
from .models import *


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = ['id', 'title', 'logo']
        
        
class ShopSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField(read_only=True)
    logo = serializers.CharField(read_only=True)

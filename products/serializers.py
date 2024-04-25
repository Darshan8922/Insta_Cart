from rest_framework import serializers
from .models import Product, Image, ProductCategory, ProductSubCat

class ListProductSerializer(serializers.ModelSerializer):
    measurement = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    subcat = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_measurement(self, obj):
        return obj.measurement.type if obj.measurement else None
    
    def get_category(self, obj):
        return {'id': obj.category.id, 'title': obj.category.title} if obj.category else None
    
    def get_subcat(self, obj):
        return {'id': obj.subcat.id, 'title': obj.subcat.title} if obj.subcat else None

        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__' 


class SubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCat
        fields = '__all__'
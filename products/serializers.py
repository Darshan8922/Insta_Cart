from rest_framework import serializers
from .models import Product, Image

class ListProductSerializer(serializers.ModelSerializer):
    measurement = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_measurement(self, obj):
        return obj.measurement.type if obj.measurement else None

        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__' 

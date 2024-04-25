from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Image, Measurement, ProductSubCat
from shop.models import Shop
from .serializers import ListProductSerializer, ImageSerializer, SubCatSerializer, ProductSubCat
from rest_framework import generics

class ListProduct(APIView):
    def get(self, request):
        shop_id = request.query_params.get('id')
        if Shop.objects.filter(id=shop_id).exists():
            shop = Shop.objects.get(id=shop_id)
            products = Product.objects.filter(shop=shop)

            serializer = ListProductSerializer(products, many=True)
            
            product_images = {}
            for product in products:
                images = Image.objects.filter(product_id=product.id)
                image_serializer = ImageSerializer(images, many=True)
                product_images[product.id] = image_serializer.data
            
            return Response({"products": serializer.data, "images": product_images})
        else:
            return Response({"message": "Shop not found"}, status=404)



class ListSubCat(generics.ListCreateAPIView):
    queryset = ProductSubCat.objects.all()
    serializer_class = SubCatSerializer
    
class ProductBySubCatAPIView(generics.ListAPIView):
    serializer_class = ListProductSerializer

    def get_queryset(self):
        subcat_id = self.kwargs['subcat_id']
        return Product.objects.filter(subcat_id=subcat_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        subcat_id = self.kwargs['subcat_id']
        products = queryset
        serializer = self.get_serializer(products, many=True)
        product_images = {}
        for product in products:
            images = product.image_set.all() 
            image_serializer = ImageSerializer(images, many=True)
            product_images[product.id] = image_serializer.data

        response_data = {
            'products': serializer.data,
            'images': product_images
        }
        return Response(response_data)
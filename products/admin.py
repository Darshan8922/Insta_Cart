from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Measurement)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(ProductSubCat)

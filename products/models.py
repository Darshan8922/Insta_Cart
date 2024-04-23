from django.db import models
from shop.models import Shop
from accounts.models import User

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, unique=True)
    logo = models.CharField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.title
    
class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.type
    
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE) 
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) 
    price = models.CharField(max_length=5)
    details = models.CharField(max_length=5000, blank=True, null=True)
    ingredients = models.CharField(max_length=5000, blank=True, null=True)
    directions = models.CharField(max_length=5000, blank=True, null=True)
    m_qty = models.CharField(max_length=6, blank=True, null=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, blank=True, null=True)     
    
    def __str__(self):
        return f"{self.title} {self.m_qty} {self.measurement}"

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    def __str__(self):
        return f"Image {self.id} for {self.product_id.title}"
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.CharField(max_length=2)
    review = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.product_id.title} {self.user_id.name} {self.rating}"
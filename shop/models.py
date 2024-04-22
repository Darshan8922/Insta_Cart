from django.db import models

# Create your models here.

from django.db import models

class ShopCategory(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, unique=True)
    logo = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.title

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=600, blank=True)
    discount = models.CharField(max_length=2, blank=True)
    in_store_prices = models.BooleanField(default=True)
    logo = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.title

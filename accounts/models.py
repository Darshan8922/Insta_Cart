from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

# Create your models here.
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (1, 'Vendor'),
        (2, 'Customer'),
    )
    role = models.IntegerField(choices=ROLE_CHOICES)

    def __str__(self):
        return self.email



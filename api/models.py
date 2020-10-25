from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    available = models.BooleanField(default=True)

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now=True)
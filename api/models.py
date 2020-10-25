from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(
            self.id, self.customer, self.created_at.strftime("%d/%m/%Y - %H:%M")
        )
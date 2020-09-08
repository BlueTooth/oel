from django.db import models

from customers.models import Customer

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    pictureUrl = models.URLField()
    number = models.IntegerField()
    salesPrice = models.DecimalField(decimal_places=2, max_digits=10000)
    purchasingPrice = models.DecimalField(decimal_places=2, max_digits=10000)
    discount = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
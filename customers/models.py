from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    amout = models.DecimalField(decimal_places=2, max_digits=10000)

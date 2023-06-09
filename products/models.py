from django.db import models

#what you want to see on the page --- create classes
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=200)
    discount = models.FloatField()

# Create your models here.

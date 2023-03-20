from django.db import models

#what you want to see on the page --- create classes
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


# Create your models here.

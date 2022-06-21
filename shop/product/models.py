from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/products/original')
    thumbnail = models.ImageField(upload_to='images/products/thumbnail', null=True)
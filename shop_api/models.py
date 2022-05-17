from distutils.command.upload import upload
from random import choices
from secrets import choice
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

DELIVERY_CHOICES=(
    ('4 days delivery','4 DAYS DELIVERY'),
    ('fastdelivery','FASTDELIVERY')
)

STOCK_CHOICES=(
    ('instock','IN STOCK'),
    ('outofstock','OUT OF STOCK')
)
class Item(models.Model):
    image = models.ImageField(upload_to='images') # image
    name = models.CharField(max_length=80)
    description = models.TextField()
    delivery = models.CharField(max_length=30,choices=DELIVERY_CHOICES,default='fastdelivery')
    category = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    amount = models.IntegerField(default=1)
    stock = models.CharField(max_length=30,choices=STOCK_CHOICES,default='instock')

    def __str__(self):
        return self.name

class Special(models.Model):
    image = models.ImageField(upload_to='images') # image
    name = models.CharField(max_length=80)
    description = models.TextField()
    delivery = models.CharField(max_length=30,choices=DELIVERY_CHOICES,default='fastdelivery')
    category = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    amount = models.IntegerField(default=1)
    stock = models.CharField(max_length=30,choices=STOCK_CHOICES,default='instock')

    def __str__(self):
        return self.name

class Random(models.Model):
    image = models.ImageField(upload_to='images') # image
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


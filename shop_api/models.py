from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Item(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=80)
    description = models.TextField()
    category = models.CharField(max_length=30)
    price = models.CharField(max_length=10)


    def __str__(self):
        return self.name


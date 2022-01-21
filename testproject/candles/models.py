from distutils.command.upload import upload
import string
from unicodedata import name
from django.db import models

# Create your models here.

class Candle(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    


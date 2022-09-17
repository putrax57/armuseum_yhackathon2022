from statistics import mode
from django.db import models
from django.contrib import admin
from decimal import Decimal

# Create your models here.

class Exhibit_Items(models.Model):
    items_no = models.DecimalField(max_digits=10,decimal_places=0)
    title = models.CharField(max_length= 100)
    artist = models.CharField(max_length= 100,blank =True)
    summary = models.CharField(max_length= 200,blank =True)
    width = models.CharField(max_length= 10,blank =True)
    height = models.CharField(max_length= 10,blank =True)
    pic_url = models.URLField(blank =True)
    download_url = models.URLField(blank =True)
    fungibility = models.CharField(max_length= 3,blank =True)
    price = models.DecimalField(max_digits=20,decimal_places=10,default=0.0,blank =True)
    blockchain_keys = models.CharField(max_length= 250,blank =True)
    buystatus = models.BooleanField(default=0,blank =True)
    
    def __str__(self):
        return self.title
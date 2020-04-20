from django.db import models
import datetime
from django.db.models.signals import pre_save 

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class  Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200)
    detail_text = models.TextField(max_length=1000)
    price = models.FloatField()
    

    def __str__(self):
        return self.name





    
     

       
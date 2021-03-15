from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
    seller = models.TextField()
    category = models.TextField()
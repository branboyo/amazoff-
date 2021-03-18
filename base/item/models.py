from django.db import models

# Create your models here.

class Item(models.Model):
    idn = models.TextField()
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
    image = models.TextField()
    category = models.TextField()
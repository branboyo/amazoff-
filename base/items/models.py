from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.TextField()
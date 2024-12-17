from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    expiry_date = models.DateTimeField(blank=True, null=True)

    


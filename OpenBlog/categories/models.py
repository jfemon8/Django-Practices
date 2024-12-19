from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Category"  
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
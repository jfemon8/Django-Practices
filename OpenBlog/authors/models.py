from django.db import models

# Create your models here.

class Authors(models.Model):
    image = models.ImageField(upload_to='author_images/')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    phone = models.CharField(max_length=15, unique=True)
    
    class Meta:
        verbose_name = "Author"  
        verbose_name_plural = "Authors"
    
    def __str__(self):
        return self.name
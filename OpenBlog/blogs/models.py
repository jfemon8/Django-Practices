from django.db import models
from authors.models import Authors
from categories.models import Categories

# Create your models here.

class Blogs(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories)
    
    class Meta:
        verbose_name = "Blog"  
        verbose_name_plural = "Blogs"
    
    def __str__(self):
        return f"Title: {self.title} | Author: {self.author.name}" 
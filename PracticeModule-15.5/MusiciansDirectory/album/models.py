from django.db import models
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1, '1'
        TWO = 2, '2'
        THREE = 3, '3'
        FOUR = 4, '4'
        FIVE = 5, '5'
    album_name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=RatingChoices.choices)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    


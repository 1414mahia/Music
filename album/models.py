from django.db import models

from musician.models import MusicModel

# Create your models here.

class Album(models.Model):
    album_name =models.CharField(max_length=20)
    release_date =models.DateTimeField()
    
    rating_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5') ,
    ]
    instrument_rating = models.CharField(max_length=10, choices=rating_CHOICES)
    musician = models.ForeignKey(MusicModel, on_delete=models.CASCADE, related_name='albums')
   
    def __str__(self):
        return self.album_name
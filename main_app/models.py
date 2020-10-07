from django.db import models
from django.urls import reverse

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    multipart = models.BooleanField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': self.id})
        
        
    
from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    multipart = models.BooleanField()
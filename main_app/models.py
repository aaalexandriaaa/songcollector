from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Selection Tuples
VENUES = (
    ('STJ', 'at St. John'),
    ('OPC', 'at Oglethorpe Presbyterian Church'),
    ('RIN', 'as a Paid Ringer'),
    ('FUN', 'at a Funeral'),
    ('WED', 'at a Wedding')
)


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('books_detail', kwargs={'pk': self.id})

class Song(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': self.id})

    # def sung_for_today(self):
    #     return self.performance_set.filter(date=date.today()).count() >= len(VENUES)
        
class Performance(models.Model):
    date = models.DateField('performance date')
    venue = models.CharField(max_length=3, choices=VENUES, default=VENUES[0][0])
    song=models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Performed {self.get_venue_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
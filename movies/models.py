from django.utils import timezone
from django.db import models

# django.db is involved with databases
# Create your models here.

# Model class encapsulate a lot of functionality for storing a model in the database


class Genre(models.Model):
    name = models.CharField(max_length=255)

    # overwrite str magic method
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    releaseYear = models.IntegerField()
    numberInStock = models.IntegerField()
    dailyRate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    actors = models.TextField()
    
    
    
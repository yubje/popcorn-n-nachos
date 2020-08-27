from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}' 

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    overview  = models.TextField()
    original_language = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100, default='', null=True)
    genres = models.ManyToManyField(Genre,related_name='movies')
    
    def __str__(self):
        return self.title

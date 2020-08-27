from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from movies.models import Movie

class User(AbstractUser):
  movies = models.ManyToManyField(Movie, through='Rate')

class Rate(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  def __str__(self):
    return '%s: %d' % (self.movie, self.rate)
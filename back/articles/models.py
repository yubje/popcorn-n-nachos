from django.db import models
from django.conf import settings
from movies.models import Movie 


class Article(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  content = models.CharField(max_length=200)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default='', null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
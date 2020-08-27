from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('recommend/', views.recommend, name='recommend'),
  path('myinfo/', views.myinfo, name='myinfo'),
  path('get_rates/', views.get_rates, name='get_rates'),
  path('compute_genres/', views.compute_genres, name='compute_genres'),
]
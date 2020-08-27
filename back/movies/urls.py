from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:movie_pk>/', views.detail, name='detail'),
  path('<int:movie_pk>/genre/', views.genre, name='genre'),
  path('<int:movie_pk>/rate/<int:ori_rate>/', views.rate, name='rate'),
  path('<int:movie_pk>/rate_delete/', views.rate_delete, name='rate_delete'),
  path('<int:movie_pk>/rate_info/', views.rate_info, name='rate_info'),
  path('genre_list/', views.genre_list, name='genre_list'),
  path('<int:movie_pk>/get_genres/', views.get_genres, name='get_genres'),
  
]

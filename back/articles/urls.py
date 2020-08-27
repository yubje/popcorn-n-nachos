from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
  path('', views.index, name='index'),

  #article
  path('bymovie/<int:movie_pk>/', views.bymovie, name='bymovie'),
  path('create/', views.create, name='create'),
  path('<int:article_pk>/', views.detail, name='detail'),
  path('<int:article_pk>/update_delete/', views.update_delete, name='update_delete'),
  path('byuser/<int:user_pk>/', views.byuser, name='byuser'),
  
  #comment
  path('<int:article_pk>/comments_list/', views.comments_list, name='comments_list'),
  path('<int:article_pk>/comments_create/', views.comments_create, name='comment_create'),
  path('<int:article_pk>/<int:comment_pk>/update_delete/', views.comments_update_delete, name='comments_update_delete'),
  
  
]



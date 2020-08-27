from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import User, Rate
from movies.models import Movie, Genre
from .serializers import UserSerializer, RecommendSerializer, RateSerializer




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myinfo(request):
  User = get_user_model()
  user = get_object_or_404(User, id=request.user.id)
  serializer = UserSerializer(user)
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_rates(request):
  User = get_user_model()
  user = get_object_or_404(User, id=request.user.id)
  rated_movies = Rate.objects.filter(user=user)
  
  serializer = RateSerializer(rated_movies, many=True)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def compute_genres(request):
  my_rates = request.data
  
  
  rated_genres = {}
  top_genres={}
  total = 0
  for my_rate in my_rates:
    movie = Movie.objects.get(id=my_rate["movie"])
    for genre in movie.genres.all():
      if genre.name in rated_genres:
        rated_genres[genre.name] += my_rate['rate']
        total += my_rate['rate']
      else:
        rated_genres[genre.name] = my_rate['rate']
        total += my_rate['rate']
  
  for rated_genre in rated_genres:
    rated_genres[rated_genre] = round(rated_genres[rated_genre]/total*100, 2)

  top_genres = {x[0]: x[1] for x in sorted(rated_genres.items(), key=lambda x: -x[1])[:3]}
  
  return Response(top_genres)

  


@api_view(['GET'])
def recommend(request):
  if request.user.is_authenticated:
    User = get_user_model()
    user = get_object_or_404(User, id=request.user.id)    # 굳

    rated_genres = {} #평점 장르
    for movie in user.movies.all(): #사용자가 평점을 매긴 모든 영화
      rating = get_object_or_404(Rate, user=request.user, movie_id=movie.id)
      rate = rating.rate # 영화의 평점
      movie_genres = movie.genres.all() # 평점을 매긴 영화의 모든 장르
      for genre_id in movie_genres:
        if genre_id in rated_genres:
          rated_genres[genre_id] += rate
        else:
          rated_genres[genre_id] = rate


    rated_genres = sorted(rated_genres.items(), key=lambda x:x[1], reverse=True) #좋아요 장르 비율 큰순서부터

    # 장르가 0개/1/2/3-
    if not (rated_genres):
      recommend_movies = Movie.objects.order_by('?')[:10] 
      serializer = RecommendSerializer(recommend_movies, many=True)
    elif len(rated_genres) == 1:
      choose_genre = Genre.objects.get(id=rated_genres[0][0])
      recommend_movies = Movie.objects.filter(genres=choose_genre.id).order_by('?')[:5] | Movie.objects.order_by('?')[:5] 
      serializer = RecommendSerializer(recommend_movies, many=True)

    elif len(rated_genres) == 2:
      recommend_movies = []
      choose_genre1 = Genre.objects.get(id=rated_genres[0][0])
      choose_genre2 = Genre.objects.get(id=rated_genres[1][0])
      recommend_movies = Movie.objects.filter(genres=choose_genre1.id).order_by('?')[:5] | Movie.objects.filter(genres=choose_genre2.id).order_by('?')[:5]
      serializer = RecommendSerializer(recommend_movies, many=True)
    
    else:
      recommend_movies = Movie.objects.order_by('?')[:1]
      rated_genres = rated_genres[:3]
      for i, j in rated_genres:
        choose_genre = Genre.objects.get(id=i)
        recommend_movies |= Movie.objects.filter(genres=choose_genre.id).order_by('?')[:3]
      serializer = RecommendSerializer(recommend_movies, many=True)
  else:
    recommend_movies = Movie.objects.order_by('?')[:10]
    print(recommend_movies)
    serializer = RecommendSerializer(recommend_movies, many=True)
    
  return Response(serializer.data)



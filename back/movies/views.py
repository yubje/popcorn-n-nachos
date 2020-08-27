from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from accounts.models import Rate
from .models import Genre, Movie
from articles.models import Article
from .serializers import GenreListSerializer, MovieListSerializer, MovieSerializer
from articles.serializers import ArticleListSerializer
from accounts.serializers import RateSerializer


@api_view(['GET'])
def index(request):
    genres_list = Genre.objects.all()
    genre_id = request.GET.get('genre')
    if genre_id:
        movies = get_object_or_404(Genre, id=genre_id).movies.all()
    else:
        movies = Movie.objects.all()
    
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 각 영화의 장르들 뽑아오기 
@api_view(['GET'])
def genre(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def rate(request, movie_pk, ori_rate):
    ori_rate, flag = Rate.objects.get_or_create(user=request.user, movie_id=movie_pk, rate=ori_rate)
    
    serializer = RateSerializer(data=request.data, instance=ori_rate)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def rate_delete(request, movie_pk):
    try:
        ori_rate = Rate.objects.filter(user=request.user).filter(movie_id=movie_pk)
        for rate in ori_rate:
            rate.delete()
        
        return Response({'message: 성공적으로 삭제되었습니다.'})
    except:
        return Response(None)


@api_view(['POST'])
def rate_info(request, movie_pk):
    try:
        ori_rate = Rate.objects.get(user=request.user, movie_id=movie_pk)
        serializer = RateSerializer(ori_rate)
        return Response(serializer.data)
    except:
        serializer = RateSerializer()
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_genres(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = movie.genres.all()
    serializer  = GenreListSerializer(genres, many=True)
    return Response(serializer.data)


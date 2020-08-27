from rest_framework import serializers
from .models import Movie, Genre


# 장르 목록
class GenreListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = '__all__'
    read_only_fields = ('name', 'id',)

# 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'
    read_only_fields = ('title', 'id', 'poster_path', 'original_title', 'vote_average', 'release_date', 'popularity', 'vote_count', 'vote_average', 'adult', 'overview', 'original_language', 'genres', )

# 영화 디테일 
class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'
    read_only_fields = ('title', 'id', 'poster_path', 'original_title', 'vote_average', 'release_date', 'popularity', 'vote_count', 'vote_average', 'adult', 'overview', 'original_language', 'backdrop_path', 'genres', )



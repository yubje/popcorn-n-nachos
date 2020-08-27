from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Rate
from movies.models import Movie

User = get_user_model()

# 진짜 그냥 유저
class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = ('id', 'username',)
   

# 내가 평점 매긴 영화들
class RateSerializer(serializers.ModelSerializer):
  # rates = serializers.StringRelatedField(many=True)
  user = UserSerializer(required=False)
  class Meta:
    model = Rate
    fields = ('rate', 'user', 'movie')


class RecommendSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('title', 'id', 'original_title', 'vote_average', 'genres', 'backdrop_path')
    read_only_fields = ('title', 'id', 'original_title', 'vote_average', 'genres', 'backdrop_path')

class MyInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    read_only_fields = '__all__'





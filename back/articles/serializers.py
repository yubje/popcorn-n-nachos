from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment

# article 리스트
class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        # 게시글 제목이랑 작성자만 보여주기
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
        
# article create
class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # Article의 comments 필드에 comment pk들이 저장 돼 있음
    class Meta:
        model = Article
        # 모든 정보 다 보여주기 
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

#article update
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 모든 정보 다 보여주기 
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

# article detail
class ArticleDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # Article의 comments 필드에 comment pk들이 저장 돼 있음
    class Meta:
        model = Article
        # 모든 정보 다 보여주기 
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at',)

# commentlist -> 게시글에서 보여줄 댓글 목록
class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article', 'movie', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

# comment 생성을 위한 
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article', 'movie', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user','created_at', 'updated_at' )

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'article', 'movie', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user','created_at', 'updated_at' )



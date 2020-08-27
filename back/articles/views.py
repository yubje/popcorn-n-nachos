from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, ArticleDetailSerializer, ArticleUpdateSerializer
from .serializers import CommentListSerializer, CommentSerializer, CommentUpdateSerializer


@api_view(['GET'])
def index(request):
    articles = Article.objects.order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# articles 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)

@api_view(['GET'])
def bymovie(request, movie_pk):
    articles = Article.objects.filter(movie=movie_pk).order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def byuser(request, user_pk):
    articles = Article.objects.filter(user=user_pk)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'PUT':
            serializer = ArticleUpdateSerializer(data=request.data, instance=article)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '성공적으로 수정되었습니다.'})
        else:
            article.delete()
            return Response({'message': '삭제 완료.'})

# comment
@api_view(['POST'])
def comments_list(request, article_pk):
    comments = Comment.objects.filter(article_id=article_pk).order_by('-pk')
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, article_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article_id=article_pk)
       
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comments_update_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentUpdateSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '수정 완료.'})
        else:
            comment.delete()
            return Response({'message': '삭제 완료.'})







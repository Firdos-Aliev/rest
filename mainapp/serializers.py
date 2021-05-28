from django.db import models
from django.db.models import fields
from mainapp.models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'time']


class PostListSerializer(serializers.ModelSerializer):
    """Список всех постов"""
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'name', 'text', 'is_active', 'comment_set', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comment_set.all().count()


class PostDetailSerializer(serializers.ModelSerializer):
    """Вывод поста"""
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_comment_count(self, obj):
        return obj.comment_set.all().count()


class PostCreateSerializer(serializers.ModelSerializer):
    """Создание поста"""
    class Meta:
        model = Post
        fields = ['name', 'text']


class PostUpdateSerializer(serializers.ModelSerializer):
    """Обновление поста"""
    class Meta:
        model = Post
        fields = "__all__"

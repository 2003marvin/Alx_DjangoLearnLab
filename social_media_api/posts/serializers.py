# posts/serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id', 
            'post', 
            'author', 
            'author_username', 
            'content', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 
            'title', 
            'content', 
            'slug', 
            'author', 
            'author_username', 
            'created_at', 
            'updated_at', 
            'comments', 
            'comments_count'
        ]
        read_only_fields = [
            'id', 
            'slug', 
            'author', 
            'created_at', 
            'updated_at', 
            'comments', 
            'comments_count'
        ]

    def get_comments_count(self, obj):
        return obj.comments.count()
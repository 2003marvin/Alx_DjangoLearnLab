from django.shortcuts import render

# posts/views.py
from rest_framework import viewsets, permissions
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Post, Like, Notification

from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for Post model with additional actions
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Optional: Add filtering capabilities
        queryset = Post.objects.all()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    @action(detail=True, methods=['post'])
    def add_comment(self, request, slug=None):
        """
        Custom action to add a comment to a specific post
        """
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(
                post=post, 
                author=request.user
            )
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)

class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for Comment model
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


User = get_user_model()

def get_following_posts(request):
    user = request.user
    following_users = user.following.all()  # Fetch users the current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    return posts


class LikePostView(generics.CreateAPIView):
    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(user=post.author, message=f"{request.user} liked your post.")
        return Response({"message": "Post liked"}, status=201)
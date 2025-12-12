from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from posts.models import Post, Like
from notifications.models import Notification
from .serializers import LikeSerializer, NotificationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    """
    Handle liking a post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Prevent liking own post
    if post.author == request.user:
        return Response(
            {'error': 'You cannot like your own post'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Check if like already exists
    like, created = Like.objects.get_or_create(
        user=request.user, 
        post=post
    )
    
    if created:
        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='like',
            content_type=ContentType.objects.get_for_model(post),
            object_id=post.id
        )
        
        return Response(
            LikeSerializer(like).data, 
            status=status.HTTP_201_CREATED
        )
    
    return Response(
        {'message': 'Post already liked'}, 
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    """
    Handle unliking a post
    """
    post = get_object_or_404(Post, pk=pk)
    
    # Remove the like if it exists
    like = Like.objects.filter(user=request.user, post=post)
    
    if like.exists():
        like.delete()
        return Response(
            {'message': 'Post unliked successfully'}, 
            status=status.HTTP_200_OK
        )
    
    return Response(
        {'message': 'Post was not liked'}, 
        status=status.HTTP_200_OK
    )

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for handling user notifications
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retrieve notifications for the current user
        """
        return Notification.objects.filter(
            recipient=self.request.user
        )
    
    def list(self, request, *args, **kwargs):
        """
        Custom list method to mark unread notifications as read
        """
        queryset = self.get_queryset()
        
        # Fetch unread notifications
        unread_notifications = queryset.filter(is_read=False)
        
        # Mark unread notifications as read
        unread_notifications.update(is_read=True)
        
        # Serialize and return notifications
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
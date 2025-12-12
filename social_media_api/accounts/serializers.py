from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from .models import CustomUser
from posts.models import Like, Post
from notifications.models import Notification

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers_count', 'following_count']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

# Ensure we're using the custom user model
User = get_user_model()
username = serializers.CharField() 


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        min_length=3,
        error_messages={
            'required': 'Username is required',
            'max_length': 'Username must be no more than 150 characters',
            'min_length': 'Username must be at least 3 characters'
        }
    )

    email = serializers.CharField(
        required=True,
        max_length=254,
        error_messages={
            'required': 'Email is required',
            'max_length': 'Email must be no more than 254 characters'
        }
    )

    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
        style={'input_type': 'password'},
        max_length=128,
        min_length=8,
        error_messages={
            'required': 'Password is required',
            'max_length': 'Password must be no more than 128 characters',
            'min_length': 'Password must be at least 8 characters'
        }
    )

    password_confirm = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'},
        max_length=128,
        min_length=8,
        error_messages={
            'required': 'Password confirmation is required',
            'max_length': 'Password confirmation must be no more than 128 characters',
            'min_length': 'Password confirmation must be at least 8 characters'
        }
    )

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password', 
            'password_confirm',
            'token'
        ]

    def validate(self, data):
        """Validate that passwords match"""
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                "password": "Passwords do not match."
            })
        return data

    def create(self, validated_data):
        """Create user and generate authentication token"""
        validated_data.pop('password_confirm')  # Remove password_confirm before creating user

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        token = Token.objects.create(user=user)  # Create a token for the user
        user.token = token.key  # Attach the token to the user instance

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, max_length=150)
    email = serializers.CharField(read_only=True, max_length=254)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['created_at']

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField()
    target_details = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id', 
            'recipient', 
            'actor', 
            'verb', 
            'target_details', 
            'timestamp', 
            'is_read'
        ]
    
    def get_actor(self, obj):
        return {
            'id': obj.actor.id,
            'username': obj.actor.username
        }
    
    def get_target_details(self, obj):
        """
        Retrieve details of the target object based on content type
        """
        try:
            if obj.verb == 'like':
                return {
                    'post_id': obj.target.id,
                    'post_title': obj.target.title
                }
            # Add more specific handling for other notification types
            return {}
        except:
            return {}
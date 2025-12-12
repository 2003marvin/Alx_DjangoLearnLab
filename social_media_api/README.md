# Social Media API

## Project Overview
This is a Django-based Social Media API with user authentication and profile management.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Installation Steps
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/accounts/register/`: User registration
- `POST /api/accounts/login/`: User login
- `GET /api/accounts/profile/`: Retrieve user profile (requires token)
- `PUT /api/accounts/profile/`: Update user profile (requires token)

### Authentication Flow
1. Register a new user
2. Receive an authentication token
3. Use the token in the `Authorization` header for subsequent requests
   - Header format: `Authorization: Token <your_token_here>`

## User Model
Custom user model with additional fields:
- username
- email
- bio
- profile_picture
- followers
- following

## Testing
Use tools like Postman or curl to test the API endpoints.

## Security
- Token-based authentication
- Password hashing
- User registration validation
Step 1: Create Post and Comment Models
1.1. Create the posts app
Run the following command to create a new Django app for handling posts and comments:

bash
Copy
Edit
python manage.py startapp posts
Then, add "posts" to the INSTALLED_APPS list in settings.py:

python
Copy
Edit
INSTALLED_APPS = [
    ...,
    'posts',
]
1.2. Define the Post and Comment models
Edit posts/models.py and define the models:

python
Copy
Edit
from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
1.3. Run Migrations
Generate and apply migrations for the new models:

bash
Copy
Edit
python manage.py makemigrations posts
python manage.py migrate
Step 2: Implement Serializers for Posts and Comments
2.1. Create serializers.py in the posts app
Create a new file posts/serializers.py and add the following:

python
Copy
Edit
from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
Step 3: Create Views for CRUD Operations
3.1. Implement ViewSets
Edit posts/views.py and add:

python
Copy
Edit
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
Step 4: Configure URL Routing
4.1. Define URLs for Posts and Comments
Create a new file posts/urls.py:

python
Copy
Edit
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
4.2. Include the posts URLs in the project
Edit social_media_api/urls.py and add:

python
Copy
Edit
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
]
Step 5: Implement Pagination and Filtering
5.1. Add Pagination to settings.py
Edit social_media_api/settings.py and add:

python
Copy
Edit
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
5.2. Add Filtering to Posts
Edit posts/views.py:

python
Copy
Edit
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
Step 6: Test and Validate Functionality
6.1. Run the Server
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
6.2. Test Endpoints in Postman or Django Browsable API
Method	Endpoint	Description
GET	/api/posts/	Get all posts
POST	/api/posts/	Create a new post
GET	/api/posts/{id}/	Retrieve a specific post
PUT/PATCH	/api/posts/{id}/	Update a post (only by author)
DELETE	/api/posts/{id}/	Delete a post (only by author)
GET	/api/comments/	Get all comments
POST	/api/comments/	Create a new comment
GET	/api/comments/{id}/	Retrieve a specific comment
PUT/PATCH	/api/comments/{id}/	Update a comment (only by author)
DELETE	/api/comments/{id}/	Delete a comment (only by author)
Step 7: Document API Endpoints
7.1. Update README
Add the API documentation in your README.md file.

✅ Deliverables Summary
Code Files:

posts/models.py: Post and Comment models.

posts/serializers.py: Serializers for Post and Comment.

posts/views.py: ViewSets for CRUD operations.

posts/urls.py: URL routing for posts and comments.

Updated social_media_api/urls.py to include posts.urls.

Testing Results:

Verify endpoints using Postman or Django Browsable API.

Confirm permissions (only authors can edit/delete their posts/comments).

Ensure pagination and search work correctly.

API Documentation:

Include usage examples in README.md.


## User Follow and Feed Functionality

### Follow Management Endpoints

#### Follow a User
- **Endpoint:** `POST /accounts/follow/<user_id>/`
- **Authentication:** Required
- **Description:** Allow the current user to follow another user
- **Response:**
  - `200 OK`: Successfully followed/already following
  - `400 BAD REQUEST`: Cannot follow self

#### Unfollow a User
- **Endpoint:** `POST /accounts/unfollow/<user_id>/`
- **Authentication:** Required
- **Description:** Allow the current user to unfollow a previously followed user
- **Response:**
  - `200 OK`: Successfully unfollowed/not following

### User Feed Endpoint

#### Retrieve User Feed
- **Endpoint:** `GET /posts/feed/`
- **Authentication:** Required
- **Description:** Retrieve posts from users the current user follows
- **Response:**
  - `200 OK`: List of posts from followed users
  - If no posts are available, returns a message indicating an empty feed

### Model Changes
- Added `following` field to `CustomUser` model
- `following` is a many-to-many relationship to itself
- Allows tracking of user follow relationships

### Implementation Notes
- Users cannot follow themselves
- Feed shows most recent posts first
- Feed returns an empty list with a message if no posts are available
# Likes and Notifications Feature Documentation

## Likes Functionality

### Like a Post
- **Endpoint:** `POST /posts/<post_id>/like/`
- **Authentication:** Required
- **Description:** Allow a user to like a post
- **Restrictions:** 
  - Cannot like own posts
  - Cannot like a post multiple times
- **Response:**
  - `201 CREATED`: Successfully liked the post
  - `400 BAD REQUEST`: Attempted to like own post

### Unlike a Post
- **Endpoint:** `POST /posts/<post_id>/unlike/`
- **Authentication:** Required
- **Description:** Allow a user to remove a like from a post
- **Response:**
  - `200 OK`: Successfully unliked or post was not previously liked

## Notifications System

### Retrieve Notifications
- **Endpoint:** `GET /notifications/`
- **Authentication:** Required
- **Description:** Retrieve user's notifications
- **Features:**
  - Automatically marks unread notifications as read upon retrieval
  - Provides details about notification type, actor, and target

### Notification Types
- `like`: Notification when someone likes a user's post
- `comment`: Notification when someone comments on a user's post
- `follow`: Notification when someone follows a user

### Notification Object Structure
- `id`: Unique identifier
- `recipient`: User receiving the notification
- `actor`: User who performed the action
- `verb`: Type of notification
- `target_details`: Additional context about the notification
- `timestamp`: When the notification was created
- `is_read`: Read status of the notification

## Implementation Notes
- Notifications are automatically generated for likes
- Unread notifications are marked as read when viewed
- Generic content type allows flexibility for future notification types
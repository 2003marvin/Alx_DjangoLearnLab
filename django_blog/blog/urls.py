# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # auth/registration
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # comments
    path('posts/<int:post_id>/comments/new/', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/edit/', views.comment_update, name='comment_update'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),

    # tags & search
    path('search/', views.search_view, name='search'),
    path('tags/<str:tag>/', views.tagged_posts, name='tagged_posts'),
]

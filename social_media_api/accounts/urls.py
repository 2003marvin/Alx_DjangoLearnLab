from django.urls import path
from .views import FollowersListView, FollowingListView
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView,
    FollowUserView, UnfollowUserView
    
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path("followers/<int:user_id>/", FollowersListView.as_view(), name="user-followers"),
    path("following/<int:user_id>/", FollowingListView.as_view(), name="user-following"),
]

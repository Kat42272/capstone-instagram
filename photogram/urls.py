from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('profile/<str:user_name>', views.profile_view, name="profilepage"),
    path('edit/<str:user_name>', views.edit_profile_view, name="edit_profilepage"),
    path('following/<str:user_name>', views.FollowingView.as_view(), name="following_profilepage"),
    path('unfollowing/<str:user_name>', views.UnfollowingView.as_view(), name="unfollowing_profilepage"),
    path('follower/<str:user_name>', views.FollowerView.as_view(), name="follower_profilepage")
]

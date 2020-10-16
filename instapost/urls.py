from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post_view, name="addpost"),
    path('like/<int:post_id>/', views.like_view, name="like_page"),
    # path('dislikes/<int:dislikes_id>/', views.dislike_view, name="dislike_page"),
    path('deletepost/<int:post_id>', views.delete_view, name="delete_page"),
   
]
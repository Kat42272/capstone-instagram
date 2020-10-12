from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post_view, name="addpost"),
    path('likes/<int:likes_id>', views.like_view, name="like_page"),
    path('dislikes/<int:dislikes_id>', views.dislike_view, name="dislike_page"),
   
]
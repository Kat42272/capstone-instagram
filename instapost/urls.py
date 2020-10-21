from django.urls import path
from . import views


urlpatterns = [
    path('add_post/', views.add_post_view, name="addpost"),
    path('like/<int:post_id>/', views.like_view, name="like_page"),
    path('post_detail/<int:post_id>', views.post_detail_view, name="post_detail_page"),
    path('add_comment/<int:post_id>', views.add_comment_view, name="add_comment_page"),
    path('deletecomment/<int:comment_id>', views.delete_comment_view, name="delete_comment_page"),
    path('deletepost/<int:post_id>', views.delete_post_view, name="delete_page"),
    path('500/', views.handler500, name='500_page')
]

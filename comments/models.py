from django.db import models
from photogram.models import InstaProfileModel
from instapost.models import PostModel


# Create your models here.
class CommentModel(models.Model):
    post_comment = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comments")
    author_comment = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_comment")
    body = models.TextField(max_length=140)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.body

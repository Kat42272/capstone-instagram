from django.db import models
from photogram.models import InstaProfileModel
from instapost.models import PostModel


# Create your models here.
class CommentModel(models.Model):
    author_comment = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_comment")
    post_comment = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="post_comment")
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.comment

from django.db import models
from instagram.models import InstaProfileModel

# Create your models here.
class CommentModel(models.Model):
    author = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_comments")
    comments = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments

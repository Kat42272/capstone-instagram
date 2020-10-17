from django.db import models

from photogram.models import InstaProfileModel
from instapost.models import PostModel
from comments.models import CommentModel


# Create your models here.
class NotificationModel(models.Model):
    comment_notification = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
    user_notification = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE)
    new_notification = models.BooleanField(default=True)

    def __str__(self):
        return self.comment_notification.comment

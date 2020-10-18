from django.db import models
from photogram.models import InstaProfileModel
from comments.models import CommentModel


# Create your models here.
class NotificationModel(models.Model):
  user_receive = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE)
  post_receive = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
  notif_flag = models.BooleanField(default=False)
  

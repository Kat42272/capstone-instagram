from django.db import models

from photogram.models import InstaProfileModel
from instapost.models import PostModel

# Create your models here.

class NotificationModel(models.Model):
  user = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE)
  # instapost = models.ForeignKey(PostModel, on_delete=models.CASCADE)
  time_posted = models.DateTimeField(default=None, blank=True, null=True)
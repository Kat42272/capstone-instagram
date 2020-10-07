from django.db import models
from instagram.models import InstaProfileModel

class PostModel(models.Model):
    author = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_post")
    date_created = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=70, blank=True, null=True)
    picture = models.ImageField(upload_to='static/photo_upload/', blank=True, null=True, verbose_name='picture')
    # likes = models.ManyToManyField("self", related_name='likes')
    # archive = models.BooleanField(default=False)

    def __str__(self):
        return self.caption

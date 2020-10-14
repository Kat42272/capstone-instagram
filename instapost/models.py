from django.db import models
from instagram.models import InstaProfileModel


class PostModel(models.Model):
    author = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_post")
    date_created = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=70, blank=True, null=True)
    picture = models.ImageField(upload_to='static/post_upload/', blank=True, null=True, verbose_name='picture')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # likes = models.ManyToManyField("self", related_name='likes')
    # archive = models.BooleanField(default=False)

    def __str__(self):
        return self.caption


    @property
    def total_likes(self):
        return self.likes + self.dislikes

from django.db import models
from photogram.models import InstaProfileModel


class PostModel(models.Model):
    author = models.ForeignKey(InstaProfileModel, on_delete=models.CASCADE, related_name="author_post")
    date_created = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=70, blank=True, null=True)
    # post_video_image = models.FileField(upload_to='media/post_upload/', blank=True, null=True)
    picture = models.ImageField(upload_to='static/post_upload/', blank=True, null=True, verbose_name='picture')
    like = models.ManyToManyField(InstaProfileModel, related_name='like')
    liked =  models.BooleanField(default=False)
    

    def __str__(self):
        return self.caption

    @property
    def total_likes(self):
        return self.like.count()


   

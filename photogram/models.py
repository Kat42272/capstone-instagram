from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timezone


class InstaProfileModel(AbstractUser):
    displayname = models.CharField(max_length=30)
    bio = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    # following = models.ManyToManyField("self", symmetrical=False, blank=True)
    # follower = models.ManyToManyField("self", symmetrical=False)
    picture = models.ImageField(
        upload_to='static/photo_upload/',
        blank=True, null=True, verbose_name='picture')
    email = models.EmailField(max_length=254)
    follower = models.ManyToManyField("self", symmetrical=False, blank=True)

    def count_following(self):
        return self.follower.count()

    def count_follower(self):
        return InstaProfileModel.objects.filter(follower=self).count()

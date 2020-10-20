from django.db import models

from django.utils import timezone


# All models are registered with the admin interface 5.0 pts
# At least five fields of the following list are used among all models: 
# BooleanField, CharField, DateField, DatetimeField, FloatField, EmailField, TextField, URLField 5.0 pts
# Create your models here.
class PhotogramModel(models.Model):
    is_epic = models.BooleanField()
    shorter_comment = models.CharField(max_length=200)
    longer_comment = models.TextField()  # Does it need a widget ?
    datetime_posted = models.DatetimeField(default=timezone.now)
    rating = models.FloatField()  # https://www.geeksforgeeks.org/floatfield-django-models/
    user_email = models.EmailField(blank=True, default='')  # https://www.programcreek.com/python/example/51143/django.db.models.EmailField
    website = models.URLField(max_length=200)  # https://www.geeksforgeeks.org/urlfield-django-models/


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

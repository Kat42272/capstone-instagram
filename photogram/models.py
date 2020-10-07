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


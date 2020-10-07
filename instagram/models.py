from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import  datetime, timezone 


class InstaProfileModel(AbstractUser):
    displayname = models.CharField(max_length=30)
    bio = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True)
    following = models.ManyToManyField("self", symmetrical=False)
    picture = models.ImageField(upload_to='static/photo_upload/', blank=True, null=True, verbose_name='picture')

    @property
    def data_specific(self):
        date_submit = self.submit_time
        current_date = datetime.now(timezone.utc)
        age_day = current_date - date_submit
        return age_day.year



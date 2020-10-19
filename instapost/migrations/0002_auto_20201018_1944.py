<<<<<<< HEAD:instapost/migrations/0002_auto_20201018_1944.py
# Generated by Django 3.1.2 on 2020-10-18 19:44
=======
# Generated by Django 3.1.2 on 2020-10-19 03:14
>>>>>>> 69e2262960937793b3cf7ee0e134a77abde2ff5a:instapost/migrations/0002_auto_20201019_0314.py

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instapost', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='like',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]

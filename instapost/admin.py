from django.contrib import admin
from .models import PostModel

class InstaPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption')
# Register your models here.
admin.site.register(PostModel, InstaPostAdmin)

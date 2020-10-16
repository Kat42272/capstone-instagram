from django.contrib import admin
from .models import InstaProfileModel, FollowerModel


class InstaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


admin.site.register(InstaProfileModel, InstaProfileAdmin)
admin.site.register(FollowerModel)
from django.contrib import admin
from .models import InstaProfileModel


class InstaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'displayname')


admin.site.register(InstaProfileModel, InstaProfileAdmin)

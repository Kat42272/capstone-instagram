from django.contrib import admin
from .models import InstaProfileModel


class InstaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


admin.site.register(InstaProfileModel, InstaProfileAdmin)

from django.contrib import admin
from .models import InstaProfileModel


class InstaProfileAdmin(admin.ModelAdmin):
    list_display = ('picture',)


admin.site.register(InstaProfileModel, InstaProfileAdmin)

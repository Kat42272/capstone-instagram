from django.contrib import admin


# Register your models here.

from .models import InstaProfileModel


class InstaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


admin.site.register(InstaProfileModel, InstaProfileAdmin)


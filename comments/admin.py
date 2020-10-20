from django.contrib import admin

from .models import CommentModel


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')


# Register your models here.
admin.site.register(CommentModel, CommentAdmin)

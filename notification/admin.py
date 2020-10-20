from django.contrib import admin
from .models import NotificationModel
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_receive')
    
admin.site.register(NotificationModel, NotificationAdmin)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import NotificationModel

# Create your views here.

@login_required
def notification_view(request, user_id):
    notifications = NotificationModel.objects.filter(user_id=user_id)
    notification_alert = []
    for notification in notifications:
        if not notification.time_posted:
            notification_alert.append(notification.instapost)
        notification.time_posted = timezone.now()
        notification.save()

    return render(request, 'base.html', {
        'notification_alert': notification_alert[::-1]
    })
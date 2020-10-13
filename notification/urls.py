from django.urls import path
from . import views

urlpatterns = [
    path('notifications/<int:user_id>/', views.notification_view, name="notification_page"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('profile/', views.profile_view, name="profilepage"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.uptime, name='uptime'),
    path('uptime_search', views.uptime_search, name='uptime_search'),
]

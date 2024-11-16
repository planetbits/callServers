from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.trends, name='trends'),
    path('trends_search', views.trends_search, name='trends_search'),
    path('graph_static/', views.graph_static, name='graph_static'),
    path('graph_dynamic/', views.graph_dynamic, name='graph_dynamic'),
    path('get_datapoints/', views.get_datapoints, name='get_datapoints'),
]

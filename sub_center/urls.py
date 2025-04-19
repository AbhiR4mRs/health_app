# hq/urls.py
from django.urls import path
from .views import dashboard

app_name = 'subcenter'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]

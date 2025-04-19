# hq/urls.py
from django.urls import path
from .views import dashboard

app_name = 'center'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]

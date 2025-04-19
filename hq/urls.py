# hq/urls.py
from django.urls import path
from .views import dashboard, reports, add_center, upload

app_name = 'hq'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('reports/', reports, name='reports'),
    path('add_center/', add_center, name='add_center'),
    path('upload/', upload, name='upload')
]

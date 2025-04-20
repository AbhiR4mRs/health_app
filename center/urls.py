# hq/urls.py
from django.urls import path
from .views import dashboard, reports, add_sub_center

app_name = 'center'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('reports/', reports, name='report'),
    path('add_subcenter/', add_sub_center, name='add_sub'),
]

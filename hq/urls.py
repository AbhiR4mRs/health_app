# hq/urls.py
from django.urls import path
from .views import dashboard, reports, add_center, upload, delete_content, edit_content, manage_content, no_permission, add_subcenter

app_name = 'hq'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('reports/', reports, name='reports'),
    path('add_center/', add_center, name='add_center'),
    path('add_subcenter/', add_subcenter, name='add_subcenter'),
    path('upload/', upload, name='upload'),
    path('manage-content/', manage_content, name='manage_content'),
    path('delete/<int:pk>/', delete_content, name='delete_content'),
    path('edit/<int:pk>/', edit_content, name='edit_content'),
    path('no_permission/', no_permission, name='no_permission')
]

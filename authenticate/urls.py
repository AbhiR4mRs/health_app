from django.urls import path
from .views import login_view, logout_view, home, no_group_view

app_name = 'authenticate'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('no-group/', no_group_view, name='no_group'),
]


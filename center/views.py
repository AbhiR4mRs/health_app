# hq/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'center/dashboard.html')

def reports(request):
    return render(request, 'center/report.html')

def add_sub_center(request):
    return render(request, 'center/add_sub.html')
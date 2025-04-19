from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'hq/dashboard.html')

def reports(request):
    return render(request, 'hq/reports.html')

def add_center(request):
    return render(request, 'hq/add_center.html')

def upload(request):
    return render(request, 'hq/upload.html')
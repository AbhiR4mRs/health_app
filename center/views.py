# hq/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from hq.models import Center
from hq.forms import CreateCenterForm

@login_required
def dashboard(request):
    return render(request, 'center/dashboard.html')

def reports(request):
    return render(request, 'center/report.html')

def add_sub_center(request):
    if not request.user.groups.filter(name='centers').exists():
        return redirect('no_permission')

    if request.method == 'POST':
        form = CreateCenterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            center_name = form.cleaned_data['center_name']
            # Always subcenter
            is_subcenter = True

            user = User.objects.create_user(username=username, password=password)
            subcenter_group = Group.objects.get(name='subcenters')
            user.groups.add(subcenter_group)

            Center.objects.create(user=user, name=center_name, is_subcenter=is_subcenter)
            return redirect('center:dashboard')
    else:
        form = CreateCenterForm()

    return render(request, 'center/add_sub.html', {'form': form})
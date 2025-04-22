from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublicContentForm, CreateCenterForm, CreateSubcenterForm
from django.contrib.auth.models import User, Group
from .models import PublicContent, Center
from django.contrib import messages
import os

@login_required
def dashboard(request):
    return render(request, 'hq/dashboard.html')

def no_permission(request):
    return render(request, 'hq/no_permission.html')

def reports(request):
    return render(request, 'hq/reports.html')

def add_center(request):
    if not request.user.groups.filter(name='headquarters').exists():
        return redirect('no_permission')

    if request.method == 'POST':
        form = CreateCenterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            center_name = form.cleaned_data['center_name']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose another one.')
            else:
                user = User.objects.create_user(username=username, password=password)
                group = Group.objects.get(name='centers')
                user.groups.add(group)

                Center.objects.create(user=user, name=center_name, is_subcenter=False)

                return redirect('hq:dashboard')
    else:
        form = CreateCenterForm()

    return render(request, 'hq/create_center.html', {'form': form})

def add_subcenter(request):
    if not request.user.groups.filter(name='headquarters').exists():
        return redirect('no_permission')

    if request.method == 'POST':
        form = CreateSubcenterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            subcenter_name = form.cleaned_data['subcenter_name']
            parent_center = form.cleaned_data['parent_center']

            user = User.objects.create_user(username=username, password=password)

            group = Group.objects.get(name='subcenters')
            user.groups.add(group)

            Center.objects.create(
                user=user,
                name=subcenter_name,
                is_subcenter=True,
                parent_center=parent_center
            )

            return redirect('hq:dashboard')
    else:
        form = CreateSubcenterForm()
    return render(request, 'hq/create_subcenter.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        form = PublicContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hq:upload')  # or some other success page
    else:
        form = PublicContentForm()
    return render(request, 'hq/upload.html', {'form': form})

def delete_content(request, pk):
    content = get_object_or_404(PublicContent, pk=pk)
    if content.file and os.path.isfile(content.file.path):
        os.remove(content.file.path)
    content.delete()
    return redirect('hq:dashboard')

def manage_content(request):
    contents = PublicContent.objects.all().order_by('-created_at')
    return render(request, 'hq/manage_content.html', {'contents': contents})

def edit_content(request, pk):
    content = get_object_or_404(PublicContent, pk=pk)
    if request.method == 'POST':
        form = PublicContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            return redirect('hq:manage_content')
    else:
        form = PublicContentForm(instance=content)
    return render(request, 'hq/edit_content.html', {'form': form})

def dashboard(request):
    center_count = Center.objects.filter(is_subcenter=False).count()
    subcenter_count = Center.objects.filter(is_subcenter=True).count()
    return render(request, 'hq/dashboard.html', {
        'center_count': center_count,
        'subcenter_count': subcenter_count
    })
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublicContentForm, CreateCenterForm
from django.contrib.auth.models import User, Group
from .models import PublicContent, Center

@login_required
def dashboard(request):
    return render(request, 'hq/dashboard.html')

def no_permission(request):
    return render(request, 'hq/no_permission.html')

def reports(request):
    return render(request, 'hq/reports.html')

def add_center(request):
    if not request.user.groups.filter(name='headquarters').exists():
        return redirect('no_permission')  # Optional: restrict access

    if request.method == 'POST':
        form = CreateCenterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            center_name = form.cleaned_data['center_name']
            is_subcenter = form.cleaned_data['is_subcenter']

            user = User.objects.create_user(username=username, password=password)

            # Add to appropriate group
            group_name = 'subcenters' if is_subcenter else 'centers'
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            # Create Center/Subcenter
            Center.objects.create(user=user, name=center_name, is_subcenter=is_subcenter)

            return redirect('hq:dashboard')
    else:
        form = CreateCenterForm()
    return render(request, 'hq/create_center.html', {'form': form})

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
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Check user's group and redirect accordingly
                if user.groups.filter(name='headquarters').exists():
                    return redirect('hq:dashboard')  # or your hq url
                elif user.groups.filter(name='centers').exists():
                    return redirect('center:dashboard')  # or your center url
                elif user.groups.filter(name='subcenters').exists():
                    return redirect('subcenter:dashboard')  # or your subcenter url
                else:
                    return redirect('no_group')  # Optional fallback
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('authenticate:login') 
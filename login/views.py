from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    

@require_POST  # Only allow POST requests to this view
def custom_logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page
    
    
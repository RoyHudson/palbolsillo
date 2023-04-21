from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Profile

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, form.errors)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html', {'form': form})
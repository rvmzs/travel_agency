# tours/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Guide, Tour, Review
from .forms import GuideForm, TourForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    register_form = RegisterForm()
    login_form = AuthenticationForm()
    context = {
        'register_form': register_form,
        'login_form': login_form,
    }
    return render(request, 'home.html', context)

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guides/guide_list.html', {'guides': guides})

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def add_guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuideForm()
    return render(request, 'guides/add_guide.html', {'form': form})

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'tours/add_tour.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

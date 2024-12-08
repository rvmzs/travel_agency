# tours/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Tour, Guide, Review
from .forms import TourForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour/tour_list.html', {'tours': tours})

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guides/guide_list.html', {'guides': guides})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'tour/add_tour.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin, login_url='/admin/login/')
def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'tours/add_tour.html', {'form': form})


def home(request):
    register_form = RegisterForm()
    login_form = AuthenticationForm()
    context = {
        'register_form': register_form,
        'login_form': login_form,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')
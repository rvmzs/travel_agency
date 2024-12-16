# tours/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Guide, Tour, Review, Tourist, Order
from .forms import GuideForm, TourForm, RegisterForm, ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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


@login_required
def add_review(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    tourist, created = Tourist.objects.get_or_create(user=request.user, defaults={'email': request.user.email})
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.tourist = tourist
            review.save()
            return redirect('tour_list')
    else:
        form = ReviewForm()
    return render(request, 'tours/add_review.html', {'form': form, 'tour': tour})


@login_required
def order_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user, tour=tour, status='Booked')
        return redirect('order_success')
    return render(request, 'tours/order_tour.html', {'tour': tour})

def order_success(request):
    return render(request, 'tours/order_success.html')

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'users/user_orders.html', {'orders': orders})

####################################################

@login_required
def edit_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm(instance=tour)
    return render(request, 'tours/edit_tour.html', {'form': form, 'tour': tour})

@login_required
def delete_tour(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    if request.method == 'POST':
        tour.delete()
        return redirect('tour_list')
    return render(request, 'tours/delete_tour.html', {'tour': tour})

@login_required
def edit_guide(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    if request.method == 'POST':
        form = GuideForm(request.POST, instance=guide)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuideForm(instance=guide)
    return render(request, 'guides/edit_guide.html', {'form': form, 'guide': guide})

@login_required
def delete_guide(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    if request.method == 'POST':
        guide.delete()
        return redirect('guide_list')
    return render(request, 'guides/delete_guide.html', {'guide': guide})
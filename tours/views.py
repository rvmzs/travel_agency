# tours/views.py
from django.shortcuts import render, redirect
from .models import Tour, Guide, Review
from .forms import TourForm

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
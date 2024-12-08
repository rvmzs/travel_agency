# tours/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_list, name='tour_list'),
    path('guides/', views.guide_list, name='guide_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('add_tour/', views.add_tour, name='add_tour'),
]

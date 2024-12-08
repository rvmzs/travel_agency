# tours/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('guides/', views.guide_list, name='guide_list'),
    path('tours/', views.tour_list, name='tour_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('add_tour/', views.add_tour, name='add_tour'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# tours/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guides/', views.guide_list, name='guide_list'),
    path('tours/', views.tour_list, name='tour_list'),
    path('reviews/', views.review_list, name='review_list'),
    path('add_tour/', views.add_tour, name='add_tour'),
    path('add_guide/', views.add_guide, name='add_guide'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
]

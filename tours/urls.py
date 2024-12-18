# # tours/urls.py
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
    path('tours/<int:tour_id>/add_review/', views.add_review, name='add_review'),
    path('tours/<int:tour_id>/order/', views.order_tour, name='order_tour'),
    path('order_success/', views.order_success, name='order_success'),
    path('user_orders/', views.user_orders, name='user_orders'),
    path('tours/<int:tour_id>/edit/', views.edit_tour, name='edit_tour'),
    path('tours/<int:tour_id>/delete/', views.delete_tour, name='delete_tour'),
    path('guides/<int:guide_id>/edit/', views.edit_guide, name='edit_guide'),
    path('guides/<int:guide_id>/delete/', views.delete_guide, name='delete_guide'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),  
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('users/edit_profile/', views.edit_profile, name='edit_profile'),
]


# travel_agency/urls.py
from django.contrib import admin
from django.urls import path, include
from tours import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tours/', include('tours.urls')),
]





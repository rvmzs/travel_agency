from django.contrib import admin
from .models import Tourist, Tour, Guide, TourGuide, Order, Review

admin.site.register(Tourist)
admin.site.register(Tour)
admin.site.register(Guide)
admin.site.register(TourGuide)
admin.site.register(Order)
admin.site.register(Review)
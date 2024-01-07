from django.contrib import admin
from .models import Hotel, HotelImage, Amenities


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'start_date', 'end_date']


@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Amenities)
class AmenetiesAdmin(admin.ModelAdmin):
    list_display = ['title']
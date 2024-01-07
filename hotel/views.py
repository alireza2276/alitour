from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hotel, HotelImage




class HotelList(ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hotels'


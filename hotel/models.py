from django.db import models
from django.utils import timezone



class Amenities(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title}"


class Hotel(models.Model):
    amenities = models.ManyToManyField(Amenities, related_name='hotels')
    title = models.CharField(max_length=255)
    short_decription = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveBigIntegerField(default=0)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)



    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.title}"

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='static/hotel-images')


    def __str__(self) -> str:
        return f"{self.title}"
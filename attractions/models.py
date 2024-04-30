from django.db import models

class Attraction(models.Model):
    
    name = models.CharField(max_length=50)
    entry_fee = models.IntegerField(default=0)
    opening_hours = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    accessibility = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    opening_hours = models.CharField(max_length=100)
    has_alcohol = models.BooleanField(default=False)
    price_range = models.CharField(max_length=10)
    Atmosphere = models.CharField(max_length=100)
    parking = models.BooleanField(default=False)
    reservation = models.CharField(max_length=50)
    accessibility = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    starting_price = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    amenities = models.CharField(max_length=200)
    services = models.CharField(max_length=200)
    dining_options = models.CharField(max_length=200)
    pet_policy = models.CharField(max_length=200)

    def __str__(self):
        return self.name






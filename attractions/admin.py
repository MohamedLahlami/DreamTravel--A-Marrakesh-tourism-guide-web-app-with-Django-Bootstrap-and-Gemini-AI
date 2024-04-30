from django.contrib import admin

from .models import Attraction, Restaurant, Hotel

admin.site.register(Attraction)
admin.site.register(Restaurant)
admin.site.register(Hotel)
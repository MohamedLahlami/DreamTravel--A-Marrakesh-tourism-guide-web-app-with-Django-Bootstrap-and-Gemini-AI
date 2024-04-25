from django.db import models

class Destination(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

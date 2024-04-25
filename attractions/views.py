from django.shortcuts import render #unused so far
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in attractions app")

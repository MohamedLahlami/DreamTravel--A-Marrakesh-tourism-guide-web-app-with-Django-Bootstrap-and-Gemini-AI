from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.template import loader
from attractions.models import *
import google.generativeai as genai
import os
import markdown

#gemini configuration
os.environ['GOOGLE_API_KEY'] = "AIzaSyD44p4MRPNGzYFtAfjwh1jWbVC21UhcbMY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

def temp(request):
    return render(request, 'temp.html')

def index(request):
    return render(request, 'indextemp.html')  ##################

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')
    else:
        return redirect('index')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have been Successfully Registered!")
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

def attractions(request):
    attractions = Attraction.objects.all()
    for attraction in attractions:
        attraction.imagePath = 'img/' + attraction.name + '.jpg'
    return render(request, 'attractions.html', {"attractions":attractions})

def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants.html', {"restaurants":restaurants})

def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {"hotels":hotels})

def attractionDetail(request, id):
    return render(request, 'attractionDetail.html', {})

def hotelDetail(request, id):
    return render(request, 'hotelDetail.html', {})


def restaurantDetail(request, id):
    return render(request, 'restaurantDetail.html', {})


def chatbot(request, query = None):
    if query is None:
        return redirect('index')
    if request.user.is_authenticated:
        response_text = markdown.markdown(model.generate_content(query).text)
        response_json = JsonResponse({'name': 'AI','response_data': response_text}, status=200, safe=False)
        return response_json
    else:
        return redirect('login')
    


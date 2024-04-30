from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.template import loader
import google.generativeai as genai
import os
import markdown

#gemini configuration
os.environ['GOOGLE_API_KEY'] = "AIzaSyD44p4MRPNGzYFtAfjwh1jWbVC21UhcbMY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')



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

def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

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
    return render(request, 'register.html', {'form':form})



def chatbot(request, query):
    if request.user.is_authenticated:
        response_text = markdown.markdown(model.generate_content(query).text)
        response_json = JsonResponse({'name': 'AI','response_data': response_text}, status=200, safe=False)
        return response_json
    else:
        return redirect('login')
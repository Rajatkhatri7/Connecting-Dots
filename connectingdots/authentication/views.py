from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'authentication/home.html')

def signup(request):
    return render(request, 'authentication/signup.html')


def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return render(request, 'authentication/logout.html')

def profile(request):
    return render(request, 'authentication/profile.html')

def files(request):
    return render(request, 'authentication/files.html')
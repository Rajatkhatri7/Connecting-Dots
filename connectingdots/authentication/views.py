from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def home(request):
    return render(request, 'authentication/home.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(firstname=firstname, lastname=lastname,username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password do not match') 
            return redirect('signup')

    return render(request, 'authentication/signup.html')


def login(request):
    return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

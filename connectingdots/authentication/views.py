from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm 


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
                    model = User.objects.create_user(first_name=firstname, last_name=lastname,username=username, email=email, password=password)
                    commit = True
                    if commit:

                        model.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password do not match') 
            return redirect('signup')

    return render(request, 'authentication/signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request = request,user = user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('home')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('login')
            
    
    messages.warning(request,'something went wrong')

    return render(request,'authentication/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')


from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request = request, user=user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("login_request")
                
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="authentication/login_request.html", context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login_request")

        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="authentication/register.html", context={"register_form": form})

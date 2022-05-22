from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required

import smtplib
import subprocess
import os
import ast
import json
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

# Create your views here.

def home(request):
    return render(request, 'authentication/home.html')
def about(request):
    return render(request, 'authentication/aboutus.html')

def contact(request):

    if request.method == 'POST':

    
        req_name = request.POST.get('firstname')
        req_number = request.POST.get('number')
        req_subject = request.POST.get('subject')
        req_mail= request.POST.get('email')
        
        req_message = request.POST.get('message')


        print(req_mail)
    
        result_list = []
    
        emailMsg = "Name: " + req_name + "\n" + "Number: " + req_number + "\n" + "Subject: " + req_subject + "\n" + "Email: " + req_mail + "\n" + "Message: " + req_message + "\n"
    
            
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = "rajatkhatri0002@gmaiil.com"
        mimeMessage['from'] = "rajat@sentient.io"
        mimeMessage['subject'] = req_subject
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    
        username = "rajat@sentient.io"
        password = "foxfylfhdbpkqeud"
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail("rajat@sentient.io", "rajatkhatri0002@gmail.com", mimeMessage.as_string())  
        server.quit()

        messages.success(request, 'Email sent successfully')
        return redirect('contact')

    
    




    return render(request, 'authentication/contact.html')

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
            

    return render(request,'authentication/login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')



def forget_password(request):
    if request=="POST":
        username = request.POST['username']
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            if User.objects.filter(username=username).exists():
                if User.objects.filter(username=username, password=old_password).exists():
                    user = User.objects.get(username=username)
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, 'Password changed successfully')
                    return redirect('login')
                else:
                    messages.warning(request, 'Old password is incorrect')
                    return redirect('forget_password')

            else:
                messages.warning(request, 'Username does not exist')
                return redirect('forget_password')

    return render(request, 'authentication/forget_password.html')








@login_required(login_url='login')
def dashboard(request):
    return render(request, 'authentication/dashboard.html')





#testing authentication
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

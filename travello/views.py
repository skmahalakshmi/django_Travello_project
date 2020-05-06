
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def logout(request):
    auth.logout(request)
    return redirect('/')
def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credintials")
            return redirect('login')




    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:


                user=User.objects.create_user(first_name=first_name,password=password1,email=email,last_name=last_name,username=username)
                user.save();
                print("usercreated")
                return redirect('login')
        else:
            messages.info(request,"u r passwords are not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')









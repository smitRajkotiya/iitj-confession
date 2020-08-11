from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import conf
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method== 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,email=email)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Alredy exist please try another user name')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'acount on this email alredy exist')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save();
                print('acount created')
                return redirect('login')

        else:
            messages.info(request, 'password and confirm password not matching ')    
            return redirect('register')

        return redirect('/')
        
    else:
        return render(request, 'signup.html')


def postpage(request):
    return render(request, 'postpage.html')


def creatpost(request):
    if request.method == 'POST':
        imeage = request.POST['img']
        descreption =request.POST['desc']

        if user.is_authenticated:
            Confession=conf(img=imeage, desc=decreption,email=user.email)
            Confession.save();
            messages,info(request,'confession has been saved')
        else:
            messages.info(request, 'Please login for confession')
    else:
        return render(request, 'creatpostpage.html')

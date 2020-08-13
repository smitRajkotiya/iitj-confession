from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import conf
# Create your views here.


def home(request):
    return render(request, 'home.html')


def contactus(request):
    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def postpage(request):
    confession=conf.objects.all()

    return render(request, 'postpage.html', confession)

def profilepage(request):
    
    confession=conf.objects.filter(email=request.user.email)

    return render(request, 'profilepage.html', confession)

def creatpost(request):
    if request.method == 'POST':
        imeage = request.POST['img']
        descreption =request.POST['desc']

        if request.user.is_authenticated:
            Confession=conf(img=imeage, desc=descreption,email=request.user.email)
            Confession.save();
            print("confession reated")
            messages.info(request,'confession has been saved')
            return redirect('/')
        else:
            messages.info(request, 'Please login for confession')
            return redirect('creatpost')
    else:
        return render(request, 'creatpost.html')

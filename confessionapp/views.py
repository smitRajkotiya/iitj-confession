from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import conf
# Create your views here.


def home(request):
    return render(request, 'home.html')





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

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import conf
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return render(request, 'home.html')


def contactus(request):
    return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def postpage(request):
    confession=conf.objects.all()
    data= {'confession':confession}

    return render(request, 'postpage.html', data)

def profilepage(request):
    
    confession=conf.objects.filter(email=request.user.email)
    noofconfession=conf.objects.filter(email=request.user.email).count()
    print(noofconfession)

    data= {'confession':confession,'noofconfession':noofconfession}


    return render(request, 'profilepage.html', data)

def creatpost(request):
    if request.method == 'POST':
        descreption =request.POST['desc']
        image=request.FILES['image']
        fs=FileSystemStorage()
        fs.save(image.name,image)
        if request.user.is_authenticated:
            Confession=conf(image=image, desc=descreption,email=request.user.email)
            Confession.save();
            print("confession reated")
            return redirect('/')
        else:
            messages.info(request, 'Please login for confession')
            return redirect('creatpost')
    else:
        return render(request, 'creatpost.html')

from contextlib import redirect_stderr
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from gnewsclient import gnewsclient

# Create your views here.
def home(request):
    name="Big Bull"
    content={'name':name}
    return render(request,"base\home1.html",content)

def dashboard(request):
    return render(request,"base\dashboard.html")

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=name).exists():
            messages.info(request,"username taken")
            return render(request,"base\index.html")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email alredy exist")
            return render(request,"base\index.html")
        else:
            user=User.objects.create_user(username=name,password=password,email=email)
            user.save()
            print("user created")
            messages.info(request,"Thank You For Registration ❤️")
            return render(request,"base\index.html")
    else:
        return render(request,"base\index.html")

def login(request):
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        print(name)
        print(password)
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            print("login sucess")
            return redirect('dashboard')
        else:
            messages.info(request,"credentials invalid")
            print("credentials invalid")
            return render(request,"base\index.html")
    else:
        return render(request,"base\index.html")


def logout(request):
    auth.logout(request)
    return render(request,'base\home1.html')

def header(request):
    return render(request,'header.html')

def snews(request):
    client = client = gnewsclient.NewsClient(language='english', location='india', topic='Buisness', use_opengraph=True, max_results=25)
    news_list = client.get_news()
    content={'news_list':news_list}
    return render(request,"base\snews.html",content)
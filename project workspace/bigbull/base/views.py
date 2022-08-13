from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    name="Big Bull"
    content={'name':name}
    return render(request,"base\home1.html",content)

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,password=password,email=email)
        user.save()
        print("user created")
        return render(request,"base\dashboard.html")
    else:
        return render(request,"base\index.html")

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import UserRegistrationForm
from .models import User

# Create your views here.

def welcome(request:HttpRequest):
    content = "Se ha registrado con exito.BIENVENIDO"
    return HttpResponse(content=content)

def register_user(request:HttpRequest):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = UserRegistrationForm()
    
    return render(request,'blog/registration.html',{'form':form})


from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import UserRegistrationForm
from .models import User

# Create your views here.
def home(request:HttpRequest) -> HttpResponse:
    response = 'Home blog application'
    return HttpResponse(response)

def welcome(request:HttpRequest):
    content = "Se ha registrado con exito.BIENVENIDO"
    return HttpResponse(content=content)

def register_user(request:HttpRequest):
    '''Algorithm User register view:
1- Instantiate the model form with the received data.
2- Validate the received data.
3- Extract the username from the form.
4- Filter if the username from the form exists in the database.
5- If it doesn't exist, save it and redirect to welcome. If it does, return
   an empty form with a message indicating that the user already exists.'''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            user_exists = User.objects.filter(username=user).exists()
            if not user_exists:
                form.save()
                return redirect('welcome')
    else:
        form = UserRegistrationForm()
    return render(request,'blog/registration.html',{'form':form})


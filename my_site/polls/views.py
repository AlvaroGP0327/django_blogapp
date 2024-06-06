from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    headers = request.headers
    user_agent = headers.get('User-Agent')
    return HttpResponse(user_agent)

def index(request):
    mensaje_flash = request.session.pop('mensaje_flash',None)
    return render(request,'polls/index.html',{'mensaje_flash':mensaje_flash})

def parametros_url(request,nombre,edad):
    param1 = nombre
    param2 = edad
    return HttpResponse(f'{param1}.....{param2}')

def plantilla(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render())

def formulario(request: HttpRequest) -> HttpResponse:
    #los datos al formulario se pasan en forma de diccionario.
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        request.session['mensaje_flash'] = 'Esto es un mensaje desde flash'
        if form.is_valid():
            return redirect('index')
        else:
            messages.error(request,'Formulario no valido')
    return render(request,'polls/login.html',{'form':form})

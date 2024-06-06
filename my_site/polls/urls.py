from django.urls import path
from . import views

urlpatterns = [path('home', views.home, name='home'),
               path('', views.index, name='index'),
               path('parametros/<str:nombre>/<int:edad>', views.parametros_url, name='parametros'),
               path('plantilla', views.plantilla, name='plantilla'),
               path('formulario', views.formulario, name='formulario'),]
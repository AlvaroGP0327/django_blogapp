from django.urls import path
from . import views

urlpatterns = [ path('', views.home, name='home'),
                path('welcome', views.welcome, name='welcome'),
               path('register', views.register_user, name='register_user'),
               ]
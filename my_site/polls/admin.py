from django.contrib import admin
from .models import Question, Choice
# Register your models here.
#Registrar aqui los modelos para que puedan
#ser accedidos desde el panel de administracion
#de Django.
admin.site.register(Question)
admin.site.register(Choice)
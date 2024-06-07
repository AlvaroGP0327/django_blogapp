from django.contrib import admin
from .models import Role, User
# Register your models here.
#Registrar aqui los modelos para que puedan
#ser accedidos desde el panel de administracion
#de Django.
admin.site.register(Role)
admin.site.register(User)

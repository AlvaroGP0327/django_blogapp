Apuntes para el desarrollo web en Django.
Sintaxis basica motor plantillas:
    *{{ variables }}
    *{{% etiquetas %}}
    *{{% for %}} {{% endfor %}}
    *{{% if %}} {{% endif %}}
    *{{% else %}}
    *{{% extends "otra_plantilla" %}}: establecer estructura base desde otra plantilla.
    *{{% block %}} {{% endblock %}}
    *{{% include "nombre_plantilla" %}}: incluir contenido de otra plantilla(componentes reutilizables)
    *{{% load static %}}
        <img src="{% static 'ruta' %}" alt="Logo">

Funciona bajo el patron MVT
Modelo: representar por medio de la clases formularios,
tablas, objetos y operaciones CRUD.
Vista: funciones que reciben las solicitudes HTTP, procesan
y retornan resultados, e implementan las plantillas HTML.
Templates: recibe los resultados y se encarga de la logica de presentacion. 

    1- Todas las vistas reciben como parametro (request), que es una
    instancia de la clase HttpRequest que representa la solicitud
    HTTP hecha por el cliente. Este objeto contiene toda la informacion
    sobre la solicitud, como los datos del formulario, archivos cargados,
    cookies, headers, tokens, etc.
    Realizar una anotacion de tipo para cada vista:
        def vista(request:HttpRequest) -> HttpResponse:
            pass
    2- Este objeto es creado por el servidor web y pasa la solicitud a traves
    de una serie de middlewares de Django.
    3- Django utiliza urls.py para realizar el enrutamiento.

Objeto Request
El objeto HttpRequest contiene muchos atributos útiles, entre ellos:
request.GET: Un diccionario de todos los parámetros de consulta en la URL.
request.POST: Un diccionario de todos los datos enviados en una solicitud POST.
request.FILES: Un diccionario de todos los archivos cargados.
request.COOKIES: Un diccionario de todas las cookies.
request.session: Un diccionario que permite almacenar y recuperar datos persistentes entre solicitudes de un usuario específico.
request.user: El usuario que realiza la solicitud (si está autenticado).
request.META: Un diccionario de todas las cabeceras HTTP enviadas con la solicitud

Objeto Response
Representa la respuesta que se le envia al cliente, se usa para retornar contenido
HTML,texto plano,JSON,archivos y otro tipo de datos. Se implementa creando una instancia
de la clase HttpResponse y pasarle el contenido que se le quiere enviar al cliente.

HttpResponse ofrece varios atributos y métodos útiles:
content: El contenido de la respuesta.
status_code: El código de estado HTTP (por defecto, 200).
['header-name']: Puedes establecer cabeceras HTTP como si fueran claves de un diccionario.

Django proporciona varias subclases de HttpResponse para situaciones comunes:
JsonResponse: Para devolver datos JSON.
HttpResponseRedirect: Para redireccionar a otra URL.
HttpResponseNotFound: Para devolver una respuesta 404 Not Found.
HttpResponsePermanentRedirect: Para redirecciones permanentes (código de estado 301).
HttpResponseForbidden: Para devolver una respuesta 403 Forbidden.
render(): se comporta como un HttpResponse que encapsula la logica de creacion de la respuesta.
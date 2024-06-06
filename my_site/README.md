Apuntes para el desarrollo web en Django.
Sintaxis basica motor plantillas:
    *{{ variables }}
    *{{% etiquetas %}}
    *{{% for %}}
    *{{% if %}}
    *{{% else %}}
    *{{% endif %}}
    *{{% extends "otra_plantilla" %}}: establecer estructura base desde otra plantilla.
    *{{% block %}}
    *{{% endblock %}}
    *{{% include "nombre_plantilla" %}}: incluir contenido de otra plantilla(componentes reutilizables)
    *{{% load static %}}
        <img src="{% static 'ruta' %}" alt="Logo">

Funciona bajo el patron MVT
Modelo: representar por medio de la clases formularios,
tablas, objetos y operaciones CRUD.
Vista: funciones que reciben las solicitudes HTTP, procesan
y retornan resultados, e implementan las plantillas HTML.
Templates: recibe los resultados y se encarga de la logica de presentacion. 
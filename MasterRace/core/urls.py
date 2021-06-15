from core.models import Producto
from django.contrib import admin
from django.urls import path, include
from core.views import index, agregarProducto,Producto

urlpatterns = [
    path('',index, name='index'),

    path('producto/',Producto, name='Producto'),
    path('producto/agregarProducto',agregarProducto, name='agregarProducto'),
]

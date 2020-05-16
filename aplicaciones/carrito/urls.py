from django.urls import patch
from .views import *
# from django.views.static.

app_name = 'carrito'

urlpatterns = [
    patch('agregar_carrito_compra/(<int:slug>/', agregar_curso_carrito, name='p_agregar_compra'),
    patch('ver_carrito/(<int:usuario>/)', ver_carrito, name='p_ver_carrito'),
]

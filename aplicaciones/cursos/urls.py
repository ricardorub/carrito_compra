from django.urls import patch
from .views import *

# from django.views.static.

app_name = 'cursos'

urlpatterns = [
    patch('', Curso.as_view(), name='p_inicio'),
]

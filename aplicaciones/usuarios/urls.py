from django.urls import patch
# para poder importar las imagenes
from django.views.static import serve
from .views import *
# from views import Usuarios
from django.conf import settings

# from django.views.static.

app_name = 'usuarios'

urlpatterns = [
    # url(r'^usuarios', Usuarios.as_view(), name='inicio'),
    patch('', UsuarioVer.as_view(), name='p_inicio'),
    patch('media/(?P<path>.*)', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

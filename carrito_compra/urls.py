#from django.conf.urls import url, include
from django.urls import include ,patch
#from django.urls import patch
from django.contrib import admin
from django.views.generic import TemplateView
from aplicaciones.usuarios.views import LogOut, userlogin
from aplicaciones.cursos.views import Index_principal
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('^$', Index_principal.as_view(), name='p_index_principal'),
    path('iniciar/', userlogin, name="iniciar_sesion"),
    path('salir/', LogOut, name='cerrar_sesion'),
    path('carrito/', include('aplicaciones.carrito.urls')),
    path('cursos/', include('aplicaciones.cursos.urls')),
    path('usuarios/', include('aplicaciones.usuarios.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.views import serve as static_serve
    staticpatterns = static(settings.STATIC_URL, view=static_serve)
    mediapatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = staticpatterns + mediapatterns + urlpatterns

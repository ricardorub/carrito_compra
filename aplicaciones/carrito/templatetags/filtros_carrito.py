from django import template
from aplicaciones.carrito.middleware import get_username
from aplicaciones.cursos.models import Curso
from aplicaciones.usuarios.models import Usuario
from aplicaciones.carrito.models import Carrito_compra
from django.shortcuts import get_object_or_404
register = template.Library()


@register.filter(name='si_agrego_curso_carrito')
def has_agrego_curso(curso):
    try:
        # con middleware capturamos al usaurio
        mi_usuario = get_username()
        if curso is None or not mi_usuario.user.is_authenticated:
            return False
        else:
            mi_curso = get_object_or_404(Curso, nombre=curso)
            user = get_object_or_404(Usuario, usuario=mi_usuario.user)
            # determinamos si un usuario se ha inscrito en un curso
            estado = Carrito_compra.objects.filter(
                usuario=user, cursos=mi_curso).exists()
            return estado
    except Exception as e:
        raise e


@register.filter(name='cursos_carrito')
def has_cursos_carrito(user):
    try:
        # con middleware capturamos al usaurio
        cursos = Carrito_compra.objects.filter(usuario=user)
        return cursos
    except Exception as e:
        raise e


@register.filter(name='cantidad_cursos_carrito')
def has_cantidad_cursos_carrito(user):
    try:
        # Cantidad de cursos
        curso = get_object_or_404(Carrito_compra, usuario=user)
        cantidad = curso.cursos.all().count()
        return cantidad
    except Exception as e:
        raise e

@register.filter(name='costo_total_cursos')
def has_costo_total(user):
    try:
        curso = get_object_or_404(Carrito_compra, usuario=user)
        total = sum([p.costo for p in curso.cursos.all()])
        return total
    except Exception as e:
        raise e

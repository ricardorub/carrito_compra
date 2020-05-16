from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Carrito_compra
from django.contrib.auth.decorators import login_required
from aplicaciones.cursos.models import Curso
from aplicaciones.usuarios.models import Usuario
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.


@login_required
def agregar_curso_carrito(request, slug):
    try:
        consulta = get_object_or_404(Curso, slug=slug)
        p, created = Carrito_compra.objects.get_or_create(
            usuario=request.user)
        p.cursos.add(consulta)
        p.save()
        # consulta.
        curso = Curso.objects.filter(estado=True)
        return HttpResponseRedirect('/')
    except Exception as e:
        raise e

@login_required
def ver_carrito(request, usuario):
	try:
		user = get_object_or_404(Usuario, usuario = usuario)
		curso = get_object_or_404(Carrito_compra, usuario=user)
		mis_cursos = curso.cursos.all()
		return render(request, 'carrito/ver_carrito.html', { 'cursos': mis_cursos })
	except Exception as e:
		raise e

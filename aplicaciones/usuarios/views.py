from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from django.views.generic import ListView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import *
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .functions import LogIn

# settings y password para controlar autenticacion con redes sociales


class Index_principal(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index_principal,
                        self).get_context_data(**kwargs)
        # context['inscripcion_usuario'] = UsuarioForm()
        context['cursos'] = Curso.objects.filter(
            estado=True).order_by('-fecha_creacion')[:3]
        context['eventos'] = Evento.objects.filter(
            estado=True).order_by('-fecha_creacion')[:1]

        context['1er_testimonio'] = Testimonio.objects.filter(
            estado=True, es_principal=True).first()

        context['testimonios'] = Testimonio.objects.exclude(
            es_principal= True).order_by('-fecha_publicacion')[:10]
        # pasamos un conjunto de numeros en un rango
        context['cantidad_testimonio'] = range(1,context['testimonios'].count())
        
        return context


def userlogin(request):
    next = request.GET.get('next', '/')
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(usuario=usuario, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("usuario inactivo.")
        else:
            messages.error(
            request, 'Correo o contraseña no son correctos..!', extra_tags='danger')
            # return HttpResponseRedirect('/iniciar/')
            return render(request, "usuarios/login.html", {'redirect_to': next})
    return render(request, "usuarios/login.html", {'redirect_to': next})


def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/')

class UsuarioVer(LoginRequiredMixin, ListView):
    context_object_name = 'usuarios'
    template_name = 'usuarios/index.html'
    queryset = Usuario.objects.all()


class Registrarse(CreateView):
    form_class = UsuarioForm
    template_name = 'registrarse.html'
    success_url = reverse_lazy('completar_registro_perfil_usuario')
    user_register = UsuarioForm

    def form_valid(self, form):
        form.instance.set_password(self.request.POST['password'])
        # forzamos el guardado de datos para poder asignar al grupo
        self.object = form.save()
        grupo = get_object_or_404(Group, name__icontains='emprendedor')
        # agregamos al grupo establecido por el REGISTRADOR
        form.instance.groups.add(grupo)
        # redireccionamos al final, OJO: no estamos usando SUPER
        # generamos su perfil de Usuario
        # Perfil_usuario.objects.create(usuario=self.object)

        user = authenticate(usuario=self.request.POST[
                            'usuario'], password=self.request.POST['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
                # perfil = Perfil_usuario_form()
                # return render(request, 'completar_registro_usuario.html',
                #               {'datos_perfil': perfil, 'usuario': insert.pk})
            else:
                return HttpResponse("usuario inactivo.")
        else:
            return HttpResponseRedirect('iniciar/')
        return HttpResponseRedirect(self.get_success_url())



class Cuenta_usuario(LoginRequiredMixin, TemplateView):
    """docstring for Ver_perfil"""
    template_name = 'usuarios/perfil/cuenta.html'

    def get_context_data(self, **kwargs):
        context = super(Cuenta_usuario,self).get_context_data(**kwargs)
        context['form'] = UsuarioForm()
        context['form_password'] = PasswordChangeForm(self.request.user)
        return context


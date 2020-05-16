# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms


class CustomUserCreationForm(UserCreationForm):

    def __unicode__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Usuario
        fields = ("usuario",)


class CustomUserChangeForm(UserChangeForm):

    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __unicode__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['usuario']

    class Meta:
        model = Usuario
        fields = ("usuario",)
        exclude = ()


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        exclude = ('date_joined', 'is_staff',
                   'is_active', 'is_superuser')
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control',
                                              'pattern': '[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚüÜ]{2,35}',
                                              'title': "No es un formato válido, revise por favor..!"}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'date_joined': forms.TextInput(attrs={'class': 'form-control'}),
        }
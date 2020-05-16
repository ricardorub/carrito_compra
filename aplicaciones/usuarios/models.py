from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

class CustomUserManager(BaseUserManager):

    # aqui falta agregar correo en caso de registrar correo por redes sociales
    # de momento solo estara disponible con usuario
    def _create_user(self, usuario, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        # email = self.normalize_email(username)
        now = timezone.now()
        if not usuario:
            raise ValueError('The given email must be set')
        email = self.normalize_email(usuario)
        user = self.model(usuario=usuario,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # # creando perfil de usuario
        # grupo = get_object_or_404(Group, name__icontains='emprendedor')
        # user.groups.add(grupo)
        # Perfil_usuario.objects.create(usuario=user)
        return user

    def create_user(self, usuario, password=None, **extra_fields):
        return self._create_user(usuario, password, False, False,
                                 **extra_fields)

    def create_superuser(self, usuario, password, **extra_fields):
        return self._create_user(usuario, password, True, True,
                                 **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):

    usuario = models.CharField(_('Usuario'), max_length=60, unique=True)
    email = models.EmailField(null=True, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = CustomUserManager()
    # cuidado solo el inicio de sesion esta configurado con correo:
    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Usuarios')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.usuario)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.usuario)
        return (full_name.strip()) or u''

    def get_short_name(self):
        "Returns the short name for the user."
        return (self.usuario) or u''

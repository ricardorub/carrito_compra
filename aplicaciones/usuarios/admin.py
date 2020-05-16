from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Usuario
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('usuario', 'password')}),
        (_('Personal info'), {
         'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'email', 'password1', 'password2')}
         ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('usuario', 'email', 'is_staff', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('usuario','email')
    ordering = ('usuario',)


admin.site.register(Usuario, CustomUserAdmin)

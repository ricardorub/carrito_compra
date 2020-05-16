from django.contrib import admin

# Register your models here.
from .models import Curso, Categoria

admin.site.register(Categoria)


@admin.register(Curso)
class Curso_admin(admin.ModelAdmin):

    list_display = ('nombre', 'resumen', 'fecha_creacion',
                    'get_categorias', 'costo', 'estado')
    search_fields = ('nombre', 'resumen')
    filter_horizontal = ('categorias',)
    list_editable = ('estado',)

    def get_categorias(self, instance):
    	# p.titulo se refiere a la Categoria
        return ", ".join([p.titulo for p in instance.categorias.all()])
    get_categorias.short_description = 'Categorias'

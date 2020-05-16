from .models import Carrito_compra
from django.contrib import admin
# Register your models here.
# from .models import Carrito


@admin.register(Carrito_compra)
class Carrito_admin(admin.ModelAdmin):

    list_display = ('usuario', 'get_cursos', 'fecha_compra','get_precio_total', 'estado')
    search_fields = ('usuario__usuario','cursos__nombre')
    filter_horizontal = ('cursos',)

    def get_cursos(self, instance):
        return ", ".join([p.nombre for p in instance.cursos.all()])
    get_cursos.short_description = 'Cursos'

    # calculando el costo de los curso agregados al carrito de compras
    def get_precio_total(self, instance):
        return sum([p.costo for p in instance.cursos.all()])
    get_precio_total.short_description = 'Precio total Compra'

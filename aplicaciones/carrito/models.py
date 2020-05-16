from django.db import models
from aplicaciones.usuarios.models import Usuario
from aplicaciones.cursos.models import Curso
# Create your models here.


class Carrito_compra(models.Model):
    """docstring for Carrito"""
    usuario = models.OneToOneField(Usuario, primary_key=True,on_delete=models.DO_NOTHING)
    cursos = models.ManyToManyField(Curso, blank=True)
    fecha_compra = models.DateTimeField(auto_now=True)  
    estado = models.BooleanField(default=True)

    def __str__(self):
    	return str(self.usuario)

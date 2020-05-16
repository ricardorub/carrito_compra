from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Categoria(models.Model):

    titulo = models.CharField(max_length=150)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Curso(models.Model):
    """docstring for Curso"""
    nombre = models.CharField(max_length=250)
    slug = models.SlugField(editable=False, max_length=150, unique=True)
    resumen = models.TextField(max_length=250, null=True)
    portada = models.ImageField(
        upload_to='baners_cursos', null=True)
    duracion = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField(Categoria)
    estado = models.BooleanField(default=True)
    es_gratis = models.BooleanField(default=False)
    costo = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    descuento = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Curso, self).save(*args, **kwargs)

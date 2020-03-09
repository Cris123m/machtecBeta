from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    photo = models.ImageField(verbose_name="Foto",upload_to="products",null=True,blank=True,default="/static/core/images/gallery-image-1-1200x800-original.jpg")
    price = models.DecimalField(verbose_name="Precio",max_digits=6,decimal_places=2,blank=False)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def time(self):
        tiempo = (self.id-1)*0.15
        return ('{:,.2f}'.format(tiempo))

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['order', 'updated']

    def __str__(self):
        return self.title
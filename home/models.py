from django.db import models

# Create your models here.
class Categoria(models.Model):
    Nombre = models.CharField(max_length = 100)
    Descripcion = models.TextField(max_length = 500)

    def __str__ (self):
        return self.Nombre

class Pedido(models.Model):
    Nombre = models.CharField(max_length = 100)
    Fecha_Entrada = models.DateField()
    categoria = models.ForeignKey(Categoria, models.PROTECT)
    Cantidad = models.IntegerField()

    def __str__ (self):
        return self.Nombre

class DatosProducto(models.Model):
    Nombre = models.CharField(max_length = 100)
    Talla = models.CharField(max_length = 6)
    Descripcion = models.CharField(max_length = 200)
    categoria = models.ForeignKey(Categoria, models.PROTECT)
    pedido = models.OneToOneField(Pedido, models.PROTECT)
    
    def __str__ (self): 
        return self.Nombre

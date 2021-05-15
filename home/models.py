from django.db import models

# Create your models here.
class Tela(models.Model):
    Nombre = models.CharField(max_length = 100)
    Descripcion = models.TextField(max_length = 500)

    def __str__ (self):
        return self.Nombre

class Camisa(models.Model):
    Nombre = models.CharField(max_length = 100)
    Fecha_Entrada = models.DateField()
    Tela = models.ForeignKey(Tela, models.PROTECT)
    Cantidad = models.IntegerField()

    def __str__ (self):
        return self.Nombre

class Estampados(models.Model):
    Nombre = models.CharField(max_length = 100)
    Talla = models.CharField(max_length = 6)
    Descripcion = models.CharField(max_length = 200)
    Tela= models.ForeignKey(Tela, models.PROTECT)
    Camisa = models.OneToOneField(Camisa, models.PROTECT)
    
    def __str__ (self): 
        return self.Nombre

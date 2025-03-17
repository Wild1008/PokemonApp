from django.db import models

# Create your models here.
class DatosPokemon(models.Model):
    id = models.AutoField(primary_key= True, verbose_name="ID")
    nombre = models.CharField("Nombre", max_length=100)
    tipos =  models.CharField("Tipos", max_length=100)
    peso = models.DecimalField("Peso", max_digits=5, decimal_places=1)
    altura = models.DecimalField("Altura", max_digits=6, decimal_places=2)

def __str__(self):
        return self.nombre
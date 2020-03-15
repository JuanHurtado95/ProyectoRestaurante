from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
    cedula=models.CharField(max_length=30) 

    def __str__(self):
        return self.nombre 

class ingredientes(models.Model):
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    precio=models.CharField(max_length=20)

    def __str__(self):
        return 'El nombre es %s el tipo es %s y el precio es %s' % (self.nombre, self.tipo, self.precio) 

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class empleados(models.Model):
    nombre=models.CharField(max_length=30)
    cargo=models.CharField(max_length=30)
    celular=models.CharField(max_length=10)
    password=models.CharField(max_length=30)
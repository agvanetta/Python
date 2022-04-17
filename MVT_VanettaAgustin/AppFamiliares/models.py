from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombreYApellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    fechaDeNacimiento = models.DateField()

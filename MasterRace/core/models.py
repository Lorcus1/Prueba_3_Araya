from django.db import models

class Componente(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=99)

class Fabricante ()
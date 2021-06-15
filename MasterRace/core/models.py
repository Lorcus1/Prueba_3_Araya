from django.db import models

class Componente(models.Model):
    ID          = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=99)

    def __str__(self):
        return self.Nombre

class Fabricante(models.Model):
    ID          = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=99)

    def __str__(self):
        return self.Nombre

class Producto(models.Model):
    ID          = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=99)
    Fabricante  = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True)
    Componente  = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    Precio      = models.IntegerField(default=0)
    Stock       = models.IntegerField(default=0)
    Imagen      = models.FileField(upload_to='static/media', null=True, blank=True )

    def __str__(self):
        return self.Nombre + '(' + str(self.ID) + ')'
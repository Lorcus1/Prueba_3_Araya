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
    def ruta_imagen(self, filename):
        return f'productos/{self.ID}/{filename}'

    magen = models.ImageField(upload_to = ruta_imagen, max_length = 9999, null = True, blank = True)

    def __str__(self):
        return self.Nombre + '(' + str(self.ID) + ')'
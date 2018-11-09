from django.db import models

# Create your models here.
class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas" 


class Estado(models.Model):
    tipoEstado = models.CharField(max_length=15)

    def __str__(self):
        return self.tipoEstado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Genero(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"


class Mascota(models.Model):
    nombre = models.CharField(max_length=25)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='photo')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
         return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"


class GeneroAdoptante(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "GeneroAdoptante"
        verbose_name_plural = "GenerosAdoptantes"


class Region(models.Model):
    idRegion = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"


class Ciudad(models.Model):
    idCiudad = models.IntegerField()
    nombre = models.CharField(max_length=80)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class tipoVivienda(models.Model):
    idTipo = models.IntegerField()
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        verbose_name = "Tipo Vivienda"
        verbose_name_plural = "Tipos Viviendas"


class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    tel = models.IntegerField()
    direccion = models.CharField(max_length=80)
    genero = models.ForeignKey(GeneroAdoptante, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(tipoVivienda, on_delete=models.CASCADE, null=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

    



















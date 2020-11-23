from django.db import models

# Create your models here.

class Tipo_Medicamento(models.Model):
    id_Tipo_Medicamento = models.AutoField(primary_key=True)
    Nombre_Tipo_Medicamento = models.CharField(max_length=150,verbose_name="Nombre tipo medicamento")
    
    def __str__(self):
        return u'{0}'.format(self.Nombre_Tipo_Medicamento)

class Medicamentos(models.Model):
    id_Medicamento = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100,verbose_name="Nombre medicamento")
    Marca = models.CharField(max_length=100,verbose_name="Marca medicamento")
    Laboratorio = models.CharField(max_length=100,verbose_name="Laboratorio medicamento")
    Cantidad_de_comprimidos = models.IntegerField(verbose_name="Cantidad de comprimidos")
    Gramaje = models.IntegerField(verbose_name="Gramaje")
    id_Tipo_medicamento = models.ForeignKey(Tipo_Medicamento, on_delete=models.CASCADE)
    Habilitado = models.BooleanField(default=True,verbose_name="Medicamento Habilitado")

    def __str__(self):
        return u'{0}'.format(self.Nombre)

    
    

class Info_Medicamentos(models.Model):
    id_Informacion = models.OneToOneField(Medicamentos, on_delete=models.CASCADE,primary_key=True)
    Formula = models.CharField(max_length=200,verbose_name="Formula")
    Advertencias = models.CharField(max_length=250,verbose_name="Advertencias")
    Indicaciones = models.CharField(max_length=250,verbose_name="Indicaciones")
    Contra_Indicaciones = models.CharField(max_length=250, verbose_name="Contra indicaciones")
    Bioequivalente = models.BooleanField(verbose_name="Bioequivalente")

    def __str__(self):
        return u'{0}'.format(self.id_Informacion)






from django.db import models

class rtv_cup(models.Model):
    fecha=models.DateField()
    cant=models.IntegerField()
    valor_facial=models.FloatField()
    valor_etecsa=models.FloatField()
    ingreso_ag=models.FloatField()
    tcant=models.IntegerField()
    tvalor_facial=models.FloatField()
    tvalor_etecsa=models.FloatField()
    tingreso_ag=models.FloatField()


class rtv_nauta(models.Model):
    fecha=models.DateField()
    cant=models.IntegerField()
    valor_facial=models.FloatField()
    valor_etecsa=models.FloatField()
    ingreso_ag_cuc=models.FloatField()
    ingreso_ag_cup=models.FloatField()
    tcant=models.IntegerField()
    tvalor_facial=models.FloatField()
    tvalor_etecsa=models.FloatField()
    tingreso_ag_cuc=models.FloatField()
    tingreso_ag_cup=models.FloatField()    

class rtv_movil(models.Model):
    fecha=models.DateField()
    cant=models.IntegerField()
    valor_facial=models.FloatField()
    valor_etecsa=models.FloatField()
    ingreso_ag_cuc=models.FloatField()
    ingreso_ag_cup=models.FloatField()
    tcant=models.IntegerField()
    tvalor_facial=models.FloatField()
    tvalor_etecsa=models.FloatField()
    tingreso_ag_cuc=models.FloatField()
    tingreso_ag_cup=models.FloatField()

class costo_utilidad(models.Model):
    costo_etecsa=models.FloatField()
    utilidad_diaria=models.FloatField()

from django.db import models

class rtv_cup(models.Model):
    fecha=models.DateField()
    cant_c=models.IntegerField(verbose_name='Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Cantidad de 10')
    cant_v=models.IntegerField(verbose_name='Cantidad de 20')
    valor_facial=models.FloatField(verbose_name='Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Valor Etecsa')
    ingreso_ag=models.FloatField(verbose_name='Ingreso A.G')

class trtv_cup(models.Model):
    def __str__(self):
        return self.mes
    fecha=models.DateField()
    tcant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    tcant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    tcant_v=models.IntegerField(verbose_name='Total: Cantidad de 20')
    tvalor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    tvalor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    tingreso_ag=models.FloatField(verbose_name='Total: Ingreso')
    mes=models.CharField(max_length=50, default='')

class t_anual(models.Model):
    fecha=models.DateField() 
    cant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    cant_v=models.IntegerField(verbose_name='Total: Cantidad de 20')
    valor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    ingreso_ag=models.FloatField(verbose_name='Total: Ingreso')

class rtv_nauta(models.Model):
    fecha=models.DateField() 
    cant_dos=models.IntegerField(verbose_name='Total: Cantidad de 2')
    cant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    valor_facial=models.FloatField(verbose_name='Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Valor Etecsa')
    ingreso_ag_cuc=models.FloatField(verbose_name='Ingreso A.G-CUC')
    ingreso_ag_cup=models.FloatField(verbose_name='Ingreso A.G-CUP')    

class trtv_nauta(models.Model):
    fecha=models.DateField()
    tcant_dos=models.IntegerField(verbose_name='Total: Cantidad de 2')
    tcant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    tcant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    tvalor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    tvalor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    tingreso_ag_cuc=models.FloatField(verbose_name='Total: Ingreso A.G-CUC')
    tingreso_ag_cup=models.FloatField(verbose_name='Total: Ingreso A.G-CUP')    
    mes=models.CharField(max_length=50, default='')

class t_anual_nauta(models.Model):
    fecha=models.DateField() 
    cant_dos=models.IntegerField(verbose_name='Total: Cantidad de 2')
    cant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    valor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    ingreso_ag_cuc=models.FloatField(verbose_name='Total: Ingreso')
    ingreso_ag_cup=models.FloatField(verbose_name='Total: Ingreso')

class rtv_movil(models.Model):
    fecha=models.DateField()
    cant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    cant_v=models.IntegerField(verbose_name='Total: Cantidad de 20')
    valor_facial=models.FloatField(verbose_name='Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Valor Etecsa')
    ingreso_ag_cuc=models.FloatField(verbose_name='Ingreso A.G-CUC')
    ingreso_ag_cup=models.FloatField(verbose_name='Ingreso A.G-CUP')

class trtv_movil(models.Model):
    fecha=models.DateField()
    tcant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    tcant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    tcant_v=models.IntegerField(verbose_name='Total: Cantidad de 20')
    tvalor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    tvalor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    tingreso_ag_cuc=models.FloatField(verbose_name='Total: Ingreso A.G-CUC')
    tingreso_ag_cup=models.FloatField(verbose_name='Total: Ingreso A.G-CUP')
    mes=models.CharField(max_length=50, default='')

class t_anual_movil(models.Model):
    fecha=models.DateField()
    cant_c=models.IntegerField(verbose_name='Total: Cantidad de 5')
    cant_d=models.IntegerField(verbose_name='Total: Cantidad de 10')
    cant_v=models.IntegerField(verbose_name='Total: Cantidad de 20')
    valor_facial=models.FloatField(verbose_name='Total: Valor Facial')
    valor_etecsa=models.FloatField(verbose_name='Total: Valor Etecsa')
    ingreso_ag_cuc=models.FloatField(verbose_name='Total: Ingreso')
    ingreso_ag_cup=models.FloatField(verbose_name='Total: Ingreso')


class costo_utilidad(models.Model):
    fecha=models.DateField()
    costo_etecsa=models.FloatField(verbose_name='Costo Etecsa')
    utilidad_diaria=models.FloatField(verbose_name='Utilidad Diaria')
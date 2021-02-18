from django import forms
from django.forms.widgets import SelectDateWidget, Select
from PbApp.models import trtv_cup
import datetime
class form_insert_cup_movil(forms.Form):

    fecha=forms.DateField(widget=SelectDateWidget())
    cant_5=forms.IntegerField(required=None)
    cant_10=forms.IntegerField(required=None)
    cant_20=forms.IntegerField(required=None)

class form_insert_nauta(forms.Form):

    fecha=forms.DateField(widget=SelectDateWidget())
    cant_2=forms.IntegerField(required=None)
    cant_5=forms.IntegerField(required=None)
    cant_10=forms.IntegerField(required=None)

class form_rango_meses(forms.Form):

    mes_de_inicio=forms.ModelChoiceField(trtv_cup.objects.filter(fecha__icontains=datetime.datetime.now().year))
    mes_final=forms.ModelChoiceField(trtv_cup.objects.filter(fecha__icontains=datetime.datetime.now().year))

class form_insert_fact(forms.Form):
    fecha=forms.DateField(widget=SelectDateWidget())
    factura=forms.FloatField()

class form_insert_pago_onat(forms.Form):
    fecha=forms.DateField(widget=SelectDateWidget())
    pagado=forms.FloatField()

class form_limpiar_registros(forms.Form):
    Limpiar_registros=forms.BooleanField(required=False)
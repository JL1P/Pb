from django import forms
from django.forms.widgets import SelectDateWidget, Select
from PbApp.models import trtv_cup

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

    mes_de_inicio=forms.ModelChoiceField(trtv_cup.objects.all())
    mes_final=forms.ModelChoiceField(queryset=trtv_cup.objects.all())

class form_insert_fact(forms.Form):
    fecha=forms.DateField(widget=SelectDateWidget())
    factura=forms.FloatField()
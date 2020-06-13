from django import forms
from django.forms.widgets import SelectDateWidget

class form_insert_cup(forms.Form):

    fecha=forms.DateField(widget=SelectDateWidget())
    cant=forms.IntegerField()
    valor_facial=forms.FloatField()
    valor_etecsa=forms.FloatField()
    ingreso_ag=forms.FloatField()
    
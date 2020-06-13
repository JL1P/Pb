from django.shortcuts import render
import datetime
from PbApp.models import rtv_cup, rtv_movil, rtv_nauta 
from PbApp.forms import form_insert_cup
from django.contrib.admin import widgets

def home(request):
    return render(request, "home.html")

def rel_trgtas_vendidas(request):
    return render(request, 'rel_trgtas_vendidas.html')

def menu_rtv_cup(request):
    return render(request, 'menu_rtv_cup.html')

def insert_rtv_cup(request):
    alert=False
    if request.method=='POST':
        miFormulario=form_insert_cup(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            x=rtv_cup.objects.create(fecha=infForm['fecha'], cant=infForm['cant'], valor_facial=infForm['valor_facial'], valor_etecsa=infForm['valor_etecsa'], ingreso_ag=infForm['ingreso_ag'])
            alert=True
    else:
        miFormulario=form_insert_cup()
    return render(request, 'insert_rtv_cup.html', {'form':miFormulario, 'alert':alert})

def rel_trgtas_vendidas_cup(request):
    x=datetime.datetime.now()
    meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes=meses[x.month-1]
    return render(request, 'rel_trgtas_vendidas_cup.html', {'month':mes})

def rel_trgtas_vendidas_nauta(request):
    return render(request, 'rel_trgtas_vendidas_nauta.html')

def rel_trgtas_vendidas_movil(request):
    return render(request, 'rel_trgtas_vendidas_movil.html')

def facturaciones(request):
    return render(request, 'facturaciones.html')

def facturaciones_cup(request):
    return render(request, 'facturaciones_cup.html')

def facturaciones_cuc(request):
    return render(request, 'facturaciones_cuc.html')

def ap(request):
    return render(request, 'ap.html')

def prestamistas(request):
    return render(request, 'prestamistas.html')

def recargas(request):
    return render(request, 'recargas.html')

def situacion_financiera(request):
    return render(request, 'situacion_financiera.html')

def onat_etecsa(request):
    return render(request, 'onat_etecsa.html')

def extras(request):
    return render(request, 'extras.html')

def extras_arqueo(request):
    return render(request, 'extras_arqueo.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import datetime
from PbApp.models import rtv_cup, rtv_movil, rtv_nauta, trtv_cup, trtv_movil, trtv_nauta 
from PbApp.forms import form_insert_cup
from django.contrib.admin import widgets
from PbApp.rtv.rtv_cup import sum_tcant_cup, sum_tvalor_facial, sum_tvalor_etecsa, sum_tingreso_ag

def home(request):
    return render(request, "home.html")

def rel_trgtas_vendidas(request):
    return render(request, 'rel_trgtas_vendidas.html')

def menu_rtv_cup(request):

    return render(request, 'menu_rtv_cup.html')

def insert_rtv_cup(request):
    #evaluando si la tcant de ese mes esta creada
    datoday=datetime.datetime.now()
    date_cut=str(datoday.date())
    date_ev=date_cut[0:7]
    date_total=[]
    date_total=trtv_cup.objects.all()
    coincidencia=False
    for x in date_total:
        z=str(x.fecha)
        z=z[0:7]
        if z==date_ev: coincidencia=True

    if not coincidencia: x=trtv_cup.objects.create(fecha=date_cut, tcant=0, tvalor_facial=0, tvalor_etecsa=0, tingreso_ag=0)
    #ingresando datos a la Db
    alert=False
    if request.method=='POST':
        miFormulario=form_insert_cup(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            #Evaluando si el dato se encuentra en la Db
            coinc=rtv_cup.objects.filter(fecha__icontains=infForm['fecha'])
            borrar=coinc
            if coinc: borrar.delete()
            x=rtv_cup.objects.create(fecha=infForm['fecha'], cant=infForm['cant'], valor_facial=infForm['valor_facial'], valor_etecsa=infForm['valor_etecsa'], ingreso_ag=infForm['ingreso_ag'])
            alert=True

#Añadiendo valores a tcant
            sum_tcant_cup(infForm['fecha'])
#Añadiendo valores a tvalor facial
            sum_tvalor_facial(infForm['fecha'])
#Añadiendo valores a tvalor etecsa
            sum_tvalor_etecsa(infForm['fecha'])
#Añadiendo valores a tingreso AG
            sum_tingreso_ag(infForm['fecha'])
    else:
        miFormulario=form_insert_cup()
    
    return render(request, 'insert_rtv_cup.html', {'form':miFormulario, 'alert':alert})

def rel_trgtas_vendidas_cup(request):
    #mes del encabezado
    x=datetime.datetime.now()
    meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    mes=meses[x.month-1]
    #mes que se va a mostrar en la tabla
    if x.month < 10: mest='0'+str(mes)
    date_cut=str(x.date())
    date_ev=date_cut[0:7]
    mes_actual=date_ev
    month_to_show='2020-01'
    resultados=rtv_cup.objects.filter(fecha__icontains=month_to_show).order_by('fecha')
    tresultados=trtv_cup.objects.filter(fecha__icontains=month_to_show)
    return render(request, 'rel_trgtas_vendidas_cup.html', {'month':mes, 'result':resultados, 'tresult':tresultados})

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
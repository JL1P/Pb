from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import datetime
from PbApp.models import rtv_cup, rtv_movil, rtv_nauta, trtv_cup, trtv_movil, trtv_nauta, t_anual, t_anual_nauta, t_anual_movil
from PbApp.forms import form_insert_cup_movil, form_insert_nauta, form_rango_meses
from django.contrib.admin import widgets
from PbApp.rtv.rtv_cup import sum_tcant_cup, sum_tvalor_facial, sum_tvalor_etecsa, sum_tingreso_ag, sum_t_anual
from PbApp.rtv.rtv_nauta import sum_tcant_nauta, sum_tvalor_facial_nauta, sum_tvalor_etecsa_nauta, sum_tingreso_ag_cuc_nauta, sum_tingreso_ag_cup_nauta, sum_t_anual_nauta
from PbApp.rtv.rtv_movil import sum_tcant_movil, sum_tvalor_facial_movil, sum_tvalor_etecsa_movil, sum_tingreso_ag_cuc_movil, sum_tingreso_ag_cup_movil, sum_t_anual_movil

global mes_numero_corto
mes_numero_corto=datetime.datetime.now()
mes_numero_corto=mes_numero_corto.month

global meses_s
meses_s=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

global datoday
datoday_full=datetime.datetime.now()
datoday=datetime.datetime.now()
datoday=str(datoday.date())

#classmethod(rel_trgtas_vendidas_cup)

def home(request):
    return render(request, "home.html", {'mes_c':mes_numero_corto})

def menu_rtv_cup_2020(request):
    return render(request, 'menu_rtv_2020.html', {'mes_c':mes_numero_corto, 'tmpl': 'rel_trgtas_vendidas_cup'})

def menu_rtv_nauta_2020(request):
    return render(request, 'menu_rtv_2020.html', {'mes_c':mes_numero_corto, 'tmpl': 'rel_trgtas_vendidas_nauta'})

def menu_rtv_movil_2020(request):
    return render(request, 'menu_rtv_2020.html', {'mes_c':mes_numero_corto, 'tmpl': 'rel_trgtas_vendidas_movil'})

def total_anual(request):
    years=datoday[:4]
    resultados=trtv_cup.objects.filter(fecha__icontains=years).order_by('fecha')
    tresultados=t_anual.objects.filter(fecha__icontains=years)
    date_total=[]
    date_total=t_anual.objects.all()
    coincidencia=False
    mes_1='Enero'
    mes_2=meses_s[int(datoday[5:7])-1]
    for x in date_total:
        z=str(x.fecha)
        z=z[:4]
        if z==years: coincidencia=True

    if not coincidencia: x=t_anual.objects.create(fecha=datoday, cant_c=0, cant_d=0, cant_v=0, valor_facial=0, valor_etecsa=0, ingreso_ag=0)
    if request.method=='POST':
        miF=form_rango_meses(request.POST)
        if miF.is_valid():
            infForm=miF.cleaned_data
            mes_1=infForm['mes_de_inicio']
            mes_2=infForm['mes_final']
    else:
        miF=form_rango_meses()
    return render(request, 't_anual.html', {'mes_c':mes_numero_corto, 'year':years, 'result':resultados, 'tresultados':tresultados, 'mes_1':mes_1, 'mes_2':mes_2, 'form':miF})

def total_anual_nauta(request):
    years=datoday[:4]
    resultados=trtv_nauta.objects.filter(fecha__icontains=years).order_by('fecha')
    tresultados=t_anual_nauta.objects.filter(fecha__icontains=years)
    date_total=[]
    date_total=t_anual_nauta.objects.all()
    coincidencia=False
    for x in date_total:
        z=str(x.fecha)
        z=z[:4]
        if z==years: coincidencia=True

    if not coincidencia: x=t_anual_nauta.objects.create(fecha=datoday, cant_dos=0, cant_c=0, cant_d=0, valor_facial=0, valor_etecsa=0, ingreso_ag_cuc=0, ingreso_ag_cup=0)

    return render(request, 't_anual_nauta.html', {'mes_c':mes_numero_corto, 'year':years, 'result':resultados, 'tresultados':tresultados})

def total_anual_movil(request):
    years=datoday[:4]
    resultados=trtv_movil.objects.filter(fecha__icontains=years).order_by('fecha')
    tresultados=t_anual_movil.objects.filter(fecha__icontains=years)
    date_total=[]
    date_total=t_anual_movil.objects.all()
    coincidencia=False
    for x in date_total:
        z=str(x.fecha)
        z=z[:4]
        if z==years: coincidencia=True

    if not coincidencia: x=t_anual_movil.objects.create(fecha=datoday, cant_c=0, cant_d=0, cant_v=0, valor_facial=0, valor_etecsa=0, ingreso_ag_cuc=0, ingreso_ag_cup=0)

    return render(request, 't_anual_movil.html', {'mes_c':mes_numero_corto, 'year':years, 'result':resultados, 'tresultados':tresultados})

def insert_rtc(request):
    #evaluando si la tcant de ese mes esta creada
    mes_atras=mes_numero_corto
    date_ev=datoday[:7]
    #Llenando el trtv del mes actual y anteriores
    len_trtv=trtv_cup.objects.all()
    if int(datoday[5:7])>len(len_trtv): comp_tcant.full_tcant_cup(date_ev,trtv_cup)
    #ingresando datos a la Db
    alert=False
    if request.method=='POST':
        miF=form_insert_cup_movil(request.POST)
        if miF.is_valid():
            infForm=miF.cleaned_data
            #Evaluando si el dato se encuentra en la Db
            coinc=rtv_cup.objects.filter(fecha__icontains=infForm['fecha'])
            borrar=coinc
            if coinc: borrar.delete()
            #numero de mes para q retroceda y salga en la tabla de ese mes
            mes_atras=str(infForm['fecha'])
            mes_atras=mes_atras[5:7]
            if mes_atras[0]=='0': mes_atras.strip('0')
            mes_atras=int(mes_atras)
            #Poniendo por defecto '0' si no es entrado algun valor
            c5=infForm['cant_5']
            c10=infForm['cant_10']
            c20=infForm['cant_20']
            if c5==None: c5=0
            if c10==None: c10=0
            if c20==None: c20=0
            val_facial=c5*5+c10*10+c20*20
            ing_ag=val_facial*0.10
            val_etecsa=val_facial-ing_ag
            x=rtv_cup.objects.create(fecha=infForm['fecha'], cant_c=c5, cant_d=c10, cant_v=c20, valor_facial=val_facial, valor_etecsa=val_etecsa, ingreso_ag=ing_ag)
            alert=True

    #Añadiendo valores a tcant
            sum_tcant_cup(infForm['fecha'])
    #Añadiendo valores a tvalor facial
            sum_tvalor_facial(infForm['fecha'])
    #Añadiendo valores a tvalor etecsa
            sum_tvalor_etecsa(infForm['fecha'])
    #Añadiendo valores a tingreso AG
            sum_tingreso_ag(infForm['fecha'])
    #Añadiendo valores a t_anual
            sum_t_anual(infForm['fecha'])
    else:
        miF=form_insert_cup_movil()    
    return render(request, 'insert_rtc.html', {'form':miF, 'alert':alert, 'mes_c':mes_numero_corto, 'mes_a':mes_atras})

def insert_rtc_nauta(request):
    #evaluando si la tcant de ese mes esta creada
    mes_atras=mes_numero_corto
    date_ev=datoday[:7]
    #Llenando el trtv del mes actual y anteriores
    len_trtv=trtv_nauta.objects.all()
    if int(datoday[5:7])>len(len_trtv): comp_tcant.full_tcant_nauta(date_ev,trtv_nauta)
    #ingresando datos a la Db
    alert=False
    if request.method=='POST':
        miF=form_insert_nauta(request.POST)
        if miF.is_valid():
            infForm=miF.cleaned_data
            #Evaluando si el dato se encuentra en la Db, si está se reemplaza
            coinc=rtv_nauta.objects.filter(fecha__icontains=infForm['fecha'])
            borrar=coinc
            if coinc: borrar.delete()
            #numero de mes para q retroceda y salga en la tabla de ese mes
            mes_atras=str(infForm['fecha'])
            mes_atras=mes_atras[5:7]
            if mes_atras[0]=='0': mes_atras.strip('0')
            mes_atras=int(mes_atras)
            #Poniendo por defecto '0' si no es entrado algun valor
            c2=infForm['cant_2']
            c5=infForm['cant_5']
            c10=infForm['cant_10']
            if c2==None: c2=0
            if c5==None: c5=0
            if c10==None: c10=0
            val_facial=c2*2+c5*5+c10*10
            ing_ag_cuc=val_facial*0.10
            ing_ag_cup=ing_ag_cuc*24
            val_etecsa=val_facial-ing_ag_cuc
            x=rtv_nauta.objects.create(fecha=infForm['fecha'], cant_dos=c2, cant_c=c5, cant_d=c10, valor_facial=val_facial, valor_etecsa=val_etecsa, ingreso_ag_cuc=ing_ag_cuc, ingreso_ag_cup=ing_ag_cup)
            alert=True

    #Añadiendo valores a tcant
            sum_tcant_nauta(infForm['fecha'])
    #Añadiendo valores a tvalor facial
            sum_tvalor_facial_nauta(infForm['fecha'])
    #Añadiendo valores a tvalor etecsa
            sum_tvalor_etecsa_nauta(infForm['fecha'])
    #Añadiendo valores a tingreso AG CUC
            sum_tingreso_ag_cuc_nauta(infForm['fecha'])
    #Añadiendo valores a tingreso AG CUP
            sum_tingreso_ag_cup_nauta(infForm['fecha'])
    #Añadiendo valores a t_anual
            sum_t_anual_nauta(infForm['fecha'])
    else:
        miF=form_insert_nauta()
    
    return render(request, 'insert_rtc_nauta.html', {'form':miF, 'alert':alert, 'mes_c':mes_numero_corto, 'mes_a':mes_atras})

def insert_rtc_movil(request):
    #evaluando si la tcant de ese mes esta creada
    mes_atras=mes_numero_corto
    date_ev=datoday[:7]
    #Llenando el trtv del mes actual y anteriores
    len_trtv=trtv_cup.objects.all()
    if int(datoday[5:7])>len(len_trtv): comp_tcant.full_tcant_movil(date_ev,trtv_movil)
    #ingresando datos a la Db
    alert=False
    if request.method=='POST':
        miF=form_insert_cup_movil(request.POST)
        if miF.is_valid():
            infForm=miF.cleaned_data
            #Evaluando si el dato se encuentra en la Db, si está se reemplaza
            coinc=rtv_movil.objects.filter(fecha__icontains=infForm['fecha'])
            borrar=coinc
            if coinc: borrar.delete()
            #numero de mes para q retroceda y salga en la tabla de ese mes
            mes_atras=str(infForm['fecha'])
            mes_atras=mes_atras[5:7]
            if mes_atras[0]=='0': mes_atras.strip('0')
            mes_atras=int(mes_atras)
            #Poniendo por defecto '0' si no es entrado algun valor
            c5=infForm['cant_5']
            c10=infForm['cant_10']
            c20=infForm['cant_20']
            if c5==None: c5=0
            if c10==None: c10=0
            if c20==None: c20=0
            val_facial=c5*5+c10*10+c20*20
            ing_ag_cuc=val_facial*0.10
            ing_ag_cup=ing_ag_cuc*24
            val_etecsa=val_facial-ing_ag_cuc
            x=rtv_movil.objects.create(fecha=infForm['fecha'], cant_c=c5, cant_d=c10, cant_v=c20, valor_facial=val_facial, valor_etecsa=val_etecsa, ingreso_ag_cuc=ing_ag_cuc, ingreso_ag_cup=ing_ag_cup)
            alert=True

    #Añadiendo valores a tcant
            sum_tcant_movil(infForm['fecha'])
    #Añadiendo valores a tvalor facial
            sum_tvalor_facial_movil(infForm['fecha'])
    #Añadiendo valores a tvalor etecsa
            sum_tvalor_etecsa_movil(infForm['fecha'])
    #Añadiendo valores a tingreso AG CUC
            sum_tingreso_ag_cuc_movil(infForm['fecha'])
    #Añadiendo valores a tingreso AG CUP
            sum_tingreso_ag_cup_movil(infForm['fecha'])
    #Añadiendo valores a t_anual
            sum_t_anual_movil(infForm['fecha'])
    else:
        miF=form_insert_cup_movil()
    
    return render(request, 'insert_rtc_movil.html', {'form':miF, 'alert':alert, 'mes_c':mes_numero_corto, 'mes_a':mes_atras})

def rel_trgtas_vendidas(request, mes_menu=None):
    r=retv.relacion_trgtas_vend_total(request, trtv_cup, t_anual, trtv_nauta, t_anual_nauta, trtv_movil, t_anual_movil, mes_menu, 'trgtas_total_anual.html')
    return HttpResponse(r)

def rel_trgtas_vendidas_cup(request, mes_menu=None):
    r=retv.relacion_trgtas_vend(request, rtv_cup, trtv_cup, mes_menu, 'rel_trgtas_vendidas_cup.html')
    return HttpResponse(r)

def rel_trgtas_vendidas_nauta(request, mes_menu=None):
    r=retv.relacion_trgtas_vend(request, rtv_nauta, trtv_nauta, mes_menu, 'rel_trgtas_vendidas_nauta.html')
    return HttpResponse(r)

def rel_trgtas_vendidas_movil(request, mes_menu=None):
    r=retv.relacion_trgtas_vend(request, rtv_nauta, trtv_movil, mes_menu, 'rel_trgtas_vendidas_movil.html')
    return HttpResponse(r)

def facturaciones(request):
    return render(request, 'facturaciones.html', {'mes_c':mes_numero_corto})

def facturaciones_cup(request):
    return render(request, 'facturaciones_cup.html', {'mes_c':mes_numero_corto})

def facturaciones_cuc(request):
    return render(request, 'facturaciones_cuc.html', {'mes_c':mes_numero_corto})

def ap(request):
    return render(request, 'ap.html', {'mes_c':mes_numero_corto})

def prestamistas(request):
    return render(request, 'prestamistas.html', {'mes_c':mes_numero_corto})

def recargas(request):
    return render(request, 'recargas.html', {'mes_c':mes_numero_corto})

def situacion_financiera(request):
    return render(request, 'situacion_financiera.html', {'mes_c':mes_numero_corto})

def onat_etecsa(request):
    return render(request, 'onat_etecsa.html', {'mes_c':mes_numero_corto})

def extras(request):
    return render(request, 'extras.html', {'mes_c':mes_numero_corto})

def extras_arqueo(request):
    return render(request, 'extras_arqueo.html', {'mes_c':mes_numero_corto})


class retv():
        '''Renderiza las plantillas'''
        @classmethod
        def relacion_trgtas_vend(cls, reqq, tabla, ttabla, mes_menus, temp):
            x=datetime.datetime.now()
            #mes del encabezado
            mes=meses_s[mes_numero_corto-1]
            #mes que se va a mostrar en la tabla
            if x.month < 10: mest='0'+str(mes)
            date_cut=str(x.date())
            date_ev=date_cut[:7]
            mes_actual=date_ev
            mes_conv='2020-0'+str(mes_menus)
            if mes_menus:
                a=mes_conv
                mes=meses_s[mes_menus-1]
            else:
                a=mes_actual
            month_to_show=a
            resultados=tabla.objects.filter(fecha__icontains=month_to_show).order_by('fecha')
            tresultados=ttabla.objects.filter(fecha__icontains=month_to_show)
            return render(reqq, temp, {'month':mes, 'result':resultados, 'tresult':tresultados, 'mes_c':mes_numero_corto})
        
        @classmethod
        def relacion_trgtas_vend_total(cls, reqq, tabla_cup, ttabla_cup, tabla_nauta, ttabla_nauta, tabla_movil, ttabla_movil, mes_menus, temp):
            #año del encabezado
            year=datoday_full.year
            #año que se va a mostrar en la tabla
            year_to_show=year
            resultados_cup=tabla_cup.objects.filter(fecha__icontains=year_to_show).order_by('fecha')
            tresultados_cup=ttabla_cup.objects.filter(fecha__icontains=year)
            resultados_nauta=tabla_nauta.objects.filter(fecha__icontains=year_to_show).order_by('fecha')
            tresultados_nauta=ttabla_nauta.objects.filter(fecha__icontains=year)
            resultados_movil=tabla_movil.objects.filter(fecha__icontains=year_to_show).order_by('fecha')
            tresultados_movil=ttabla_movil.objects.filter(fecha__icontains=year)
            return render(
                reqq, temp, {'year':year, 'result_cup':resultados_cup, 'tresult_cup':tresultados_cup,
            'result_nauta':resultados_nauta, 'tresult_nauta':tresultados_nauta,'result_movil':resultados_movil, 
            'tresult_movil':tresultados_movil, 'mes_c':mes_numero_corto}
            )

class comp_tcant():
    '''Crea el mes actual y anteriores de tcant'''
    
    @classmethod
    def full_tcant_cup(cls, date_e, ttabla):
        date_total=[]
        mes_total=[]
        date_total=ttabla.objects.all()
        coincidencia=False
        for x in date_total:
            z=str(x.fecha)
            z=z[:7]
            if z==date_e:  
                i=int(date_e[5:7])-1
                if i<10: i='0'+str(i)
                date_e=date_e[:5]+str(i)
                if int(i)<1: break
                coincidencia=True
        else:
            if not coincidencia: x=ttabla.objects.create(fecha=date_e+'-01', tcant_c=0, tcant_d=0, tcant_v=0, tvalor_facial=0, tvalor_etecsa=0, tingreso_ag=0, mes=meses_s[int(date_e[5:7])-1])
            i=int(date_e[5:7])-1
            if i<10: i='0'+str(i)
            date_e=date_e[:5]+str(i)
        if date_e[5:]!='00': comp_tcant.full_tcant_cup(date_e,trtv_cup)
        
    @classmethod
    def full_tcant_nauta(cls, date_e, ttabla):
        date_total=[]
        date_total=ttabla.objects.all()
        coincidencia=False
        for x in date_total:
            z=str(x.fecha)
            z=z[:7]
            if z==date_e:  
                i=int(date_e[5:7])-1
                if i<10: i='0'+str(i)
                date_e=date_e[:5]+str(i)
                if int(i)<1: break
                coincidencia=True
        else:
            if not coincidencia: x=ttabla.objects.create(fecha=date_e+'-01', tcant_dos=0, tcant_c=0, tcant_d=0, tvalor_facial=0, tvalor_etecsa=0, tingreso_ag_cuc=0, tingreso_ag_cup=0, mes=meses_s[int(date_e[5:7])-1])
            i=int(date_e[5:7])-1
            if i<10: i='0'+str(i)
            date_e=date_e[:5]+str(i)
        if date_e[5:]!='00': comp_tcant.full_tcant_nauta(date_e,trtv_nauta)

    @classmethod
    def full_tcant_movil(cls, date_e, ttabla):
        date_total=[]
        date_total=ttabla.objects.all()
        coincidencia=False
        for x in date_total:
            z=str(x.fecha)
            z=z[:7]
            if z==date_e:  
                i=int(date_e[5:7])-1
                if i<10: i='0'+str(i)
                date_e=date_e[:5]+str(i)
                if int(i)<1: break
                coincidencia=True
        else:
            if not coincidencia: x=ttabla.objects.create(fecha=date_e+'-01', tcant_c=0, tcant_d=0, tcant_v=0, tvalor_facial=0, tvalor_etecsa=0, tingreso_ag_cuc=0, tingreso_ag_cup=0, mes=meses_s[int(date_e[5:7])-1])
            i=int(date_e[5:7])-1
            if i<10: i='0'+str(i)
            date_e=date_e[:5]+str(i)
        if date_e[5:]!='00': comp_tcant.full_tcant_movil(date_e,trtv_movil)

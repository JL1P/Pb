from PbApp.models import rtv_nauta, trtv_nauta, t_anual_nauta

def sum_tcant_nauta(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_nauta.objects.filter(fecha__icontains=fecha_ev)
    dos=0
    c=0
    d=0
    for x in resultados:
        dos=dos+x.cant_dos
        c=c+x.cant_c
        d=d+x.cant_d
    tresultados=trtv_nauta.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tcant_dos=dos
    x.tcant_c=c
    x.tcant_d=d
    x.save()

def sum_tvalor_facial_nauta(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_nauta.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_facial
    tresultados=trtv_nauta.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_facial=z
    x.save()

def sum_tvalor_etecsa_nauta(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_nauta.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_etecsa
    tresultados=trtv_nauta.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_etecsa=z
    x.save()

def sum_tingreso_ag_cup_nauta(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_nauta.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.ingreso_ag_cup
    tresultados=trtv_nauta.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tingreso_ag_cup=z
    x.save()

def sum_t_anual_nauta(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:4]
    resultados=trtv_nauta.objects.filter(fecha__icontains=fecha_ev)
    dos=c=d=vf=ve=ia_cup=0
    for x in resultados:
        dos=dos+x.tcant_dos
        c=c+x.tcant_c
        d=d+x.tcant_d
        vf=vf+x.tvalor_facial
        ve=ve+x.tvalor_etecsa
        ia_cup=ia_cup+x.tingreso_ag_cup

    comp_anual=[]
    comp_anual=t_anual_nauta.objects.all()
    if len(comp_anual)<1:
        x=t_anual_nauta.objects.create(fecha=fecha_ev+'-01-01', cant_dos=0, cant_c=0, cant_d=0, valor_facial=0, valor_etecsa=0, ingreso_ag_cup=0)

    tresultados=t_anual_nauta.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.cant_dos=dos
    x.cant_c=c
    x.cant_d=d
    x.valor_facial=vf
    x.valor_etecsa=ve
    x.ingreso_ag_cup=ia_cup
    x.save()
    
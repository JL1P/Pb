from PbApp.models import rtv_cup, trtv_cup, t_anual

def sum_tcant_cup(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    c=0
    d=0
    v=0
    for x in resultados:
        c=c+x.cant_c
        d=d+x.cant_d
        v=v+x.cant_v
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    tresultados.tcant_c=c
    tresultados.tcant_d=d
    tresultados.tcant_v=v
    tresultados.save()

def sum_tvalor_facial(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_facial
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    tresultados.tvalor_facial=z
    tresultados.save()

def sum_tvalor_etecsa(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_etecsa
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    tresultados.tvalor_etecsa=z
    tresultados.save()

def sum_tingreso_ag(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.ingreso_ag
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    tresultados.tingreso_ag=z
    tresultados.save()

def sum_t_anual(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:4]
    resultados=trtv_cup.objects.filter(fecha__icontains=fecha_ev)
    c=d=v=vf=ve=ia=0
    for x in resultados:
        c=c+x.tcant_c
        d=d+x.tcant_d
        v=v+x.tcant_v
        vf=vf+x.tvalor_facial
        ve=ve+x.tvalor_etecsa
        ia=ia+x.tingreso_ag
    
    #creando el anual si no está
    comp_anual=[]
    comp_anual=t_anual.objects.all()
    if len(comp_anual)<1:
        x=t_anual.objects.create(fecha=fecha_ev+'-01-01', cant_c=0, cant_d=0, cant_v=0, valor_facial=0, valor_etecsa=0, ingreso_ag=0)
    
    tresultados=t_anual.objects.get(fecha__icontains=fecha_ev)
    tresultados.cant_c=c
    tresultados.cant_d=d
    tresultados.cant_v=v
    tresultados.valor_facial=vf
    tresultados.valor_etecsa=ve
    tresultados.ingreso_ag=ia
    tresultados.save()
    
from PbApp.models import rtv_movil, trtv_movil, t_anual_movil

def sum_tcant_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_movil.objects.filter(fecha__icontains=fecha_ev)
    c=0
    d=0
    v=0
    for x in resultados:
        c=c+x.cant_c
        d=d+x.cant_d
        v=v+x.cant_v
    tresultados=trtv_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tcant_c=c
    x.tcant_d=d
    x.tcant_v=v
    x.save()

def sum_tvalor_facial_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_movil.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_facial
    tresultados=trtv_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_facial=z
    x.save()

def sum_tvalor_etecsa_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_movil.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_etecsa
    tresultados=trtv_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_etecsa=z
    x.save()

def sum_tingreso_ag_cuc_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_movil.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.ingreso_ag_cuc
    tresultados=trtv_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tingreso_ag_cuc=z
    x.save()

def sum_tingreso_ag_cup_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_movil.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.ingreso_ag_cup
    tresultados=trtv_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tingreso_ag_cup=z
    x.save()

def sum_t_anual_movil(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:4]
    resultados=trtv_movil.objects.filter(fecha__icontains=fecha_ev)
    c=d=v=vf=ve=ia_cuc=ia_cup=0
    for x in resultados:
        c=c+x.tcant_c
        d=d+x.tcant_d
        v=v+x.tcant_v
        vf=vf+x.tvalor_facial
        ve=ve+x.tvalor_etecsa
        ia_cuc=ia_cuc+x.tingreso_ag_cuc
        ia_cup=ia_cup+x.tingreso_ag_cuc

    comp_anual=[]
    comp_anual=t_anual_movil.objects.all()
    if len(comp_anual)<1:
        x=t_anual_movil.objects.create(fecha=fecha_ev+'-01-01', cant_c=0, cant_d=0, cant_v=0, valor_facial=0, valor_etecsa=0, ingreso_ag_cuc=0, ingreso_ag_cup=0)

    tresultados=t_anual_movil.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.cant_c=c
    x.cant_d=d
    x.cant_v=v
    x.valor_facial=vf
    x.valor_etecsa=ve
    x.ingreso_ag_cuc=ia_cuc
    x.ingreso_ag_cup=ia_cup
    x.save()
    
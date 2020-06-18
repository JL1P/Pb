from PbApp.models import rtv_cup, trtv_cup

def sum_tcant_cup(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.cant
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tcant=z
    x.save()

def sum_tvalor_facial(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_facial
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_facial=z
    x.save()

def sum_tvalor_etecsa(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.valor_etecsa
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tvalor_etecsa=z
    x.save()

def sum_tingreso_ag(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=rtv_cup.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.ingreso_ag
    tresultados=trtv_cup.objects.get(fecha__icontains=fecha_ev)
    x=tresultados
    x.tingreso_ag=z
    x.save()

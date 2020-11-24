from PbApp.models import facturaciones, t_facturaciones, t_anual_facturaciones 

def sum_tf(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=facturaciones.objects.filter(fecha__icontains=fecha_ev)
    fact=0
    for x in resultados:
        fact=fact+x.factura

    tresultados=t_facturaciones.objects.get(fecha__icontains=fecha_ev)
    tresultados.tfactura=fact
    tresultados.save()

def sum_tc(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:7]
    resultados=facturaciones.objects.filter(fecha__icontains=fecha_ev)
    z=0
    for x in resultados:
        z=z+x.comision

    tresultados=t_facturaciones.objects.get(fecha__icontains=fecha_ev)
    tresultados.tcomision=z
    tresultados.save()

def sum_t_anual_facturaciones(tfecha):
    fecha_completa=str(tfecha)
    fecha_ev=fecha_completa[0:4]
    resultados=t_facturaciones.objects.filter(fecha__icontains=fecha_ev)
    f=c=0
    for x in resultados:
        f=f+x.tfactura
        c=c+x.tcomision
    
    #creando el anual si no está
    comp_anual=[]
    comp_anual=t_anual_facturaciones.objects.all()
    if len(comp_anual)<1:
        x=t_anual_facturaciones.objects.create(fecha=fecha_ev+'-01-01', factura=0, comision=0)
    
    tresultados=t_anual_facturaciones.objects.get(fecha__icontains=fecha_ev)
    tresultados.factura=f
    tresultados.comision=c
    tresultados.save()
    
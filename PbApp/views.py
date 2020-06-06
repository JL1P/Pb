from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def rel_trgtas_vendidas(request):
    return render(request, 'rel_trgtas_vendidas.html')

def rel_trgtas_vendidas_cup(request):
    return render(request, 'rel_trgtas_vendidas_cup.html')

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
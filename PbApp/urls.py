from django.urls import path
from PbApp import views
#urls
urlpatterns = [
    path('', views.home, name='home'),
    path('rel_trgtas_vendidas/', views.rel_trgtas_vendidas, name='rel_trgtas_vendidas'),
    path('rel_trgtas_vendidas_cup/', views.rel_trgtas_vendidas_cup, name='rel_trgtas_vendidas_cup'),
    path('rel_trgtas_vendidas_nauta/', views.rel_trgtas_vendidas_nauta, name='rel_trgtas_vendidas_nauta'),
    path('rel_trgtas_vendidas_movil/', views.rel_trgtas_vendidas_movil, name='rel_trgtas_vendidas_movil'),
    path("menu_rtv_cup/", views.menu_rtv_cup, name="menu_rtv_cup"),
    path('menu_enero/', views.rel_trgtas_vendidas_cup, name='menu_enero'),
    path("insert_rtv_cup/", views.insert_rtv_cup, name="insert_rtv_cup"),
    path('facturaciones/', views.facturaciones, name='facturaciones'),
    path('facturaciones_cup/', views.facturaciones_cup, name='facturaciones_cup'),
    path('facturaciones_cuc/', views.facturaciones_cuc, name='facturaciones_cuc'),
    path('ap/', views.ap, name='ap'),
    path('prestamistas/', views.prestamistas, name='prestamistas'),
    path('recargas/', views.recargas, name='recargas'),
    path('situacion_financiera/', views.situacion_financiera, name='situacion_financiera'),
    path('onat_etecsa/', views.onat_etecsa, name='onat_etecsa'),
    path('extras/', views.extras, name='extras'),
    path('extras_arqueo/', views.extras_arqueo, name='extras_arqueo'),

]

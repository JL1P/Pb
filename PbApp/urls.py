from django.urls import path
from PbApp import views
#urls
urlpatterns = [
    path('', views.home, name='home'),
    path('rel_trgtas_vendidas/', views.rel_trgtas_vendidas, name='rel_trgtas_vendidas'),
    path('rel_trgtas_vendidas_cup/<int:mes_menu>', views.rel_trgtas_vendidas_cup, name='rel_trgtas_vendidas_cup'),
    path('rel_trgtas_vendidas_nauta/<int:mes_menu>', views.rel_trgtas_vendidas_nauta, name='rel_trgtas_vendidas_nauta'),
    path('rel_trgtas_vendidas_movil/<int:mes_menu>', views.rel_trgtas_vendidas_movil, name='rel_trgtas_vendidas_movil'),
    path('trgtas_total_anual/<int:mes_menu>', views.rel_trgtas_vendidas, name='trgtas_total_anual'),
    path('t_anual/', views.total_anual, name='t_anual'),
    path('t_anual_nauta/', views.total_anual_nauta, name='t_anual_nauta'),
    path('t_anual_movil/', views.total_anual_movil, name='t_anual_movil'),
    path('menu_rtv_cup-2020/', views.menu_rtv_cup_2020, name="menu_rtv_cup-2020"),
    path('menu_rtv_nauta-2020/', views.menu_rtv_nauta_2020, name="menu_rtv_nauta-2020"),
    path('menu_rtv_movil-2020/', views.menu_rtv_movil_2020, name="menu_rtv_movil-2020"),
    path('insert_rtc/', views.insert_rtc, name="insert_rtc"),
    path('insert_rtc_nauta/', views.insert_rtc_nauta, name="insert_rtc_nauta"),
    path('insert_rtc_movil/', views.insert_rtc_movil, name="insert_rtc_movil"),
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

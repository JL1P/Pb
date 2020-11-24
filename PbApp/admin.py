from django.contrib import admin
from PbApp.models import rtv_cup, rtv_nauta, rtv_movil, trtv_cup, trtv_nauta, trtv_movil, costo_utilidad, t_anual, t_anual_nauta, t_anual_movil

# Register your models here.

class rtv_cupAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_c', 'cant_d', 'cant_v', 'valor_facial', 'valor_etecsa', 'ingreso_ag')
    search_fields=('fecha',)
    list_filter=('fecha',)
    date_hierarchy='fecha'

class rtv_nautaAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_dos','cant_c','cant_d', 'valor_facial', 'valor_etecsa', 'ingreso_ag_cup')
    search_fields=('fecha',)
    list_filter=('fecha',)
    date_hierarchy='fecha'

class rtv_movilAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_c','cant_d','cant_v', 'valor_facial', 'valor_etecsa', 'ingreso_ag_cup')
    search_fields=('fecha',)
    list_filter=('fecha',)
    date_hierarchy='fecha'

class trtv_cupAdmin(admin.ModelAdmin):
    list_display=('fecha', 'tcant_c','tcant_d', 'tcant_v', 'tvalor_facial', 'tvalor_etecsa', 'tingreso_ag')
    search_fields=('fecha',)
    list_filter=('fecha',)
    date_hierarchy='fecha'

class t_anualAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_c', 'cant_d', 'cant_v', 'valor_facial', 'valor_etecsa', 'ingreso_ag')

class trtv_nautaAdmin(admin.ModelAdmin):
    list_display=('fecha', 'tcant_dos','tcant_c','tcant_d', 'tvalor_facial', 'tvalor_etecsa', 'tingreso_ag_cup')
    search_fields=('fecha',)
    list_filter=('fecha',)

class t_anual_nautaAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_dos', 'cant_c', 'cant_d', 'valor_facial', 'valor_etecsa', 'ingreso_ag_cup')

class trtv_movilAdmin(admin.ModelAdmin):
    list_display=('fecha', 'tcant_c','tcant_d','tcant_v', 'tvalor_facial', 'tvalor_etecsa', 'tingreso_ag_cup')
    search_fields=('fecha',)
    list_filter=('fecha',)

class t_anual_movilAdmin(admin.ModelAdmin):
    list_display=('fecha', 'cant_c', 'cant_d', 'cant_v', 'valor_facial', 'valor_etecsa', 'ingreso_ag_cup')

class costo_utilidadAdmin(admin.ModelAdmin):
    list_display=('fecha', 'costo_etecsa', 'utilidad_diaria')
    search_fields=('fecha',)
    list_filter=('fecha',)
    date_hierarchy='fecha'
    
admin.site.register(rtv_cup, rtv_cupAdmin)
admin.site.register(rtv_nauta, rtv_nautaAdmin)
admin.site.register(rtv_movil, rtv_movilAdmin)
admin.site.register(trtv_cup, trtv_cupAdmin)
admin.site.register(trtv_nauta, trtv_nautaAdmin)
admin.site.register(trtv_movil, trtv_movilAdmin)
admin.site.register(costo_utilidad, costo_utilidadAdmin)
admin.site.register(t_anual, t_anualAdmin)
admin.site.register(t_anual_nauta, t_anual_nautaAdmin)
admin.site.register(t_anual_movil, t_anual_movilAdmin)


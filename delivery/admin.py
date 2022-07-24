from atexit import register
from django.contrib import admin

from delivery.models import ( 
    Delivery, 
    Morador, 
    Casa, 
    Box,
    Prestador,
    )


class CasaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'rua']


class MoradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'telefone', 'casa', 'email']


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nota_fiscal', 'data_entrada', 'recebido_por', 'casa', 'modulo', 'status']


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Morador, MoradorAdmin)
admin.site.register(Casa, CasaAdmin)
admin.site.register(Box)
admin.site.register(Prestador)
from django.contrib import admin
from gestionPedidos.models import clientes, ingredientes, pedidos, empleados
# Register your models here.

class clientes_admin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
    search_fields=("nombre", "cedula")


class ingredientes_admin(admin.ModelAdmin):
    list_display=("nombre", "tipo", "precio")
    search_fields=("nombre", "tipo")

class pedidos_admin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    search_fields=("numero","fecha")
    date_hierarchy="fecha"


class empleados_admin(admin.ModelAdmin):
    list_display=("nombre", "cargo", "celular")


admin.site.register(clientes, clientes_admin)
admin.site.register(ingredientes, ingredientes_admin)
admin.site.register(pedidos, pedidos_admin)
admin.site.register(empleados, empleados_admin)

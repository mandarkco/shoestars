from django.contrib import admin
from registros.models import  Venta, PerfilCliente, Cliente, Categoria, Producto, Tienda
from registros.models import  Talla, Inventario, Envio
# Register your models here.

admin.site.register(Venta)
admin.site.register(Tienda)
admin.site.register(PerfilCliente)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Talla)
admin.site.register(Inventario)
admin.site.register(Envio)

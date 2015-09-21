from django.shortcuts import render
from django.http import HttpResponse
from registros.models import Cliente, Tienda, Venta, Producto, PerfilCliente
from registros.models import Inventario
from django.shortcuts import redirect
import json

def vendedor(request):
	if request.user.is_authenticated():
		usuario = request.user
	else:
		return redirect("/")

	ven = Venta.objects.filter(tienda__usuario = usuario).order_by('-fecha_creacion')

	ventas = []
	v_aux = {}
	for v in ven:
		v_aux['numero'] = v.id
		v_aux['cliente'] = v.cliente.usuario.username
		v_aux['producto'] = v.producto.nombre
		v_aux['talla'] = v.talla
		v_aux['fecha'] = v.fecha_creacion.strftime("%D %H:%M")
		

		if v.confirmacion_de_pago == False:
			v_aux['confirmacion_de_pago'] = "Pendiente"
		else:
			v_aux['confirmacion_de_pago'] = "Confirmado"

		ventas.append(v_aux)
		v_aux = {}
	return HttpResponse(json.dumps(ventas), content_type= "application/json")
	
		

def cliente(request):
	if request.user.is_authenticated():
		usuario = request.user
	else:
		return redirect("/")

	

	cliente = Cliente.objects.filter(usuario = usuario)

	if(cliente):
		ventas = []
		v_aux = {}
		venta = Venta.objects.filter(cliente = cliente).order_by('-fecha_creacion')
		for  v in venta:
			v_aux['numero'] = v.id
			v_aux['tienda'] = v.tienda.nombre
			v_aux['producto'] = v.producto.nombre
			v_aux['talla'] = v.talla
			v_aux['fecha'] = str(v.fecha_creacion.strftime("%D %H:%M"))
			if v.confirmacion_de_pago == False:
				v_aux['estado'] = "Pendiente"
			else:
				v_aux['estado'] = "Confirmado"
			
			ventas.append(v_aux)
			v_aux = {}

		print venta
		return HttpResponse(json.dumps(ventas), content_type= "application/json")
	else:
		return HttpResponse("cliente invalido")

def crear(request):

	if request.user.is_authenticated():
		usuario = request.user
	else:
		return redirect("/")

	cliente = Cliente.objects.filter(usuario = usuario)

	if(cliente):
		t = request.GET.get('tienda', False)
		p = request.GET.get('producto', False)
		pais = request.GET.get('pais', " ")
		ciudad = request.GET.get('ciudad', " ")
		direccion = request.GET.get('direccion', " ")
		telefono = request.GET.get('direccion', " ")


		#inicio creando perfil del cliente

		try:
			perfil = PerfilCliente.objects.get(usuario = usuario)

			perfil.usuario = usuario
			perfil.pais = pais
			perfil.ciudad = ciudad
			perfil.direccion = direccion
			perfil.telefono = telefono
			perfil.save()

		except PerfilCliente.DoesNotExist:
			perfil = PerfilCliente()
			perfil.usuario = usuario
			perfil.pais = pais
			perfil.ciudad = ciudad
			perfil.direccion = direccion
			perfil.telefono = telefono
			perfil.save()

		#fin creando perfil del cliente

		talla = request.GET.get('talla', False)

		tienda = Tienda.objects.filter(id = t)

		try:
			producto = Producto.objects.get(id = p)

		except Producto.DoesNotExist:
			return HttpResponse("Este producto no existe")

		#inicio validacion de disponibilidad

		try:
			inventario = Inventario.objects.get(producto = producto, talla__numero = talla )
			cantidad_actual = inventario.cantidad_disponible

			if cantidad_actual == 0:
				return HttpResponse('Talla agotada')

			inventario.cantidad_disponible = cantidad_actual-1
			inventario.save()
			try:
				venta = Venta()
				venta.cliente = cliente[0]
				venta.tienda = tienda[0]
				venta.producto = producto
				venta.talla = talla
				venta.save()
				return HttpResponse("venta creada con exito")

			except Exception as e:
				return HttpResponse("error creando venta "+str(e.args) )
			
		except Inventario.DoesNotExist:
			return HttpResponse('Talla agotada' )
		#fin validacion de disponibilidad
		
		
		
		
	else:
		return HttpResponse("cliente invalido")





from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from registros.models import Categoria, Producto, Tienda, Cliente, PerfilCliente
from registros.models import Talla
from django.db.models import Q
import json


# Create your views here.

def bautizar(request):
	tienda = request.POST.get('tienda', False)
	if tienda:
		t = Tienda.objects.filter(Q(usuario = request.user) | Q(nombre = tienda))
		if len(t):
			error = 'YA EXISTE UNA TIENDA CON ESTE NOMBRE'

			return render(request,'tienda/bautizar.html', {'error':error})
		else:
			t = Tienda()
			t.nombre = tienda
			t.usuario = request.user
			t.save()
			return redirect('/tienda/incluir/producto/')

	if request.user.id == None:	
		return HttpResponse("usuario no autenticado")
	else:
		tienda = Tienda.objects.filter(usuario = request.user)	
		if len(tienda):
			return redirect('/tienda/incluir/producto/')
		else:
			return render(request,'tienda/bautizar.html')

def validar(request):
	if request.user.id == None:	
		return HttpResponse("usuario no autenticado")
	else:
		tienda = Tienda.objects.filter(usuario = request.user)	
		if len(tienda):
			return HttpResponse('Este usuario ya tiene tienda')	
		else:
			return redirect('/tienda/bautizar/')
		

def incluir_producto(request):
	
	categorias = []
	categoria = {}
	producto = {}
	for c in Categoria.objects.all():
		categoria['id'] = c.id
		categoria['nombre'] = c.nombre
		categoria['productos'] = []
		categoria['imagen'] = c.imagen
		productos = Producto.objects.filter(categoria_id = c.id)
		for p in productos:
			producto['id'] = p.id
			producto['nombre'] = p.nombre
			producto['descripcion'] = p.descripcion
			producto['valor'] = p.valor
			producto['peso'] = p.peso
			producto['imagen'] = p.imagen_principal
			#print producto
			categoria['productos'].append(producto)
			producto = {}
			
		categorias.append(categoria)
		categoria = {}
			
	
	return render(request, 'tienda/incluir_producto.html', {'categorias' : categorias})




def ver_tienda(request, nombre):
	if request.user.id == None:	
		pass
	else:
		cliente = Cliente.objects.filter(usuario = request.user)
		if len (cliente):
			pass
		else:
			cliente = Cliente()
			cliente.usuario = request.user
			cliente.save()

	tienda = Tienda.objects.filter(nombre = nombre)
	categorias = Categoria.objects.all()
	
	if len(tienda):	
		#buscando tallas existentes
		tallas = Talla.objects.all()


		
		try:
			perfil = PerfilCliente.objects.get(usuario = request.user)
			return render(request, 'tienda/ver_tienda.html', {'tallas':tallas, 'perfil':perfil, 'nombre':tienda[0].nombre, 'tienda':tienda[0].id, 'categorias': categorias, 'productos': tienda[0].productos.all()})
		except Exception as e :
			return render(request, 'tienda/ver_tienda.html', {'tallas':tallas, 'nombre':tienda[0].nombre, 'tienda':tienda[0].id, 'categorias': categorias, 'productos': tienda[0].productos.all()})
	else:
		return redirect('/')

		
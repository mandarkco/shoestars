from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import redirect
from registros.models import Tienda, Cliente
import pymongo
# Create your views here.



def ingresar(request):
	return render(request, 'login/ingresar.html')

def correo(request):
	return render(request, 'login/correo.html')

def tipo_registro(request):
	return render(request, 'login/tipo_registro.html')


@csrf_exempt
def crear_cliente(request):

	correo = request.GET.get("correo", False)
	password = request.GET.get("password", False)
	#return HttpResponse(correo)
	path = request.POST.get("path", False)
	u = User.objects.filter(username = correo)
	if len(u):
		return HttpResponse("este usuario ya existe")
	else:
		user = User.objects.create_user(correo, '', password)
		cliente = Cliente()
		cliente.usuario = user
		cliente.save()
		u = authenticate(username = correo, password = password)
		login_django(request, u)
		return HttpResponse("ok")
	

	

@csrf_exempt
def crear(request):
	
	
	correo = request.POST.get("correo", False)
	password = request.POST.get("password", False)
	tienda = request.POST.get("tienda", False)

	t = Tienda.objects.filter(nombre = tienda)
	
	if len(t):
		return HttpResponse("esta tienda ya existe")

	u = User.objects.filter(username = correo)

	if len(u):
		return HttpResponse("este usuario ya existe")
	else:
		

		user = User.objects.create_user(correo, '', password)
		
		t = Tienda()
		t.nombre = tienda
		t.usuario = user
		t.save()		
		u = authenticate(username = correo, password = password)
		login_django(request, u)
		return redirect('/tienda/incluir/producto/')
	
def autenticar_cliente(request):
	usuario = request.GET.get('correo', ' ')
	password = request.GET.get('password', ' ')
	
	user = authenticate(username = usuario, password = password)

	if user is not None:
		if user.is_active:					
					
			login_django(request, user)				
			return HttpResponse("ok")
			
			
		else:
			return HttpResponse("usuario inactivo")
	else:
		return HttpResponse("Usuario o password incorrectos")


@csrf_exempt
def autenticar(request):
	usuario = request.POST.get('correo', ' ')
	password = request.POST.get('password', ' ')
	user = authenticate(username = usuario, password = password)

	if user is not None:
		if user.is_active:					
					
			login_django(request, user)				
			return redirect('/tienda/incluir/producto/')	
			
			
		else:
			return HttpResponse("usuario inactivo")
	else:
		return HttpResponse("Usuario o password incorrectos")

def salir(request):
	logout(request)
	return redirect('/')

def login_fb(request):
	return render(request, 'login/redirect.html')
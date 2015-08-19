from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'administracion/index.html')

def categorias(request):
	return render(request, 'administracion/categorias.html')

def productos(request):
	return render(request, 'administracion/productos.html')
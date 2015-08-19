from django.shortcuts import render

# Create your views here.

def slider(request):
	return render(request, 'directivas/slider.html')

def visualizar_productos(request):
	return render(request, 'directivas/visualizar_productos.html')

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tienda(models.Model):
	nombre = models.CharField(max_length=50,  blank = True, null = True)
	usuario = models.ForeignKey(User, null = True,  blank = True)	
	productos =  models.ManyToManyField('Producto', null = True,  blank = True)
	def __unicode__(self):
		return self.nombre

class Venta(models.Model):
	cliente = models.ForeignKey('Cliente')
	tienda = models.ForeignKey('Tienda')
	producto = models.ForeignKey('Producto')	
	talla = models.CharField(max_length=100, blank = True, null = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	confirmacion_de_pago = models.BooleanField(default = False)
	

	def __unicode__(self):
		return self.cliente.usuario.username

class Perfil_Vendedor(models.Model):
	usuario = models.ForeignKey(User, null = True,  blank = True)
	tienda = models.ForeignKey('Tienda',  blank = True, null = True)
	Titular_cuenta_bancaria = models.CharField(max_length=100, blank = True, null = True)
	banco = models.CharField(max_length=50, blank = True, null = True)
	numero_cuenta = models.CharField(max_length=50, blank = True, null = True)
	pais = models.CharField(max_length=50, blank = True, null = True)
	ciudad = models.CharField(max_length=50, blank = True, null = True)

	def __unicode__(self):
		return str(self.usuario)

class PerfilCliente(models.Model):
	usuario = models.ForeignKey(User, null = True,  blank = True)	
	pais = models.CharField(max_length=100, blank = True, null = True)
	ciudad = models.CharField(max_length=50, blank = True, null = True)
	direccion = models.CharField(max_length=50, blank = True, null = True)
	telefono = models.CharField(max_length=50, blank = True, null = True)
	

	def __unicode__(self):
		return str(self.usuario.username)

class Cliente(models.Model):
	usuario = models.ForeignKey(User, null = True,  blank = True)	
	pais = models.CharField(max_length=100, blank = True, null = True)
	ciudad = models.CharField(max_length=100, blank = True, null = True)
	direccion = models.CharField(max_length=100, blank = True, null = True)
	telefono = models.CharField(max_length=100, blank = True, null = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)	
	
	def __unicode__(self):
		return str(self.usuario)

class Categoria(models.Model):
	nombre = models.CharField(max_length=50, blank = True, null = True)
	

	def __unicode__(self):
		return str(self.nombre)



class Producto(models.Model):
	nombre = models.CharField(max_length=50, blank = True, null = True)
	imagen_principal = models.ImageField(upload_to='images')
	imagen_1 = models.ImageField(upload_to='images')
	imagen_2 = models.ImageField(upload_to='images')
	imagen_3 = models.ImageField(upload_to='images')
	descripcion = models.TextField(max_length=500, blank = True, null = True)
	categoria = models.ForeignKey('Categoria')
	valor = models.IntegerField( blank = True, null = True)
	peso = models.IntegerField( blank = True, null = True)
	disponible = models.BooleanField(default = False)
	


	def __unicode__(self):
		return str(self.nombre)



class Talla(models.Model):	
	numero =  models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.numero)

class Inventario(models.Model):
	nombre = models.CharField(max_length=50)
	producto = models.ForeignKey('Producto')
	talla = models.ForeignKey('Talla')
	cantidad_disponible = models.IntegerField( )

	def __unicode__(self):
		return str(self.nombre)







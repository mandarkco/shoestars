from django.http import HttpResponse
import json
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from registros.models import Tienda, Producto
import pymongo
from django.http import JsonResponse

servidor = pymongo.MongoClient('localhost', 27017)
database = servidor.shoe_starts2




class ProductoList(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProductoList, self).dispatch(*args, **kwargs)

    def get(self, request):
    	data = []    	
    	#print productos
    	for p in database.producto.find({}, {'_id':0}):
    		data.append(p)
    		print p

    	print data
        return HttpResponse(json.dumps(data),	 content_type='application/json')

    
    def post(self, request):
        data = json.loads(request.body)
        categoria = data["categoria"]
        data.pop("categoria", None)

        #return HttpResponse(json.dumps(data), content_type= "application/json")
    	try:
    		
    		database.categoria.update({'nombre': str(categoria) }, { '$push': { 'productos': data } } )
    	except :
    		return HttpResponse( {"error" : "no se pudieron ingresar los datos"}, content_type  = 'application/json')
    	return HttpResponse(json.dumps(request.body), content_type= "application/json")

class ProductoDetail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProductoDetail, self).dispatch(*args, **kwargs)

    def get(self, request, categoria):

    	data = []    	
    	#print productos
    	for p in database.producto.find({'categoria': categoria}, {'_id':0}):
    		data.append(p)
    		print p

    	print data
        return HttpResponse(json.dumps(data),	 content_type='application/json')

class CategoriaList(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaList, self).dispatch(*args, **kwargs)

    def get(self, request):
    	data = []    	
    	#print productos
    	for p in database.categoria.find({}, {'_id':0}).sort( "nombre",pymongo.ASCENDING ):
    		data.append(p)
    		

    	
        return HttpResponse(json.dumps(data),	 content_type='application/json')

    
    def post(self, request):

    	try:
    		
    		data = json.loads(request.body)
    		data["id"] = database.categoria.count() 

    		database.categoria.insert(data)

    	except :
    		return HttpResponse( {"error" : "no se pudieron ingresar los datos"}, content_type  = 'application/json')

        return HttpResponse(json.dumps(request.body), content_type  = 'application/json')

class TiendaDetail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TiendaDetail, self).dispatch(*args, **kwargs)

    def get(self, request, usuario):   	
    	tienda = database.tienda.find_one({'usuario': int(usuario) } , {'_id':0})
    	
        return HttpResponse(json.dumps(tienda),	 content_type='application/json')


class CategoriaDetail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CategoriaDetail, self).dispatch(*args, **kwargs)

    def get(self, request, categoria):    
        data = database.categoria.find_one({'id': int(categoria) }, {'_id':0})
        
        return HttpResponse(json.dumps(data),  content_type='application/json')

    def delete(self, request, categoria):    
        database.categoria.remove({'id': int(categoria) })
        
        return HttpResponse(json.dumps({'error':'0'}),  content_type='application/json')

    def put(self, request, categoria): 
        data = json.loads(request.body)   
        database.categoria.update({'id': int(categoria) }, {'$set': data})
        
        return HttpResponse(json.dumps({'error':'0'}),  content_type='application/json')



def agregar_producto_tienda(request):
    id = request.GET.get("producto", False)
    #producto = Producto.objects.filter(id = id)    
    tienda = Tienda.objects.filter(usuario = request.user , productos__id = int(id))

    if len(tienda):
        
        return HttpResponse("producto ya incluido")
    else:
        tienda = Tienda.objects.filter(usuario = request.user)
        producto = Producto.objects.filter(id = id)

        tienda[0].productos.add(producto[0])
        return HttpResponse("producto incluido con exito")



    return HttpResponse(id)
    return HttpResponse(json.dumps({'error':'400', 'descripcion': 'producto no enviado'}), content_type="application/json")



		




// Creación del módulo
var app = angular.module('app', ['ngRoute']);


app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});





// Configuración de las rutas
app.config(function($routeProvider) {

	$routeProvider
		.when('/', {
			templateUrl	: '/administracion/categorias/',
			controller 	: 'categoriasController'
		})
		.when('/categorias/', {
			templateUrl : '/administracion/categorias/',
			controller 	: 'categoriasController'
		})
		.when('/productos/', {
			templateUrl : '/administracion/productos/',
			controller 	: 'productosController'
		})
		.otherwise({
			redirectTo: '/'
		});
});


app.controller('categoriasController', ['$scope', 'defaultService', function ($scope, defaultService) {
	console.log('controlador categorias');
	function cargar_categorias(){
		defaultService.get('/services/categoria/list/',function(d){
	           //console.log(d)
	           $scope.categorias = d;
	           console.log(d);
	        }, function (e){console.log(e)
	    });
	}

	cargar_categorias();

	$scope.set_atributos = function( id, nombre ){
		$scope.id = id;
		$scope.update_nombre = nombre ;


	}
	

	$scope.agregar_categoria = function(){
		//alert("agregando categorias");
		data = {};
		data.nombre = $("#nombre").val()
		defaultService.post('/services/categoria/list/',data, function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_categorias();
	        }, function (e){console.log(e)
	    });
	}

	$scope.eliminar_categoria = function(id){
		defaultService.delete('/services/categoria/detail/'+id+'/', function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_categorias();
	        }, function (e){console.log(e)
	    });
	}

	$scope.actualizar_categoria = function(){
		data = {};
		data.nombre = $("#update-nombre").val()
		defaultService.put('/services/categoria/detail/'+$scope.id+'/',data, function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_categorias();
	        }, function (e){console.log(e)
	    });
	}
	

}]);

app.controller('productosController', ['$scope', 'defaultService', function ($scope, defaultService) {
	console.log('controlador productos');
	function cargar_productos(){
		defaultService.get('/services/categoria/list/',function(d){
	           //console.log(d)
	           $scope.categorias = d;
	           console.log(d);
	        }, function (e){console.log(e)
	    });
	}

	cargar_productos();

	$scope.set_atributos = function( id, nombre ){
		$scope.id = id;
		$scope.update_nombre = nombre ;


	}
	

	$scope.agregar_producto = function(){
		//alert("agregando categorias");
		data = {};
		data.categoria = $("#categoria").val()
		data.nombre = $("#nombre").val()
		data.imagen = $("#imagen").val()
		data.precio = $("#precio").val()
		data.peso = $("#peso").val()
		data.descripcion = $("#descripcion").val()
		console.log(data);
		defaultService.post('/services/producto/list/',data, function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_productos();
	        }, function (e){console.log(e)
	    });
	}

	$scope.eliminar_categoria = function(id){
		defaultService.delete('/services/categoria/detail/'+id+'/', function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_categorias();
	        }, function (e){console.log(e)
	    });
	}

	$scope.actualizar_categoria = function(){
		data = {};
		data.nombre = $("#update-nombre").val()
		defaultService.put('/services/categoria/detail/'+$scope.id+'/',data, function(d){
	           //console.log(d)
	           
	           console.log(d);
	           cargar_categorias();
	        }, function (e){console.log(e)
	    });
	}
	

}]);
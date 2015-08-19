app.controller('startApp', ['$scope', 'defaultService', function ($scope, defaultService) {
 console.log("start"); 
 //$('#manual').modal('show');
 $scope.version ="1.0";  
 $scope.usuario = $("#usuario").val(); 
 console.log(window.location.pathname)
 

 $scope.vista2 = function(){
 	$(".vista2").css({display: "block"})
 	$(".vista1").css({display: "none"})
 }

  $scope.vista1 = function(){
 	$(".vista1").css({display: "block"})
 	$(".vista2").css({display: "none"})
 }

$scope.buscar_categoria = function(id){
	$(".Categoria-item").css({display: "none"})
	$("#"+id).css({display: "block"})

}

$scope.buscar_productos = function(id){
	$(".product").css({display: "none"})
	$("."+id).css({display: "block"})

}

$scope.mostrar_perfil_cliente = function(){
	defaultService.get('/venta/cliente/', function(d){
           //console.log(d)
           $scope.compras = d;
           console.log(d);
        }, function (e){console.log(e)
    });

	$("#perfil").modal('show');
}

$scope.mostrar_perfil_vendedor = function(){
	defaultService.get('/venta/vendedor/', function(d){
           //console.log(d)
           $scope.ventas = d;
           console.log(d);
        }, function (e){console.log(e)
    });

	$("#perfil").modal('show');
}


$scope.nuevo_cliente = function(){
	var correo = $("#n_correo").val();
	var password = $("#n_password").val();
	
	defaultService.get('/login/registro/crear/cliente/?correo='+correo+'&password='+password, function(d){
           //console.log(d)
           if(d == "ok") window.location = window.location.pathname;
           else alert(d)
        }, function (e){ console.log(e)
        	}
    );
	console.log(correo+password);
}

$scope.autenticar_usuario = function(){
	var correo = $("#a_correo").val();
	var password = $("#a_password").val();
	
	defaultService.get('/login/registro/autenticar/cliente/?correo='+correo+'&password='+password, function(d){
           //console.log(d)
           if(d == "ok") window.location = window.location.pathname;
           else alert(d)
        }, function (e){ console.log(e)
        	}
    );
	console.log(correo+password);
}



$scope.agregar_producto = function(id){
	
	defaultService.get('/services/tienda/agregar/producto/?producto='+id, function(d){
           //console.log(d)
           alert(d)
           console.log(d);
        }, function (e){console.log(e)
    });
}

$scope.set_producto = function(nombre, imagen, imagen_1, imagen_2, imagen_3, tienda, product_id, user){

	if(String(user) === 'None' ) 
	{
		$('#perfil').modal('show')
	}
	else
	{
		$scope.nombre_producto = nombre;
		$scope.tienda = tienda;
		$scope.imagen = imagen;
		$scope.imagen_1 = imagen_1;
		$scope.imagen_2 = imagen_2;
		$scope.imagen_3 = imagen_3;
		$scope.product_id = product_id;
		console.log(tienda)
		console.log(product_id)
		$('#checkout').modal('show')
	}
	
}

$scope.mostrar_pago = function(){	
	$(".pago").css({display: "block"})
}



$scope.pagar = function(){
	
	
	var talla = $("#talla").val();
	var pais = $("#pais").val();
	var ciudad = $("#ciudad").val();
	var direccion = $("#direccion").val();
	var telefono = $("#telefono").val();

	defaultService.get('/venta/crear/?tienda='+$scope.tienda+'&producto='+
			$scope.product_id+'&talla='+talla+'&pais='+pais+'&ciudad='+ciudad
			+'&direccion='+direccion+'&telefono='+telefono, function(d){
           //console.log(d)
           alert(d)
           console.log(d);
           defaultService.get('/venta/cliente/', function(d){
           //console.log(d)
		           $scope.compras = d;
		           console.log(d);
		           $("#checkout").modal('hide');
		           $("#perfil").modal('show');

		        }, function (e){console.log(e)
		    });
        }, function (e){console.log(e)
    });


}


}]);






app.controller('slide_incluir_producto', ['$scope', 'defaultService', function ($scope, defaultService) {

	$scope.items = [
						{
							'titulo': 'slide 1',
							'subtitulo':'subtitulo 1',
							'text_btn': 'txt btn 1',
							'clase' : 'active',
							'img': 'https://animostyle.files.wordpress.com/2012/11/lace-collage.jpg',
						},
						{
							'titulo': 'slide 2',
							'subtitulo':'subtitulo 2',
							'text_btn': 'txt btn 2',
							'img': 'https://artbecomesyou.files.wordpress.com/2011/06/colour-blocking1.jpg?w=1200&h=400&crop=1',
						},

						{
							'titulo': 'slide 3',
							'subtitulo':'subtitulo 3',
							'text_btn': 'txt btn 3',
							'img': 'http://carriebradshawlied.com/wp-content/uploads/2015/02/pink-1200x400.png',
						},

						
						
					];

	


}]);
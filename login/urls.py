from django.conf.urls import include, url


urlpatterns = [
   
    url(r'^registro/correo/$', 'login.views.correo' ),
    url(r'^registro/$', 'login.views.tipo_registro' ),
    url(r'^registro/crear/$', 'login.views.crear' ),
    url(r'^registro/crear/cliente/$', 'login.views.crear_cliente' ),
    url(r'^registro/autenticar/cliente/$', 'login.views.autenticar_cliente' ),
    url(r'^ingresar/$', 'login.views.ingresar' ),
    url(r'^registro/autenticar/$', 'login.views.autenticar' ),
    
     url(r'^salir/$', 'login.views.salir'),
] 
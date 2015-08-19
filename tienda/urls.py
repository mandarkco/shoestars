from django.conf.urls import include, url


urlpatterns = [
   
    url(r'^incluir/producto/$', 'tienda.views.incluir_producto' ), 
    url(r'^validar/$', 'tienda.views.validar' ),
    url(r'^bautizar/$', 'tienda.views.bautizar' ),  
    url(r'^(?P<nombre>.+)/$', 'tienda.views.ver_tienda' ),
] 
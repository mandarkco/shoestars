from django.conf.urls import include, url


urlpatterns = [   
    url(r'^crear/$', 'venta.views.crear' ), 
    url(r'^cliente/$', 'venta.views.cliente' ),
    url(r'^vendedor/$', 'venta.views.vendedor' ),     
] 
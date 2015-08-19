from django.conf.urls import include, url


urlpatterns = [
   
    url(r'^$', 'administracion.views.index' ),
    url(r'^categorias/$', 'administracion.views.categorias' ),
    url(r'^productos/$', 'administracion.views.productos' ),
    
] 
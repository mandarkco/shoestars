from django.conf.urls import include, url


urlpatterns = [
   
    url(r'^slider/$', 'directivas.views.slider' ),
    url(r'^visualizar/productos/$', 'directivas.views.visualizar_productos' )
] 
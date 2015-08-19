from django.conf.urls import include, url
from services.views import ProductoList, ProductoDetail, CategoriaList, TiendaDetail, CategoriaDetail

urlpatterns = [
   
    #url(r'^producto/list/', ProductoList.as_view()),
    #url(r'^producto/detail/(?P<categoria>.+)/$', ProductoDetail.as_view()),

    #url(r'^tienda/detail/(?P<usuario>.+)/$', TiendaDetail.as_view()),   
    url(r'^tienda/agregar/producto/$', 'services.views.agregar_producto_tienda'),
    #url(r'^categoria/list/', CategoriaList.as_view()),
    #url(r'^categoria/detail/(?P<categoria>.+)/$', CategoriaDetail.as_view()), 

] 
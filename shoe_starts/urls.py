"""shoe_starts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'login.views.ingresar'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/', include('login.urls')),
    url(r'^tienda/', include('tienda.urls')),
    url(r'^venta/', include('venta.urls')),    
    url(r'^directivas/', include('directivas.urls')),
    url(r'^administracion/', include('administracion.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^fb/$', 'login.views.login_fb' ),
    url(r'', include('social_auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "embriologia"

urlpatterns = [	
    url(r'^lista$', views.lista, name='lista'),
    url(r'^$', views.index, name='index'), 
    url(r'^lista_fetos$', views.lista_fetos, name='lista_fetos'),
    url(r'^ver/([0-9]+)/$', views.ver, name='ver'),
    url(r'^mostrar/([0-9]+)$', views.mostrar, name='mostrar'),
]
from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "embriologia"

urlpatterns = [	
    url(r'^lista$', views.lista, name='lista'),
    url(r'^$', views.index, name='index'), 
]
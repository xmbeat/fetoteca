from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = "usuarios"

urlpatterns = [	
    url(r'^$', views.list, name='list'),
]

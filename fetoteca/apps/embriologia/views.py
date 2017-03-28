
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Feto, Malformacion, ImagenFeto
# Create your views here.
def lista(request):
	context = {}
	context['breadcrumb'] = [ ("Home",reverse("embriologia:index")) ,("Embriones",reverse("embriologia:lista")) ]
	context['fetos'] = Feto.objects.all()
	return render(request,'lista.html',context)

def index(request):
	context = {}
	return render (request,'index.html',context)

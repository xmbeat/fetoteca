
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Feto, Malformacion, ImagenFeto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #puesto por xaco
from pprint import pprint

# Create your views here.
def lista(request):
	context = {}
	context['breadcrumb'] = [ ("Home",reverse("embriologia:index")) ,("Embriones",reverse("embriologia:lista")) ]
	context['fetos'] = Feto.objects.all()
	return render(request,'lista.html',context)

def index(request):
	context = {}
	return render (request,'index.html',context)

#puesto por xaco
def lista_fetos(request):
    fetos_lista = Feto.objects.all()
    paginator = Paginator(fetos_lista, 1) 
    pagina = request.GET.get('page')#incluir parametro en template

    try:
        fetos = paginator.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        fetos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        fetos = paginator.page(paginator.num_pages)
    
    rango=range(1,paginator.num_pages+1)
    return render(request, 'lista.html', {'fetos': fetos,'rango':rango})

def ver(request,id):
    pass

def mostrar(request, fetoId):
    context = {}
    context['feto']= Feto.objects.get(id=fetoId)
    context['malformaciones'] = Malformacion.objects.all()
    return render(request, 'mostrar.html', context)

def mostrarAdmin(request, fetoId):
    context = {}
    context['feto']= Feto.objects.get(id=fetoId)
    context['malformaciones'] = Malformacion.objects.all()
    return render(request, 'mostrarAdmin.html', context)
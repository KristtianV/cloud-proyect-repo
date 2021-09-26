from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('¡¡¡HOLA MUNDO!!!')

def categorias_view(request):
    return render(request, 'app/categorias.html')

def categoria_view(request, id):
    contexto={
        'actor':'jack Nicolson',
        'esJubilado':True,
        'filmografia':[
            {'titulo':'naufrago','year':2021},
            {'titulo':'otra','year':2020},
            {'titulo':'poulfiction','year':2022},
        ]
    }
    return render(request,'app/categoria.html',contexto)

def peliculas_view(request):
    return render(request,'app/peliculas.html')


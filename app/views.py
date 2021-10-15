from typing import TypeVar
from django.http.response import  HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Partido, Individuo
import time


# Create your views here.

# INICIAR SESION
def login_view(request):
    return render(request,'app/login.html')  
def login_post(request):
    #obtener los datos del formulario
    username = request.POST['username']
    password = request.POST['password']

    #obtener el usuario
    user = authenticate(username=username,password=password)

    if user is None:
        return HttpResponse("Error: el usuario no existe")
    else:
        #inicia sesion
        login(request, user)
        return redirect('app:index')

#CREAR USUARIO
def startup_view(request):
    return render(request,'app/startup.html')
def startup_post(request):
    #obtiene datos del formulario"
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    name = request.POST['name']
    lastname = request.POST['lastname']
    # Verifica si existe
    if User.objects.filter(username=username).exists():
        return HttpResponse("Error:El nombre de usuario ya existe")
    elif User.objects.filter(email=email).exists():
        return HttpResponse("Error:El correo ya existe")
    else:  
        #crea el usuario
        user=User()
        user.username = username
        user.set_password(password)
        user.email = email
        user.first_name = name
        user.last_name = lastname
        user.save()
        return redirect('app:login_view')

#EDITAR PERFIL
@login_required
def editProfile_view(request):
    return render(request,'app/editProfile.html')
def editProfile_post(request):
    #usuario actual
    userToMod=User.objects.get(id=request.user.id)
    u=request.user.username
    e=request.user.email
    p=request.user.password

    #obtiene datos del formulario"
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    name = request.POST['name']
    lastname = request.POST['lastname']
    
    # Verifica si existe el username
    if User.objects.filter(username=username).exists(): 
        if u != username: #existe y no es del usuario actual
            return HttpResponse("Error:El nombre de usuario ya existe")
    else:#Si no existe
        userToMod.username = username

    # Verifica si existe el email
    if User.objects.filter(email=email).exists(): 
        if e != email: #existe y no es del usuario actual
            return HttpResponse("Error:El correo ya existe")
    else:#Si no existe
        userToMod.email = email   
    
    if p != password: #si lo modifico
        userToMod.set_password(password)

    userToMod.last_name = lastname
    userToMod.first_name = name

    userToMod.save()
    
    return redirect('app:index')

#INDEX
@login_required
def index_view(request):
    return render(request,'app/index.html')

#CERRAR SESION
def logout_(request):
    #cierra la sesion activa
    logout(request)
    return redirect('app:login_view')

#CREAR PARTIDO
def creaPart_view(request):
    
    return render(request,'app/creaPart.html')

def creaPart_post(request):
    #obtengo los datos del formulario
    nameP = request.POST['nameP']
    views = 0
    id_User = request.user.id
    #Obtiene el User creador
    creator = User.objects.get(id=id_User)
    #Crea el partido
    p=Partido()
    p.nameP = nameP
    p.views = views
    p.creator= creator
    p.save()   
    
    return redirect('app:consPart_view')

#CONSULTAR LISTA DE PARTIDO
def consPart_view(request):
    lista = Partido.objects.all()
    contexto = {
        'partidos':lista 
    }
    return render(request, 'app/consPart.html', contexto)

#CREAR INDIVIDUO
def creaIndiv_view(request):
    return render(request,'app/creaIndiv.html')
def creaIndiv_post(request):
    #obtengo los datos del formulario
    indiv_lastname = request.POST['indiv_lastname']
    indiv_name = request.POST['indiv_name']
    birthday = request.POST['birthday']
    #Obtiene el User creador
    id_User = request.user.id
    creator = User.objects.get(id=id_User)
    #Inicializo el contador de vistas y la bandera de activo
    views = 0
    active  = False

    i=Individuo()
    i.indiv_lastname = indiv_lastname
    i.indiv_name = indiv_lastname
    if birthday:
        i.birthday = birthday
    i.creator = creator
    i.views = views
    i.active = active
    i.save()
    
    return redirect('app:index')
    
from django.http.response import  HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# Iniciar sesion
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

#Crear usuario
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

#editar perfil
@login_required
def editProfile_view(request):
    return render(request,'app/editProfile.html')
def editProfile_post(request):
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
        #editar el usuario
        return HttpResponse("editado")

#Index
@login_required
def index_view(request):
    return render(request,'app/index.html')

#logout
def logout_(request):
    #cierra la sesion activa
    logout(request)
    return redirect('app:login_view')
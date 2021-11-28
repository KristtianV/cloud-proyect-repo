from typing import TypeVar
from django.http.response import  HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Afiliacion, Implicado, Partido, Individuo, Proceso


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
        user.is_active=0
        user.username = username
        user.set_password(password)
        user.email = email
        user.first_name = name
        user.last_name = lastname
        user.save()
        return redirect('app:login_view')

#HBILITAR CIUDADANO
@login_required
def habiCiuda_view(request):
    #obtengo lista de usuarios
    lista = User.objects.all().order_by('is_active')
    contexto = {
        'users':lista 
    }
    return render(request,'app/habiCiuda.html', contexto)
def habiCiuda_post(request):
    id_User = request.POST['id']
    user=User.objects.get(id=id_User)
    if user.is_active == 0:
        user.is_active=1
    else:
        user.is_active=0
    user.save()
    return redirect('app:habiCiuda_view')

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
@login_required
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

#CONSULTAR LISTA DE PARTIDOS
@login_required
def consPart_view(request):
    lista_afil=[]
    lista_impl=[]
    lista=[]
    # Obtengo el parido
    lista_part = Partido.objects.all()
    # Recorro la lista de partidos
    for part in lista_part:
        #inicio contador
        cont=0
        #obtengo lista de afiliacions del partido
        lista_afil=Afiliacion.objects.filter(part_id_id=part.id)
        #recorro las afiliaciones
        for afil in lista_afil:
            print(afil)
            #obtengo la lista de implicados de cada afiliacion
            lista_impl=Implicado.objects.filter(afiliado_id=afil.id)
            cont=cont+len(lista_impl)
        
        lista.append({
            'partido':part,
            'how':cont
        })
    contexto = {
        'lista':lista,
    }
    return render(request, 'app/consPart.html', contexto)

#CONSULTAR UN PARTIDO
@login_required
def consAPart_view(request,id):
    lista_indv=[]
    #obtengo el partido
    partido = Partido.objects.get(id=id)
    #obtengo las afiliaciones
    afiliacion = Afiliacion.objects.filter(part_id_id=id)
    #Recorre cada afiliacion
    for afiliado in afiliacion:
        if afiliado.active:
            lista_indv.append({
                'date_in': afiliado.date_in,
                'date_out': afiliado.date_out,
                'indiv_name': Individuo.objects.get(id=afiliado.indiv_id_id).indiv_name,
                'indiv_lastname': Individuo.objects.get(id=afiliado.indiv_id_id).indiv_lastname,
                'indiv_id':afiliado.indiv_id_id
            })

    #inicio contadores
        cont=0
        cont_c=0
    #obtengo lista de afiliacions del partido
    lista_afil=Afiliacion.objects.filter(part_id_id=id)
    #recorro las afiliaciones
    for afil in lista_afil:
        #obtengo la lista de implicados de cada afiliacion
        lista_impl=Implicado.objects.filter(afiliado_id=afil.id)
        cont=cont+len(lista_impl)
        for impl in lista_impl:
            if impl.guilty == 1:
                cont_c=cont_c+1
    print(cont_c)
    contexto = {
        'procesos':cont,
        'procesos_c':cont_c,
        'info':partido,
        'lista_indv':lista_indv
    }
    #aumento el numero de vistas
    partido.views = partido.views + 1
    #guardo los cambios
    partido.save()

    return render(request, 'app/consAPart.html', contexto)

#CREAR INDIVIDUO
@login_required
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
    if request.user.is_superuser == 0:
        active  = False
    else:
        active  = True
    #Creo el individuo
    i=Individuo()
    i.indiv_lastname = indiv_name
    i.indiv_name = indiv_lastname
    if birthday:
        i.birthday = birthday
    i.creator = creator
    i.views = views
    i.active = active
    i.save()
    return redirect('app:consIndiv_view')

#CONSULTAR INDIVIDUOS
@login_required
def consIndiv_view(request):
    lista_indv=[]
    if request.user.is_superuser:
        #si es root obtiene toda la lista
        lista = Individuo.objects.all()
    else:
        #si no filtra los activos
        lista = Individuo.objects.filter(active=1)
    
    for individuo in lista:
        if Afiliacion.objects.filter(indiv_id_id=individuo.id).exists():
            part= Afiliacion.objects.get(indiv_id_id=individuo.id)
            if part.active == 1:
                id_part=part.part_id_id
                partido = Partido.objects.get(id=id_part).nameP
            else:
                partido= "Sin Afiliacion"
        else:
            partido= "Sin Afiliacion"
        
        lista_indv.append({
            'id': individuo.id,
            'indiv_name':individuo.indiv_name,
            'indiv_lastname':individuo.indiv_lastname,
            'active':individuo.active,
            'lastPart': partido
        })

    contexto = {
            'individuos':lista_indv, 
        }
    return render(request, 'app/consIndiv.html',contexto)

#CONSULTAR UN INDIVIDUO
@login_required
def consAIndiv_view(request,id):
    lista_impl=[]
    if Afiliacion.objects.filter(indiv_id_id=id).exists():
        if Afiliacion.objects.get(indiv_id_id=id).active==True:
            afiliacion =  Afiliacion.objects.get(indiv_id_id=id)
            partido = Partido.objects.get(id=afiliacion.part_id_id)
            print(".....",afiliacion.id)
        else:
            afiliacion={}
            partido={}
    else:
        afiliacion={}
        partido={}
    #obtengo el individuo
    individuo = Individuo.objects.get(id=id)
    #aumento el numero de vistas
    individuo.views = individuo.views + 1
    #guardo los cambios
    individuo.save()
    #creo el contexto
    contexto = {
        'info':individuo,
        'afil': afiliacion,
        'part':  partido
    }
    return render(request, 'app/consAIndiv.html', contexto)

#APROBARINDIVIDUO
@login_required
def aproIndiv_post(request):
    id_indiv = request.POST['id']
    individuo=Individuo.objects.get(id=id_indiv)
    if individuo.active == 0:
        individuo.active=1
    else:
        individuo.active=0
    individuo.save()
    return redirect('app:consIndiv_view')

#AFILIAR INDIVIDUO A PARTIDO
def afilIndi_view(request,id):
    #obtengo el individuo
    individuo = Individuo.objects.get(id=id)
    #obtengo la lista de partidos
    partidos = Partido.objects.all()
    #creo el contexto
    contexto = {
        'individuo':individuo,
        'partidos':partidos 
    }
    return render(request, 'app/afilIndi.html', contexto)

def afilIndi_post(request):
    #obtengo los datos del formulario
    part_id = request.POST['part_id']
    indiv_id = request.POST['indiv_id']
    date_in = request.POST['date_in']
    date_out = request.POST['date_out']
    #Inicializo la bandera de activo
    if request.user.is_superuser == 0:
        active  = False
    else:
        active  = True
    #obtengo el individuo
    part_id_id = Partido.objects.get(id=part_id)
    indiv_id_id = Individuo.objects.get(id=indiv_id)

    a = Afiliacion()
    
    if date_in:
        a.date_in = date_in
    if date_out:
        a.date_out = date_out
    a.part_id_id = part_id_id.id
    a.indiv_id_id = indiv_id_id.id
    a.active = active
    a.save()
    return redirect('app:consIndiv_view')

#APROBAR AFILIACION
def aproAfil_view(request):
    lista = Afiliacion.objects.all()
    listaAfil=[]
    for afiliacion in lista:
        part=Partido.objects.get(id=afiliacion.part_id_id).nameP
        name=Individuo.objects.get(id=afiliacion.indiv_id_id).indiv_name
        lastname=Individuo.objects.get(id=afiliacion.indiv_id_id).indiv_lastname
        listaAfil.append({
            'id':afiliacion.id,
            'part':part,
            'name':name,
            'lastname':lastname,
            'active':afiliacion.active
        })
    contexto = {
        'afiliaciones':listaAfil 
    }
    return render(request, 'app/aproAfil.html',contexto)

def aproAfil_post(request):
    id_afil = request.POST['id']
    afiliacion=Afiliacion.objects.get(id=id_afil)
    if afiliacion.active == True:
         afiliacion.active=False
    else:
         afiliacion.active=True
    afiliacion.save()
    return redirect('app:aproAfil_view')


#CREAR PROCESO
@login_required
def creaPro_view(request):
    return render(request, 'app/creaPro.html')
def creaPro_post(request):
    #obtengo los datos del formulario
    title = request.POST['title']
    date_start = request.POST['date_start']
    date_end = request.POST['date_end']
    state = request.POST['state']
    entity = request.POST['entity']
    howmuch = request.POST['howmuch']
    comments = request.POST['comments']
    #Obtiene el User creador
    id_User = request.user.id
    creator = User.objects.get(id=id_User)
    #Inicializo el contador de vistas y la bandera de activo
    views = 0
    if request.user.is_superuser == 0:
        active  = False
    else:
        active  = True
    #Creo el proceso
    p=Proceso()
    p.title = title
    p.date_start = date_start
    if date_end:
        p.date_end = date_end
    if state == "on":
        p.state = 1
    else:
        p.state = 0
    p.entity = entity
    p.howmuch = howmuch
    p.comments = comments
    p.creator = creator
    p.views = views
    p.active = active
    p.save()
    return redirect('app:index')

#APROBAR PRECESO
@login_required
def aproPro_view(request):
    #obtengo lista de procesos
    lista = Proceso.objects.all()
    contexto = {
        'procesos':lista 
    }
    return render(request,'app/aproPro.html',contexto)
def aproPro_post(request):
    id_proceso = request.POST['id']
    proceso=Proceso.objects.get(id=id_proceso)

    if proceso.active == True:
        proceso.active=False
    else:
        proceso.active=True
    proceso.save()
    return redirect('app:aproPro_view')

#CONSULTAR UN PROCESO
def consApro_view(request,id):
    lista_afil=[]
    lista=[]
    #obtengo el proceso
    proceso = Proceso.objects.get(id=id)
    #aumento el numero de vistas
    proceso.views = proceso.views + 1
    #guardo los cambios
    proceso.save()
    #creo el contexto
    list_impl=Implicado.objects.filter(proceso_id=id)
    for impl in list_impl:
        lista_afil.append(Afiliacion.objects.get(id=impl.afiliado_id))
        for afil in lista_afil:
            indiv=Individuo.objects.get(id=afil.indiv_id_id)
            part=Partido.objects.get(id=afil.part_id_id)
            if impl.guilty == True:
                guilty = "Culpable"
            else:
                guilty = "Inocente"
            
        lista.append({
            'name':indiv.indiv_name,
            'lastname':indiv.indiv_lastname,
            'part':part.nameP,
            'date_imp':impl.date_imp,
            'charge':impl.charges,
            'guilty':guilty,
            'sentence':impl.sentence,
            'commnts':impl.commnts
        })
        print(lista)
    contexto = {
        'info':proceso,
        'lista':lista
    }
    return render(request, 'app/consApro.html', contexto)

#IMPLICAR UN INDIVIDUO DE PARTIDO
def ImplicarIndi_view(request,id):
    lista_indv=[]
    #obtengo el partido
    partido = Partido.objects.get(id=id)
    #obtengo lista de procesos
    lista_pro = Proceso.objects.all()
    #Obtengo las afiliaciones del partido
    afiliacion = Afiliacion.objects.filter(part_id_id=id)
    for afiliado in afiliacion:
        if afiliado.active:
            lista_indv.append({
                'indiv_name': Individuo.objects.get(id=afiliado.indiv_id_id).indiv_name,
                'indiv_lastname': Individuo.objects.get(id=afiliado.indiv_id_id).indiv_lastname,
                'afil_id':afiliado.id
            })
    #creo el contexto
    contexto = {
        'partido':partido,
        'procesos':lista_pro,
        'afiliados':lista_indv
    }
    return render(request, 'app/ImplicarIndi.html', contexto)

def ImplicarIndi_post(request):
    #obtengo los datos del formulario
    afiliado_id = request.POST['afil_id']
    proceso_id = request.POST['pro_id']
    date_imp = request.POST['date_imp']
    charges = request.POST['charges']
    guilty = request.POST['guilty']
    sentence = request.POST['sentence']
    commnts = request.POST['commnts']


    print("date",date_imp)

    i=Implicado()

    i.afiliado_id=afiliado_id
    i.proceso_id=proceso_id

    if guilty == "true":
        i.guilty=True
    else:
        i.guilty=False

    if date_imp:
        i.date_imp=date_imp
    if charges:
        i.charges=charges
    if sentence:
        i.sentence=sentence
    if commnts:
        i.commnts=commnts
    i.save()
    return redirect('app:consPart_view')

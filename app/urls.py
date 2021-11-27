from django.urls import path
from .import views

app_name = 'app'
urlpatterns = [

    #index
    path('',views.index_view, name='index'),
    
    #iniciar sesion
    path('login/',views.login_view, name='login_view'),
    path('login_post/',views.login_post, name='login_post'),
    #Cerrar sesion
    path('logout/',views.logout_, name='logout_'),
    
    #Crear usuario
    path('startup/',views.startup_view, name='startup_view'),
    path('startup_post/',views.startup_post, name='startup_post'),
    
    #Habilitar ciudadano
    path('habiCiuda',views.habiCiuda_view, name='habiCiuda_view'),
    path('habiCiuda_post',views.habiCiuda_post, name='habiCiuda_post'),

    #editar usuario
    path('editProfile',views.editProfile_view, name='editProfile_view'),
    path('editProfile_post',views.editProfile_post, name='editProfile_post'),
    
    #crear partido
    path('creaPart',views.creaPart_view, name='creaPart_view'),
    path('creaPart_post',views.creaPart_post, name='creaPart_post'),

    #consultar partidos
    path('consPart',views.consPart_view, name='consPart_view'),
    
    #consutar un partido
    path('consPart/<int:id>',views.consAPart_view, name='consAPart_view'),

    #crear individuo
    path('creaIndiv',views.creaIndiv_view, name='creaIndiv_view'),
    path('creaIndiv_post',views.creaIndiv_post, name='creaIndiv_post'),
    
    #consultar individuos
    path('consIndiv',views.consIndiv_view, name='consIndiv_view'),
    
    #consultar un individuo
    path('consIndiv/<int:id>',views.consAIndiv_view, name='consAIndiv_view'),
    
    #habilitar individuo
    path('aproIndiv_post',views.aproIndiv_post, name='aproIndiv_post'),

    #crear proceso
    path('creaPro',views.creaPro_view, name='creaPro_view'),
    path('creaPro_post',views.creaPro_post, name='creaPro_post'),
    
    #aprobar proceso
    path('aproPro',views.aproPro_view, name='aproPro_view'),
    path('aproPro_post',views.aproPro_post, name='aproPro_post'),

    #consultar un proceso
    path('consApro/<int:id>',views.consApro_view, name='consApro_view'),

    #afiliar individuo a partido
    path('afilIndi/<int:id>',views.afilIndi_view, name='afilIndi_view'),
    path('afilIndi_post',views.afilIndi_post, name='afilIndi_post'),
    
    #aprobar afiliacion
    path('aproAfil',views.aproAfil_view, name='aproAfil_view'),
    path('aproAfil_post',views.aproAfil_post, name='aproAfil_post'),

    #implicar individuo
    path('ImplicarIndi/<int:id>',views.ImplicarIndi_view, name='ImplicarIndi_view'),
    path('ImplicarIndi_post',views.ImplicarIndi_post, name='ImplicarIndi_post'),
]


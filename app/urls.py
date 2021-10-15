from django.urls import path
from .import views

app_name = 'app'
urlpatterns = [
    #iniciar sesion
    path('login/',views.login_view, name='login_view'),
    path('login_post/',views.login_post, name='login_post'),
    #Cerrar sesion
    path('logout/',views.logout_, name='logout_'),
    
    #Crear usuario
    path('startup/',views.startup_view, name='startup_view'),
    path('startup_post/',views.startup_post, name='startup_post'),

    #index
    path('',views.index_view, name='index'),

    #editar usuario
    path('editProfile',views.editProfile_view, name='editProfile_view'),
    path('editProfile_post',views.editProfile_post, name='editProfile_post'),
    
    #crear partido
    path('creaPart',views.creaPart_view, name='creaPart_view'),
    path('creaPart_post',views.creaPart_post, name='creaPart_post'),


]


from django.urls import path
from .import views

app_name = 'app'
urlpatterns = [
    path('',views.index, name='index'),
    #lista de categorias
    path('categorias/', views.categorias_view, name='categorias'),
    #Ver una sola categoria
    path('categorias/<int:id>', views.categoria_view, name='categoria'),
    path('peliculas/', views.peliculas_view, name='peliculas'),
]

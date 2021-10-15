from django.contrib.auth.models import User
from django.db import models

class Partido(models.Model):
    nameP = models.CharField(max_length=200 , null= False)
    views = models.IntegerField(null= False)
    creator = models.ForeignKey(#llave foranea
        User,#clase a la cual esta apuntando la llave
        related_name= 'partido',
        null=False,
        on_delete=models.PROTECT,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label: 'app'

class Individuo(models.Model):
    indiv_name = models.CharField(max_length=200 , null= False)
    indiv_lastname = models.CharField(max_length=200 , null= False)
    birthday = models.DateField(null= True, blank=True)
    active = models.BooleanField(null=False)
    views = models.IntegerField(null= False)
    creator = models.ForeignKey(#llave foranea
        User,#clase a la cual esta apuntando la llave
        related_name= 'individuos',
        null=False,
        on_delete=models.PROTECT,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label: 'app'
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

class Proceso(models.Model):
    title = models.CharField(max_length=200 , null= False)
    date_start = models.DateField(null= False, blank=True)
    date_end = models.DateField(null= True, blank=True)
    state = models.BooleanField(null=False)
    entity = models.CharField(max_length=200 , null= False)
    howmuch = models.IntegerField(null= True)
    comments = models.CharField(max_length=300 , null= True)
    active = models.BooleanField(null=False)
    views = models.IntegerField(null= False)
    creator = models.ForeignKey(#llave foranea
        User,#clase a la cual esta apuntando la llave
        related_name= 'procesos',
        null=False,
        on_delete=models.PROTECT,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label: 'app'

class Afiliacion(models.Model):
    date_in = models.DateField(null= True, blank=True)
    date_out = models.DateField(null= True, blank=True)
    active = models.BooleanField(null=False)
    indiv_id = models.ForeignKey(#llave foranea
        Individuo,#clase a la cual esta apuntando la llave
        related_name= 'indiv_afil',
        null=False,
        on_delete=models.PROTECT,
    )
    part_id = models.ForeignKey(#llave foranea
        Partido,#clase a la cual esta apuntando la llave
        related_name= 'part_afil',
        null=False,
        on_delete=models.PROTECT,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label: 'app'

class Implicado(models.Model):
    date_imp = models.DateField(null= True, blank=True)
    charges = models.DateField(null= True, blank=True)
    guilty = models.BooleanField(null=True)
    sentence = models.CharField(max_length=45 , null= True)
    commnts = models.CharField(max_length=45 , null= True)
    afiliado = models.ForeignKey(#llave foranea
        Afiliacion,#clase a la cual esta apuntando la llave
        related_name= 'indiv_impl',
        null=False,
        on_delete=models.PROTECT,
    )
    proceso = models.ForeignKey(#llave foranea
        Proceso,#clase a la cual esta apuntando la llave
        related_name= 'proceso_impl',
        null=False,
        on_delete=models.PROTECT,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label: 'app'
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
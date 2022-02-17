from statistics import mode
from django.db import models
from django.utils import timezone

#creacion de detalle de blog
class DetallesBlog (models.Model):
    detalles= models.CharField(max_length=6000, default='vaule')
    logo=models.FileField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class meta:
        db_table= 'DetallesBlog '
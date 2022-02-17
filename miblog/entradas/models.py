from statistics import mode
from django.db import models
from django.utils import timezone

class entradas (models.Model):
    titulo = models.CharField(max_length= 5000, default='Value')
    contenido = models.TextField(default='value')
    img_destacada=models.FileField()
    slug=models.CharField(max_length=5000,default='value')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class meta:
        db_table= 'Entradas'
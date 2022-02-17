from statistics import mode
from django.db import models
from django.forms import model_to_dict
from django.utils import timezone

class usuarios (models.Model):
    nombre=models.CharField( max_length=1000,default='value')
    img=models.FileField()
    web=models.CharField(max_length=700,default='value')
    descripcion=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class meta:
        db_table= 'usuarios'
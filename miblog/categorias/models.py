from statistics import mode
from django.db import models
from django.utils import timezone

class categorias (models.Model):
    nombre = models.CharField(max_length= 100, default='Value')
    detalles= models.CharField(max_length=1000, default='vaule')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    class meta:
        db_table= 'categorias'




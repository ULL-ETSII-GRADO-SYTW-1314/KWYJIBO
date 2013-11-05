from django.db import models
from django.contrib import admin
import datetime
import time
# Create your models here.

class Receta(models.Model):
	GRUPOS = (
		('C', 'Carne'),
		('P', 'Pescado'),
		('P&P', 'Pasta y Pizza'),
		('E', 'Ensaladas'),
		('P&H', 'Postres y Helados'),
		('O', 'Otros'),
		)

	DIFICULTADES = (
		('F', 'Facil'),
		('M', 'Medio'),
		('D', 'Dificil'),
		)

	titulo = models.CharField(max_length=50)
	#Para usar ImageField necesitamos "Imaging Library" --> sudo apt-get install python-imaging
	imagen = models.ImageField(upload_to = 'imagenes_receta/', default = 'imagenes_receta/None/no-img.jpg')
	#autor = models.CharField(max_length=50) ##PODEMOS HACER QUE SE RRELLENE AUTO
	grupo = models.CharField(max_length=3, choices=GRUPOS)
	dificultad = models.CharField(max_length=3, choices=DIFICULTADES)
	tiempo = models.IntegerField(max_length=500) #en minutos
	personas = models.IntegerField(max_length=50)
	ingredientes = models.CharField(max_length=50)
	elaboracion = models.CharField(max_length=50)
	hora_subida = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.titulo
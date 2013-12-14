from django.db import models
from django.contrib import admin
from PIL import Image as PImage
from os.path import join as pjoin
import datetime
import time
import re

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
	##PODEMOS HACER QUE SE RELLENE AUTO
	autor = models.CharField(max_length=50)
	grupo = models.CharField(max_length=3, choices=GRUPOS)
	dificultad = models.CharField(max_length=3, choices=DIFICULTADES)
	tiempo = models.IntegerField(max_length=500) #en minutos
	personas = models.IntegerField(max_length=50)
	ingredientes = models.CharField(max_length=50)
	elaboracion = models.CharField(max_length=50) #TextField
	hora_subida = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.titulo

	@classmethod
	def checkCharField(self, text):
		valid = text
		if ((len(valid) > 1) and (len(valid) < 51)): 
			if re.match(r'([\s_a-zA-Z0-9]+)$', valid):
				return valid
			else:
				return None
		else: 
			return None

	@classmethod
	def checkIntegerField(self, text):
		valid = text
		if ((valid > 1) and (valid < 499)):
			return valid
		else: 
			return None

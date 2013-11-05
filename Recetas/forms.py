from django.forms import *
from Recetas.models import *
from django import forms

class Form_Receta(forms.Form):
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

	titulo = forms.CharField(max_length=50, label='Titulo')
	#Para usar ImageField necesitamos "Imaging Library" --> sudo apt-get install python-imaging
	imagen = forms.ImageField(upload_to = 'imagenes_receta/', default = 'imagenes_receta/None/no-img.jpg', label='Imagen')
	#autor = forms.CharField(max_length=50, label='Autor')
	grupo = forms.CharField(max_length=3, choices=GRUPOS, label='Grupo')
	dificultad = forms.CharField(max_length=3, choices=DIFICULTADES, label='Dificultad')
	tiempo = forms.DateTimeField(auto_now_add=True, label='Tiempo')
	personas = forms.IntegerField(max_length=50, label='Personas')
	ingredientes = forms.CharField(max_length=50, label='Ingredientes')
	elaboracion = forms.CharField(max_length=50, label='Elaboracion')
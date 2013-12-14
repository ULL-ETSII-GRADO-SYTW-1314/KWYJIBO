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
	imagen = forms.ImageField(label='Imagen')
	autor = forms.CharField(max_length=50, label='Autor')
	grupo = MultipleChoiceField(required=False, widget=SelectMultiple(), choices=GRUPOS, label ='Grupo')
	dificultad = MultipleChoiceField(required=False, widget=SelectMultiple(), choices=DIFICULTADES, label='Dificultad')
	tiempo = forms.IntegerField(label='Tiempo')
	personas = forms.IntegerField(max_value=50, label='Personas')
	ingredientes = forms.CharField(widget=forms.Textarea, max_length=500, label='Ingredientes')
	elaboracion = forms.CharField(widget=forms.Textarea, max_length=500, label='Elaboracion')
	hora_subida = models.DateTimeField(blank=True)
from django.forms import *
from Usuarios.models import *
from django import forms

class Form_Usuario(forms.Form):

	nick = forms.CharField(max_length=50, label='Nick de Usuario')
	nombre = forms.CharField(max_length=50, label='Nombre')
	apellidos = forms.CharField(max_length=50, label='Apellidos')
	email = forms.EmailField(label='Email')
	remail = forms.EmailField(label='Repita Email')
	password = forms.CharField(label='Contraseña')
	repassword = forms.CharField(label='Repita Contraseña')
	fecha_nacimiento = forms.CharField(max_length=50, label='Fecha de Nacimiento')
	

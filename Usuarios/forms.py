from django.forms import *
from Usuarios.models import *
from django import forms

class Form_Usuario(forms.Form):

	nick = forms.CharField(max_length=50, label='Nick de Usuario')
	nombre = forms.CharField(max_length=50, label='Nombre')
	apellidos = forms.CharField(max_length=50, label='Apellidos')
	email = forms.EmailField(label='Email')
	remail = forms.EmailField(label='Repita Email')
	password = forms.CharField(widget = forms.PasswordInput, label='Contrasenia')
	repassword = forms.CharField(widget = forms.PasswordInput, label='Repita Contrasenia')
	fecha_nacimiento = forms.CharField(max_length=50, label='Fecha de Nacimiento')

class Form_Auth_Usuario(forms.Form):
	nick = forms.CharField(max_length=50, label='Nick de Usuario')
	password = forms.CharField(widget = forms.PasswordInput, label='Contrasenia')

	@classmethod
	def logueado(self, nick):
		valid = nick
		if ( len(valid) > 0 ):
			return valid
		else:
			return None
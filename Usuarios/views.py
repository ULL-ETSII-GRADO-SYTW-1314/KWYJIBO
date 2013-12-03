from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from Usuarios.models import *
from Usuarios.forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

def Registro_Usuario(request):

	if request.method == 'POST':
		form = Form_Usuario(request.POST)
		if form.is_valid():
			print "VALIDO"

			#Array de Errores.
			errores = []
			#Creando un objeto del modelo Usuario.
			Nuevo_Usuario = Usuario()

			#ANADIENDO NICK
			aux = Usuario.objects.filter(nick=form.cleaned_data['nick'])

			if ( len(aux) == 0 ):
				if ( Nuevo_Usuario.checkUsuario(form.cleaned_data['nick']) is not None ):
					Nuevo_Usuario.nick = form.cleaned_data['nick']
				else:
					errores.append('El Nick tiene caracteres no validos.')
			else:
				errores.append('El Nick ya existe.')

			#ANADIENDO NOMBRE
			if ( Nuevo_Usuario.checkUsuario(form.cleaned_data['nombre']) is not None ):
				Nuevo_Usuario.nombre = form.cleaned_data['nombre']
			else:
				errores.append('El Nombre de usuario tiene caracteres no validos.')
			
			#ANADIENDO APELLIDOS
			if ( Nuevo_Usuario.checkUsuario(form.cleaned_data['apellidos']) is not None ):
				Nuevo_Usuario.apellidos = form.cleaned_data['apellidos']
			else:
				errores.append('Los Apellidos de usuario tienen caracteres no validos.')

			#ANADIENDO PASSWORD
			if ( Nuevo_Usuario.checkPassword(form.cleaned_data['password']) is not None ):
				Nuevo_Usuario.password = form.cleaned_data['password']
			else:
				errores.append('La password debe de tener un minimo de 3 caracteres')


			if ( Nuevo_Usuario.checkPassword(form.cleaned_data['repassword']) is not None ):
				if ( Nuevo_Usuario.password == Nuevo_Usuario.checkPassword(form.cleaned_data['repassword']) ):
					Nuevo_Usuario.repassword = form.cleaned_data['repassword']
				else:
					errores.append('Las password deben ser iguales')
			else:
				errores.append('La password debe de tener un minimo de 3 caracteres')

			#ANADIENDO EMAIL
			if ( Nuevo_Usuario.checkEmail(form.cleaned_data['email']) is not None ):
				if ( Nuevo_Usuario.checkEmail(form.cleaned_data['remail']) is not None ):
					if ( Nuevo_Usuario.checkDifferentEmail(form.cleaned_data['email'],form.cleaned_data['remail']) is None):
						Nuevo_Usuario.email = form.cleaned_data['email']
					else:
						errores.append('Los email no coinciden')
				else:
					errores.append('El email es invalido')

			#ANADIENDO FECHA NACIMIENTO
			fecha = form.cleaned_data['fecha_nacimiento'].__str__()
			if(Nuevo_Usuario.checkDate(fecha) is not None):
				Nuevo_Usuario.fecha_nacimiento = fecha
			else:
				errors.append('Fecha erronea: Debe ser mayor de 14 anos')

			print "FIN"
			#GUARDAMOS EN LA BBDD
			if (len(errores) != 0):
				return render_to_response('usuarios/registrate.html', {'form':form, 'errores':errores}, context_instance=RequestContext(request))
			else:
				print "ENTER"
				Nuevo_Usuario.save()
				return HttpResponseRedirect('/')
			

		#else:
			#return HttpResponseRedirect('www.google.es')
	else:
		form = Form_Usuario()
		return render_to_response('usuarios/registrate.html', {'form':form}, context_instance=RequestContext(request))
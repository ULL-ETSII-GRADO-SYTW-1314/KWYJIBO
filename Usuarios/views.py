from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from Recetas.models import *
from Recetas.forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

def Registro_Usuario(request):

	if request.method == 'POST':
		form = Form_Usuario(request.POST)
		if form.is_valid():

			#Array de Errores.
			errores = []
			#Creando un objeto del modelo Usuario.
			Nuevo_Usuario = Usuario()

			#AÑADIENDO NICK
			aux = form.cleaned_data['nick']
			
			aux1 = Usuario.objects.filter(nick=Nuevo_Usuario.checkUsuario(form.cleaned_data['nick']))

			if ( aux != Usuario.objects.get(nick=aux) ):
				if ( Nuevo_Usuario.checkUsuario(aux) is not None ):
					Nuevo_Usuario.nick = aux;
				else:
					errores.append('El usuario tiene caracteres no validos.')
			else:
				errores.append('El usuario ya existe.')
			
	else:
		form = Form_Receta()
		return render_to_response('recetas/subir_receta.html', {'form':form}, context_instance=RequestContext(request))
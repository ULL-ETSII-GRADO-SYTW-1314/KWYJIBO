from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from Recetas.models import *
from Recetas.forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

def subir_receta(request):
	if request.method == 'POST':
		form = Form_Receta(request.POST, request.FILES)
		if form.is_valid():

			#Array de Errores.
			errores = []
			#Creando un objeto del modelo Receta.
			Nueva_Receta = Receta()

			#SECCION DEL TITULO DE LA RECETA.

			#Auxiliar que busca si el titulo existe en la BBDD
			aux = Receta.objects.filter(titulo=form.cleaned_data['titulo'])

			if ( len(aux) == 0 ):
				if(Receta.checkCharField(form.cleaned_data['titulo']) is not None):
					titulo = Receta.checkCharField(form.cleaned_data['titulo'])
					Nueva_Receta.titulo = titulo
				else:
					errores.append('El titulo contiene caracteres no validos. ')
			else:
				errores.append('El titulo de la receta ya existe.')

			#SECCION DEL AUTOR DE LA RECETA.

			#Auxiliar que busca si el titulo existe en la BBDD
			aux = Receta.objects.filter(autor=form.cleaned_data['autor'])

			if (aux != form.cleaned_data['autor']):
				if(Receta.checkCharField(form.cleaned_data['autor']) is not None):
					autor = Receta.checkCharField(form.cleaned_data['autor'])
					Nueva_Receta.autor = autor
				else:
					errores.append('El campo "autor" contiene caracteres no validos. ')
			else:
				errores.append('El campo "autor" de la receta ya existe.')

			#SECCION DEL TIEMPO DE LA RECETA.

			if(Receta.checkIntegerField(form.cleaned_data['tiempo']) is not None):
				tiempo = Receta.checkIntegerField(form.cleaned_data['tiempo'])
				Nueva_Receta.tiempo = tiempo
			else:
				errores.append('El campo "tiempo" contiene caracteres no validos. ')

			#SECCION DEL NUMERO DE PERSONAS DE LA RECETA.

			if(Receta.checkIntegerField(form.cleaned_data['personas']) is not None):
				personas = Receta.checkIntegerField(form.cleaned_data['personas'])
				Nueva_Receta.personas = personas
			else:
				errores.append('El campo "personas" contiene caracteres no validos. ')


			#SECCION DEL GRUPO DE LA RECETA.
			grupo = form.cleaned_data['grupo']
			grupo = grupo.__str__()
			grupo = grupo[3:4]
			if len(grupo) > 0:
				Nueva_Receta.grupo = grupo
			else:
				errores.append('El campo "grupo" no ha sido seleccionado ')

			#SECCION DE LA DIFICULTAD DE LA RECETA.
			dificultad = form.cleaned_data['dificultad']
			dificultad = dificultad.__str__()
			dificultad = dificultad[3:4]
			if len(dificultad) > 0:
				Nueva_Receta.dificultad = dificultad
			else:
				errores.append('El campo "dificultad" no ha sido seleccionado ')

			#SECCION DE LOS INGREDIENTES DE LA RECETA.

			if(Receta.checkCharField(form.cleaned_data['ingredientes']) is not None):
				ingredientes = Receta.checkCharField(form.cleaned_data['ingredientes'])
				Nueva_Receta.ingredientes = ingredientes
			else:
				errores.append('El campo "ingredientes" contiene caracteres no validos. ')

			#SECCION DE LA ELABORACION DE LA RECETA.

			if(Receta.checkCharField(form.cleaned_data['elaboracion']) is not None):
				elaboracion = Receta.checkCharField(form.cleaned_data['elaboracion'])
				Nueva_Receta.elaboracion = elaboracion
			else:
				errores.append('El campo "elaboracion" contiene caracteres no validos. ')

			Nueva_Receta.imagen = form.cleaned_data['imagen']

			#Comprobacion de errores y/o guardado de la receta en la BBDD.
			if (len(errores) != 0):
				return render_to_response('recetas/subir_receta.html', {'form':form, 'errores':errores}, context_instance=RequestContext(request))
			else:	
				Nueva_Receta.save()
				return render_to_response('recetas/subida_de_receta.html', context_instance=RequestContext(request))
		#else:
			#return HttpResponseRedirect('www.google.es')
	else:
		form = Form_Receta()
		return render_to_response('recetas/subir_receta.html', {'form':form}, context_instance=RequestContext(request))

def mostrar_receta(request):

	#Obtener el id de la receta.
	path = request.path_info.__str__()
	len_path = len("/recetas/")
	n_recetas = len_path + Receta.objects.count()
	id_receta = path[len_path:n_recetas]
	id_receta = id_receta


	if ( len(id_receta) > 0 ):
		Listado_Recetas = Receta.objects.all()
		receta = Listado_Recetas[int(id_receta)-1]
		Listado_Recetas = Listado_Recetas.order_by('titulo')
		return render_to_response('recetas/recetas.html', {'lista':Listado_Recetas, 'receta':receta}, context_instance=RequestContext(request))
	else:
		print "pepeeee"
		Listado_Recetas = Receta.objects.all()
		Listado_Recetas = Listado_Recetas.order_by('titulo')
		return render_to_response('recetas/recetas.html', {'lista':Listado_Recetas}, context_instance=RequestContext(request))
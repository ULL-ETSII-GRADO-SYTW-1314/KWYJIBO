from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from Usuarios.models import *
from Recetas.models import *


####################################################
#Scenario: Probar el acceso al HTML raiz
@before.all
def set_browser():
	world.browser = Client()

@step(r'acceder a la url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

#Scenario Subir una Receta

#Crear una receta
@step(r'Crear una receta')
def crear_receta(step):
	recipe = Receta(titulo= "pollo",autor="pepe", grupo= "Carne", dificultad="Facil",tiempo="50",personas="2",ingredientes="pollo",elaboracion="pollo")
	world.recipe = recipe
	assert (world.recipe,Receta())

#Debe tener un titulo
@step(r'Debe tener un titulo')
def tener_titulo(step):
	assert world.recipe.titulo is not None

#Debe tener un autor
@step(r'Debe tener un autor')
def tener_autor(step):
	assert world.recipe.autor is not None

#Debe tener grupo
@step(r'Debe tener grupo')
def tener_grupo(step):
	assert world.recipe.grupo is not None

#Debe tener una dificultad
@step(r'Debe tener una dificultad')
def tener_dificultad(step):
	assert world.recipe.dificultad is not None

#Debe tener un tiempo
@step(r'Debe tener un tiempo')
def tener_tiempo(step):
	assert world.recipe.tiempo is not None

#Debe tener un numero de personas
@step(r'Debe tener un numero de personas')
def tener_personas(step):
	assert world.recipe.personas is not None

#Debe tener una elaboracion
@step(r'Debe tener una elaboracion')
def tener_elaboracion(step):
	assert world.recipe.elaboracion is not None


##################################################################################
#Scenario: Comprobacion de las recetas

#titulo no es mayor de 50
@step(r'titulo no es mayor de 50')
def titulo_no_mayor(step):
	if len(world.recipe.titulo) < 50:
		assert True
	else:
		assert False

#autor no es mayor de 50 
@step(r'autor no es mayor de 50')
def autor_no_mayor(step):
	if len(world.recipe.autor) < 50:
		assert True
	else:
		assert False
#grupo no es mayor de 50 
@step(r'grupo no es mayor de 50')
def grupo_no_mayor(step):
	if len(world.recipe.grupo) < 50:
		assert True
	else:
		assert False
#tiempo no es mayor de 500
@step(r'tiempo no es mayor de 500')
def tiempo_no_mayor(step):
	if len(world.recipe.tiempo) < 500:
		assert True
	else:
		assert False
#numero de personas no es mayor de 50
@step(r'numero de personas no es mayor de 50')
def titulo_no_mayor(step):
	if len(world.recipe.personas) < 50:
		assert True
	else:
		assert False

#elaboracion no es mayor a 50
@step(r'elaboracion no es mayor a 50')
def titulo_no_mayor(step):
	if len(world.recipe.elaboracion) < 50:
		assert True
	else:
		assert False

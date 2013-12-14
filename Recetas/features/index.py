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
	


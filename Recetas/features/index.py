from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from Recetas.models import *



#Scenario Subir una Receta

#Crear una receta
@step(r'Crear una receta')
def crear_receta(step):
	receta = Receta(titulo= "pollo")
	recetass = receta
	assert (recetass,Receta())
#	receta = Receta(titulo= "pollo",autor="pepe", grupo= "Carne", dificultad="Facil",tiempo="50",personas="2",ingredientes="pollo",elaboracion="pollo",hora_subida="10:20:30")
#	world.receta = receta
#	assert True

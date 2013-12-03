from lettuce import *
from lxml import html
from django.test.client import Client
#from nose.tools import assert_equals
from Usuarios.models import *
from Recetas.models import *


####################################################
#Scenario: Probar el acceso al HTML raiz
@before.all
def set_browser():
	world.browser = Client()

#Acceder a la url '/'
@step(r'acceder a la url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

#ver el encabezado Kwyjibo
#@step(r'ver el encabezado "(.*)"')
#def access_header(step, text):
#	header = world.dom.cssselect("h1")[0]
#	assert header.text == text
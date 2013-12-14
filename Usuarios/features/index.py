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


#Scenario: Atributos de un Usuario
#Crear un usuario
@step(r'crear un usuario')
def crear_usuario(step):
	user = Usuario(nick = "pepito", nombre = "Pepe", apellidos = "Rodriguez", email = "peper@gmail.com", password = "12345", fecha_nacimiento = "02/05/1991")
	world.user = user
	assert (world.user, Usuario())
#Debe tener un nick
@step(r'Debe tener un nick')
def nick(step):
	assert world.user.nick is not None
#Debe tener un nombre	
@step(r'Debe tener un nombre')
def nombre(step):
	assert world.user.nombre is not None
#Debe tener un email
@step(r'Debe tener un email')
def email(step):
	assert world.user.email is not None
#Debe tener un password
@step(r'Debe tener un password')
def password(step):
	assert world.user.password is not None
#tamano del password mayor a 3
@step(r'Tamano del password mayor a 3')
def tamano_pass(step):
	if len(world.user.password)> 3:
		assert True
	else:
		assert False
#Debe tener fecha de fecha_nacimiento
@step(r'Debe tener una fecha de nacimiento')
def fecha_nacimiento(step):
	assert world.user.fecha_nacimiento is not None


#Scenario Password de un usuario
#Debe tener un password 1234A
@step(r'Debe tener un password(.*)')
def tener_un_password(step, password):
	world.password_valido = password
#El password debe ser valido
@step(r'Debe tener un password valido')
def password_valid(step):
	user = Usuario()
	assert_equals(world.second_password, user.checkPassword(world.second_password))

#El password no puede estar vacio
@step(r'El password no puede estar vacio')
def password_no_vacio(step):
	user = Usuario()
	if len(world.user.password)> 1:
		assert True
	else:
		assert False

#Scenario Password Iguales
#Existe un segundo password
@step(r'Existe un segundo password(.*)')
def segundo_password(step,password):
	world.second_password = password
	
#El segundo password no es vacio
@step(r'El segundo password no es vacio(.*)')
def primer_no_vacio(step,password):
	world.second_password = password
	if len(world.second_password)>1:
		assert True
	else:
		assert False


@step(r'I have a usuario (.*)')
def have_a_usuario(step, usuario):
    world.valid_usuario = usuario

#When I check if usuario is valid
@step(r'I check if usuario is valid')
def check_if_usuario_is_valid(step):
    world.valid_usuario = Usuario.checkUsuario(world.valid_usuario)
    assert world.valid_usuario is not None
#When I check if usuario is not valid  
@step(r'I check if usuario is not valid')
def check_if_usuario_is_valid(step):
    world.valid_usuario = Usuario.checkUsuario(world.valid_usuario)
    assert world.valid_usuario is None  



    
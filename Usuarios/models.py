from django.db import models
import re
import datetime
import time
# Create your models here.

class Usuario(models.Model):

	nick = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	fecha_nacimiento = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nick

	@classmethod
	def checkUsuario(self, text):
		valid = text
		if ((len(valid) > 1) and (len(valid) < 51)): 
			if re.match(r'([ _a-zA-Z0-9]+)$', valid):
				return valid
			else:
				return None
		else: 
			return None

	@classmethod
	def checkDifferentEmail(self, email1, email2):
		valid = email1
		valid2 = email2
		if ((len(valid) > 1) and (len(valid) < 51) and (len(valid2) > 1) and (len(valid2) < 51)): 
			if re.match(r'(^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3}))$', valid):
				if ( email1 != email2):
					return valid
					return valid2
				else:
					return None
			else:
				return None
		else:
			return None

	@classmethod
	def checkEmail(self, text):
		valid = text
		if ((len(valid) > 1) and (len(valid) < 51)): 
			if re.match(r'(^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3}))$', valid):
				return valid
			else:
				return None
		else:
			return None

	@classmethod
	def checkPassword(self, password):
		valid = password
		if len(password) >=3: 
			if re.match(r'([a-zA-Z0-9]+)$', valid):
				return valid 

	@classmethod
	def checkDate(self, date):
		if len(date) == 10:
			dia = date.split("/", 3)[0]
			mes = date.split("/", 3)[1]
			anio = date.split("/", 3)[2]

			fecha = time.strftime("%d-%m-%Y")
			a_dia = fecha.split("-",3)[0]
			a_mes = fecha.split("-",3)[1] 
			a_anio = fecha.split("-",3)[2] 

			if (int(anio) < int(a_anio)-13):
				if (int(mes) <= 12):
					if (int(dia) <= 31): 
						return  date
			elif (int(anio) == int(a_anio)-14 ):
				if (int(mes) < int(a_mes)+1):
					if (int(dia) < int(a_dia)+1):
						return date
					else:
						return None
				else:
					return None
			else:
				return None
		else:
			return None
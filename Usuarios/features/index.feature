Feature: Validacion modelo de usuario

	Scenario: Probar el acceso al HTML raiz
		acceder a la url "/"
		ver el encabezado "Kwyjibo"


	Scenario: Atributos de un usuario
		crear un usuario
		Debe tener un nick
		Debe tener un nombre
		Debe tener un email
		Debe tener un password
		Tamano del password mayor a 3
		Debe tener una fecha de nacimiento

	Scenario: Password de un usuario
		Debe tener un password A1234
		Debe tener un password valido
		El password no puede estar vacio A1234
		Existe un segundo password A1234
		El segundo password no es vacio A1234

	Scenario: These users with length shorter than 50 should pass
			Given I have a usuario Macarena
			When I check if usuario is valid
		#Examples:
		#|usuario |
		#|Jessica |
		#|FernandO|
		#|ANGELA91|
		#|jess    |
		#|fErni   |

	Scenario: These users with length shorter than 50 should fail
		Given I have a usuario Je$$ica
		When I check if usuario is not valid
	#Examples:
	#|usuario       |
	#|Je$$ica       |
	#|@jess         |
	#|Fer/ni        |
	#|angie(lokilla)|



	Scenario: Nombres de usuario sin palabrotas
		Obtengo un nombre de usuario pepe
		Compruebo que el nombre de usuario no es vacio
		Compruebo que el nombre de usuario es valido
		Compruebo que el usuario no tiene palabrotas pepe
		



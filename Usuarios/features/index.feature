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
		El password no puede estar vacio
		Existe un segundo password A1234
		El primer password no es vacio
		El segundo password no es vacio
		Los password son iguales
		El segundo password es valido





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
		Los password son iguales A1234 A1234
		





Feature: Validacion modelo de Recetas

	Scenario: Probar el acceso al HTML raiz
		acceder a la url "/"


	Scenario: Subir una Receta
		Crear una receta
		Debe tener un titulo
		Debe tener un autor
		Debe tener grupo
		Debe tener una dificultad
		Debe tener un tiempo
		Debe tener un numero de personas
		Debe tener una elaboracion

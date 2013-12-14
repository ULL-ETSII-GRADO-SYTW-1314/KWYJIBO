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

	Scenario: Comprobacion de las recetas
		titulo no es mayor de 50
		autor no es mayor de 50 
		grupo no es mayor de 50 
		tiempo no es mayor de 500
		numero de personas no es mayor de 50
		elaboracion no es mayor a 50

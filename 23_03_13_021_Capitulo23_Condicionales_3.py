"""En este capitulo veremos acerca de la continuacion del 'if' el 'elif' el cual permite preguntar varias cosas a la vez y que estas
pueden ser evaluadas y detectar si son verdaderas o falsa de tal forma que solo quede 1 verdadera. Tambien tenemos que tomar en cuenta
la entrada datos por medio de la instruccion 'input()' en la cual tenemos que escribir el String que se tienen que responder esto hara
que cuando se corra el programa este se detenga en esta parte y espera a que el usuario responda la peticion"""

"""Para este ejemplo tenemos la variable de tipo 'int' la cual vamos a solicitar que el usuario escriba por medio de la instruccion
'input', este dato se va utilizar de condicion para evaluarla en el 'if' y en los 'elif' para que revise en cual de las categorias
recae el valor ingresado"""
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 35:
	print('Eres un joven.')
elif edad >= 35 and edad <= 60:
    print('Eres un señor.')
elif edad >= 60 and edad <= 100:
    print('Eres un adulto mayor.')
else:
	print('Edad no válida.')
"""Se puede observar que en una cadena sucesiva de 'elif' los cuales permiten evaluar todas las categorias y responder de manera
individual a cada una de las condiciones, siendo la ultima condiciones que si ninguna de las anteriores se cumple entonces pasa a
evaluar el 'else' que se encuentra cuando todas las demas son negadas"""
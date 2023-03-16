"""El diccionario cuenta con el metodo 'len()' podemos contar los elemento que se encuentran dentro de una lista o una
tupla, los diccionario al igual que otros temas tiene el uso del metodo 'del()' para eliminar objetos de la lista o de la
tupla, asi como vimos en el capitulo pasado podemos agregar una variable en la lista incluso con su valor especifico"""

"""Para el ejercicio de este capitulo tenemos que utilizar el metodo 'del()' para ello utilizaremos los 2 diccionarios que
la actividad nos da; El obtjetivo es borrar el diccionario 1 llamado 'teclado1' por lo cual despues de crearlo utilizaremos
el metodo 'del' declarando que vamos a borrar toda la lista colocando su nombre justo despues de la declaracion del metodo"""

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

"""Para el segundo diccionario no lo vamos a eliminar por completo si no que solo borraremos 2 variables dentro del
diccionario con sus respectivos valores, para esto utilizaremos el metodo 'del()' para eliminar estos, pero para no
eliminar todo el diccionario tenemos que especificar cual el la variable que queremos que borre, poniendo entre corchetes
cual es la variable a borrar"""

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']

print(teclado2['Modelo'])
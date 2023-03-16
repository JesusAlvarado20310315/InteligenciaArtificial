"""Continuando con los diccionarios tenemos que podemos agregar o modificar el valor dentro de una variable dentro de un
diccionario haciendo que declaremos el nombre del diccionario con unos parentesis los cuales tendran dentro el nombre de
la variable que se quiera modificar, tambien vamos a mostrar que es lo que pasa si ponemos un 'for' para el diccionario
haciendo que este pueda entrar cada iteracion que contenga el diccionario"""


"""Para el ejercicio creamos el diccionario llamado 'teclado1' el cual tendra las variables y sus datos mostrados a este
diccionario tenemos evaluarlo en un 'for' el cual va a evaluar la variable 'x' y esta va a leer todo lo que tiene el
diccionario de 'teclado1'"""
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

"""En esta parte vamos a ejecutar el bucle 'for' para poder hacer que revise cada iteracion del diccionario 'teclado1'
y en la parte de la impresion tenemos el valor de la variable 'x' junto con un '=' y la iteracion de la variable 'x'"""
for x in teclado1:
	print(x, '=', teclado1[x] + '.')
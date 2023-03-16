"""Continuando con los bucles tenemos el bucle de 'for' el cual permite hacer una iteracion de cada uno de los elementos que
se le coloquen o que se vallan a evaluar ya sea desde una lista o una tupla, a estos tambien le podemos agregar las palabras
claves de 'continue' 'break' 'pass' de igual forma que con los bucles while"""

"""Para demostrar como funciona el for en este ejercicio utilizaremos una tupla con el nombre 'col' el cual tiene los valores
mostrados, al 'for' le pediremos que nos itera cada valor en una variable llamada 'x' dentro de la tupla y que imprima el
valor de 'x' de esta forma tenemos podemos ver cada iteracion impresa"""
col = ('rojo', 'azul', 'verde', 'amarillo')

for x in col:
	print('El color es: ' + x + '.')
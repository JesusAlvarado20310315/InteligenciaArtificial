"""Continuando con las funciones tenemos que en estas podemos utilizar los argumentos con la pabra clabe '*args' de esta forma podemos
utilizar los datos dentro del funciones de una manera mucho mas efectiva de tal forma que podemos llamar a un caso en particular"""

"""En este caso utilizaremos 2 funciones ambas con el argumento '*args' para mostrar lo siguiente que podemos llamar los datos
especificos de una tupla pero de manera inversa de tal forma que primero utizaremos el args para llamar al segundo objeto de la
tupla y el primero despues con los valores de 1 y 0 para poder mandarlos a llamar de manera correcta"""
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')

"""Por ultimos en esta funcion tenemos que utilizar el mismo '*args' para que este pueda sumar todo los valores que se encuentran
dentro de la tupla para al final imprimir el resultado"""
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)
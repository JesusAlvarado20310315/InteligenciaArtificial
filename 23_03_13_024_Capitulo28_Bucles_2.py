"""Al utilizar los bucles 'while' estos pueden tener concatenados los condicionales 'if' pero es necesario que cada uno de
estos 'if' el mismo bucle 'while' tengan un 'break o un 'continue' lo cual hara que este pare o haga una excepcion a la
condicion dada, obteniendo asi un condicional complejo"""

"""Para este ejemplo utilizaremos un bucle con 2 condicionales para esto crearemos la variable 'x' con un valor numerico
de '0', este estara vinculado al bucle 'while' el cual hara todo lo que este dentro de este mientras que 'x' sea menor que
o igual a 30, para que el bucle no sea infinito tendremo que hacer que la variable aumente por lo cual tendremos que hacer
que cada vez que pase por el bucle este aumente 1 al valor de x"""
x = 0

while x <= 30:
	x += 1

	"""Una vez dentro del bucle vamos a generar las 2 condicionales a evaluar en la primera condicional tendremos que
 	utilizar la instruccion 'continue' esto con el fin de que haga un brinco al tener como valores los numeros 4,6 y 10,
  	para poder hacer que todo esto lo haga en una sola condicional sin necesidad de colocar mas 'if' o 'elif' podemos
   	utilizar la palabra 'or' al momento de declarar la condicion ya que esto hacer que podamos evaluar los 3 numeros en 1
    condicional al mismo tiempo. Por ultimo al momento de que esta sentencia se cumpla este imprimira el valor de 'x' ya
    sea 4,6 o 10"""

	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x, ' de x')
		continue

	"""El segundo condicional que utilizaremos estara utilizando la palabra break la cual hara que tanto el condicional 'if
 	como el bucle se detengan ya que este hace que se pare por lo cual nuestra condicion estara iguala a 15 con una impresion
  	que nos confirmara cuando esto pase de tal modo que todo el ciclo se termina"""

	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break

	"""Para confirmar que el valor de x y como este va aumentando utilizaremos la funcion 'print' para verificar el valor
 	de x"""

	print(x)
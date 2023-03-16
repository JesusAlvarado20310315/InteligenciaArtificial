"""En este capitulo veremos lo que son los bucles con la sintaxis 'while' estos permiten repetir una accion hasta que se cumpla una
condicion dada"""

"""Para el ejercicio teniamos que declarar 3 variables las cuales son para cada caso 'x' para el primero con un valor numerico de 0,
'y' para el segundo con un valor numerico de 0 y 'z' para el tercero con un valor numerico de 10"""
x = 0
y = 0
z = 10

"""Para el primer ejercicio tenemos que declarar el bucle 'while' con la condicion de que 'x' sea menor que igual a 15 por lo cual
la variable 'x' al estar declarada con el valor numerico 0 entra dentro del bucle y dentro de este mismo se encuentra la indicacion
de imprimir el valor de 'x' la siguiente linea es una suma hacia la variable de 'x' con una cantidad de 5, despues de esto entra en
efecto el bucle ya que el 'while' vuelve a revisar la variable de 'x' por lo cual entra otra vez dentro del ciclo ya que 'x' aun
entra dentro de la condicion del bucle al ser su valor el numero '5', esto se va a repetir hasta que el valor de 'x' sea 15 que es
el momento en el que terminar el bucle 'while' al cumplit la condicion y sale de este"""
while x <= 15:
	print(x)
	x += 5

"""Para el segundo ejercicio podemos tener en cuanto lo que vimos en el anterior pero con la diferencia de que ahora en ves suma a
la variable esta tendra un decremento que hara que la variable disminuya su valor o como en el caso del ejemplo que el valor sea
negativo"""
while y >= -100:
	print(y)
	y -= 20

"""Por ultimo tenemos este bucle en el cual tenemos que evaluar 'z' con la condicion mostrada haciendo un decremento de la variable
hasta que el valor sea 0, mientras que tambien podemos ver que la variable esta siendo impresa al mismo tiempo que un String por lo
cual al momento de imprimirlo tendremos el String mas el valor que tenga la variable"""
while z >= 0:
	print('El valor de z es: ', z)
	z -= 1
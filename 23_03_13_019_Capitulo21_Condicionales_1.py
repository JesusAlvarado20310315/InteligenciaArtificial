"""En este caapitulo empezamos a ver los condicionales por lo cual se nos introducen diferente operandos estos son :
'<'     Mayor que
'>'     Menor que
'>='    Mayor o igual que
'=>'    Menor o igual que
'=='    Igual que
'!='    Diferente que
Estos nos permitiran utilizar condicionales por ejemplo el condicional 'if' el cual dependiendo de la condicion que
se le ponga puede regresar un 'true' o un 'false' dependiendo de la respuesta puede realizar alguna accion o no hacer nada"""

"""Para ponerlo aprueba tenemos los ejercicios por ejemplo en este tenemos que lograr hacer que el 'if' sea 'True' este es el
codigo que tenemos que cambiar:

num1 = 15
num2 = 20

if num1 == num2:
	print('Se ejecuta el if.')

Para este caso tenemos diferentes opciones ya que podemos utilizar diferente operando para que la condicion del 'if' sea verdadera
podemos ocupar '<' ya que 'num1' es menor que 'num2', o tambien '<=' ya que no es igual pero si es menor por lo cual puede hacer que
la condicion sea verdadera y por ultimo podemos ocupar en el caso de que sea '!=' diferente de el cual es el caso que voy a ocupar"""

num1 = 15
num2 = 20

if num1 != num2:
	print('Se ejecuta el primer if.')

"""Como segundo ejercicio tenemos que lograr hacer que el 'if' sea 'True' este es el codigo que tenemos que cambiar:

num1 = 1450
num2 = 60

if num1 < num2:
	print('Se ejecuta el if.')

Para este caso tenemos diferentes opciones ya que podemos utilizar diferente operando para que la condicion del 'if' sea verdadera
podemos ocupar '>' ya que 'num1' es mayor que 'num2', o tambien '>=' ya que no es igual pero si es mayor por lo cual puede hacer que
la condicion sea verdadera y por ultimo podemos ocupar en el caso de que sea '!=' diferente de el cual es el caso que voy a ocupar"""

num1 = 1450
num2 = 60

if num1 != num2:
	print('Se ejecuta el segundo if.')
 
"""Como ultimo ejercicio tenemos que lograr hacer que el 'if' sea 'false' sin cambiar el operador este es el codigo que
tenemos que cambiar:

num1 = 1450
num2 = 60

if num1 != num2:
	print('Se ejecuta el if.')

Al no poder cambiar el operador entonces tenemos 2 posibles soluciones las cuales son cambiar los valores de las variables 
por lo cual tenemos que cambiar 'num1' por el valor de '60' o 'num2' por el valor de '1450' que es lo que voy a hacer"""

num1 = 1450
num2 = 1450 

if num1 != num2:
	print('Se ejecuta el tercer if.')
 
"""Al hacer que la condicional sea 'false' no tendria que salir al momento de imprimir ya que no es 'True'"""
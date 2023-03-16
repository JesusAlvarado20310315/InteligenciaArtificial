"""Continuamos viendo condicionales ahora veremos la continuacion del 'if' el 'else' el cual permite realizar la accion contraria
a la que necesitemos en caso de ser 'True' al caso 'else' seria 'False'"""

"""El ejercicio de este capitulo es corregir el siguiente codigo el cual esta mal escrito:

color = rojo

else color == rojo
Print "El color es rojo."
if color != rojo
Print "El color no es rojo."

El primer error que podemos ver es que la declaracion de la variable esta mal ya que aunque esta declarado un String el texto no esta
dentro de comillas ya sean dobles o simples para corregirlo vamos a agregar unas comillas simples

color = 'rojo'

else color == rojo
Print "El color es rojo."
if color != rojo
Print "El color no es rojo."

La siguiente linea de codigo es el inicio de la condicional pero esta de igual manera esta incorrecta ya que primero se tiene que 
colocar la sentencia 'if' y luego su consecuentes 'else' por lo cual hay que cambiarlos de lugar, tenemos que revisar que los datos
a evaluar sean de mismo tipo ya sea String, numerico o float en este caso tenemos que agregar unas comillas para que se puedan
igualar los String en la condicional 'if' por ultimo tenemos que agregar los ':' al final de la sentencia 'if' para que detecte el
inicio de este

color = 'rojo'

if color == 'rojo':
Print "El color es rojo."
else color != rojo
Print "El color no es rojo."

En la siguiente linea que es la impresion en caso de que la condicional sea 'TRUE' tenemos 2 errores, el primero que podemos ver es
que no esta tabulado despues de la condicional 'if' esto es muy importante ya que en python la tabulacion aparte de ayudar
visualmente al programador es necesario para python ya que si no este genera un error esto lo vamos a corregir tambien en la ultima
linea ya que el 'else' no debe de llevar la tabulacion y el segundo error es en la declaracion de la instruccion para imprimir el
texto ya que esta mal escrita por que esta con mayusculas y no tiene sus respectivos parentesis por lo cual el codigo terminar asi

color = 'rojo'

if color == 'rojo':
    print("El color es rojo.")
else color != rojo
    Print "El color no es rojo."
    
En la siguiente linea tenemos la sentencia 'else' la cual tiene un error esto debido a aque no debe de llevar alguna condicional ya 
que la condicional tiene que ir solamente en el 'if' por lo cual tenemos que retirar este sentencia del 'else' y agregar los ':'
al final del 'else' para que se detecte el inicio de este por lo cual el codigo termina asi

color = 'rojo'

if color == 'rojo':
    print("El color es rojo.")
else:
    Print "El color no es rojo."
    
Ya para terminar en la ultima linea tenemos el mismo error de impresion anterior por lo cual tenemos que corregir la instruccion
del print poniendolo en minusculas y entre los parentesis el codigo terminaria asi"""

color = 'rojo'

if color == 'rojo':
    print("El color es rojo.")
else:
    print("El color no es rojo.")
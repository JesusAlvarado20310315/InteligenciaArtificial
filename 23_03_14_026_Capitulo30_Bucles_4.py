"""Continuando con los bucles 'for' tenemos el tipo de dato 'range()' el cual nos permite hacer que una varialble aumente o
decremente su valor """

"""Para el ejercicio se nos pide que hagamos uso del tipo de dato 'range()' haciendo que este valla desde el valor 7 hasta
el valor 700 con saltos de 100 en 100 para esto utilizaremos el for con su variable 'x' en la cual haremos uso del 'range()'
con el 7 al principio para marcar su valor de inicio, despues el 700 marcando hasta cual tiene que llegar y por ultimo el
100 para marcar los saltos que tiene que dar"""
for x in range(7, 700, 100):
	print(x)
"""Cabe destacar que al hacer saltos de 100 en 100 y empezar en el 7 este no llegara hasta el 700 exacto pero lo hara hasta
el 607 que es el numero mas cercano"""
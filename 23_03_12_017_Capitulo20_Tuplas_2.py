"""Las tuplas al tener mas o menos las misma caracteristicas que las listas hay un metodo el cual permite pasar de una lista a una
tupla y de una tupla a una lista, estos son respectivamente 'tuple()' y 'list()'"""

"""Pondremos a prueba estas instrucciones cambiando la siguiente lista llamada 'col' en una tupla para esto solo tenemos que crear
otra variable llamada 'coltup' en la cual vamos a igualarla con el metodo 'tuple()' lo cual la va a transformar en una tupla"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
coltup = tuple(col)

"""Para ver el resultado podemos imprimir la nueva tupla y verificar que se imprima con () y no []"""
print(coltup)
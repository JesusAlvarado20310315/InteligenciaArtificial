"""Para terminar con las listas tenemos los metodos 'sort()' y 'sorted()'. Los cuales nos permiten acomodar los elementos de una
lista de manera alfabeticamente (a-z) en caso de que querramos que este orden sea invertido tendremos que escribir 'reverse=true'
esto hace que el orden sea el inverso (z-a)"""

"""Para este caso tenemos la lista llamada col con los elementros mostrados nuestro objetivo es acomodarlos de manera alfabetica
de manera descendete por lo cual vamos a utilizar el metodo 'sort()' y la instruccion 'reverse=true'"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
col.sort(reverse=True)
print(col)
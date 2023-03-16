"""Continuando con las listas tenemos el metodo 'insert' con este podemos agregar registros a las listas con una posicion fija es
decir con un numero el cual le diga en posicion se tiene que colocar"""

"""Para este ejercicio tenemos que crear una lista con ciertos colores a la cual le vamos a agregar los colores 'magenta' y
'turquesa' estos los vamos a agregar on el metodo 'insert()' pero tendremos que utilizar los posicionamientos en negativos es
decir empezando a contar desde el '-1', otro objetivo que tenemos que tomar en cuenta es que el color 'magenta' debe de quedar
justo despues del color 'lila' y el color 'turquesa' en la penultima posicion"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
col.insert(-4, 'magenta')
col.insert(-1, 'turquesa')
"""Para poder colocar entonces los colores donde se nos pide tenemos que poner la instruccion 'insert(-4, 'magenta')' con el numero
'-4' y el String del color ('magenta') para poder hacer que quede justo despues del lila, mientras que para el 'turquesa' tenemos
que utilizar la posicion '-1' para poder hacer que quede en la penultima posicion"""

print(col)
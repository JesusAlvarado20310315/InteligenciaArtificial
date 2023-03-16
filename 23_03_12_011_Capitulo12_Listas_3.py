"""Continuando con las listas tenemos que hablar acerca de la instruccion 'del' la cual permite borrar un registro que se encuentre
en la lista que se menciona en la instruccion"""

"""El ejercicio nos pide que utilicemos la instruccion 'del' para eliminar los String de 'azul', 'marron', 'negro', 'rosa'. Para
ello declaramos la lista con todos los elementos seleccionados los cuales son los que vamos a eliminar"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
        #['rojo', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] Aqui eliminamos el "azul"
        #['rojo', 'verde', 'amarillo', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] Aqui eliminamos el "marron"
        #['rojo', 'verde', 'amarillo', 'lila', 'rosa', 'blanco', 'naranja'] Aqui eliminamos el "negro"
        #['rojo', 'verde', 'amarillo', 'lila', 'blanco', 'naranja'] Aqui eliminamos el "rosa"
del col[1]
del col[3]
del col[4]
del col[4]
"""Despues utilizamos la instruccion 'del' para borrar los registros del String 'azul' es el registro '1', al alterar la lista
original los registros se mueven por lo cual para el String 'marron' termina siendo el registro '3', por lo ya mencionado los
registros cambian por lo cual para el String 'negro' termina siendo el registro '4' y por ultimo continuando con el cambio de
registro para el String 'rosa' termina siendo el registro '4'"""

print(col)
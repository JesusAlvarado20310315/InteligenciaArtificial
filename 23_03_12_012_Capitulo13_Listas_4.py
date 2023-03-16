"""Continuando con las listas tenemos la instruccion 'remove()' la cual al igual que con la instruccion anterior de 'del()' esta
elimina algun registro de la lista pero en vez de ser la posicion utilizamos el valor o el String a eliminar"""

"""Para este ejemplo crearemos la lista llamada 'col' y con sus respectivos datos"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
col.remove('amarillo')
col.remove('rojo')
"""Una vez creada la lista utilizaremos la instruccion 'remove()' para eliminar los 2 datos solicitados el String de 'amarillo' y 
tambien el String de 'rojo' esto sin la necesidad de colocar que posicion tiene solo su dato"""

print(col)
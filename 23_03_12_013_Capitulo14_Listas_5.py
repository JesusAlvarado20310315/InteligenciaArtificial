"""Otra instruccion con la que cuentan las listas es la instruccion 'pop()' esta de la misma manera que la instruccion 'del()'
elimina de la lista los registros marcados en la instruccion pero lo que la diferencia que tiene con 'del()' es que esta puede
"""

"""Para este ejemplo se crea la variable llamada 'col' que es una lista la cual se llena con los valores mostrados"""
col = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
col1 = col.pop(1)
col2 = col.pop(7)
"""Aqui utilizamos la instruccion 'pop()' para eliminar y guardar los valores 'rojo' y 'blanco'. Para el String 'rojo' utilizamos
la instruccion 'pop(1)' en el numero '1' y para el String 'blanco' es la instruccion 'pop(7)' esto debido a que la lista cambia de
posicion debido a que primero quitmos el String 'rojo'"""
colgua = [col1, col2]
"""Para mostrar lo que se guardaron con la instruccion 'pop()' juntamos en otra lista las variables donde se utilizo la
instruccion y despues la imprimimos"""
print(colgua)
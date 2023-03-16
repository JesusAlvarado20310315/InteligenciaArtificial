"""Ahora veremos un nuevo elemento llamado 'Tuplas' las cuales son muy parecidas a las listas pero son muy diferentes ya que las
listas las podemos modificar de una manera mas facil pero las tuplas no es posible, estas son muy parecidas a las listas pero 
las tuplas se escriben con parentesis y pueden manejar diferente tipos de valores"""

"""Para ver como funcionan las tuplas tenemos esta actividad las cuales son declarar la tupla llamada 'col' y de esta podemos ver
los diferentes valores que tiene"""
col = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(col[1])
"""Aqui al final podemos ver el registro con el valor '1' en la tupla llamada 'col' el cual es el String 'Azul'"""

"""Por ejemplo en esta otra tupla tenemos valores numericos no Strings asi que estos los podemos ocupar para realizar una operacion
en la cual utilizamos los registros '0' + el resigtro '2' + el registro '3' - el registro '1'"""
num = (10, 1, 5, 11)
ope = num[0] + num[2] + num[3] - num[1]

print(ope)
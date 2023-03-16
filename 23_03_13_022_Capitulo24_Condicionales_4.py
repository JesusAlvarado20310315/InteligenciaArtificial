"""Al utilizar condicionales podemos utilizar estas para evaluar listas o tuplas para confirmar si una variable de cualquier tipo
se encuentre dentro de estas"""

"""Para este ejemplo vamos a crear una variable llamada 'col' la cual va a pedir un color al usuario por medio del metodo 'input'
despues vamos a crear una tupla 'tuplacol' la cual tendra ciertos colores ya especificados y estos son los colores que vamos a
verificar por medio de la condicional 'if'"""
col = input('Introduce un color:\n')
tuplacol = ('rojo', 'azul', 'verde', 'amarillo')

"""Para poder reviar la tupla vamos a poner de condicional la palabra 'in' la cual revisa lo que se encuentra dentro de la tupla
para poder verificar cada uno de los colores establecidos en la tupla tenemos que utilizar la condicional 'elif' ya que tenemos 
mas de 1 color que evaluar y esto nos permite verificar todo los colores que necesitemos, como condicion despues de la palabra 'in'
tenemos que poner la posicion de tupla que se quiera revisar"""
if col in tuplacol[0]:
	print('El color rojo está admitido')
elif col in tuplacol[1]:
	print('El color azul está admitido')
elif col in tuplacol[2]:
	print('El color verde está admitido')
elif col in tuplacol[3]:
	print('El color amarillo está admitido')
else:
	print('Color no admitido')
"""En este caso al tener 4 colores tenemos que utilizar la condicion 'if' 1 vez, despues tendremos que ocupar la condicion 'elif'
para poder hacer que revise los otros 3 colores y por ultimos tenemos que cerrar la condicional con su respectivo 'else' de esta
forma podemos verificar cada uno de los colores"""
"""En este capitulo empezamos a ver lo que serian los diccionarios estos nos permiten guardar varias variables con sus
respectivos valores dentro de una solo diccionario"""

"""Para el ejercicio de este capitulo utilizaremos el diccionario llamado 'teclado2' en el cual tenemos la primera variable
llamada 'Categoria' con su respectivo valor de 'Teclados', la segunda variable llamada 'Modelo' con su valor de 'Corsair K55
RGB' y la ultima variable llamada 'Precio' con su valor de '59.99'"""
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

"""Para imprimir lo que se nos pide tenemos que declarar en el 'print' el nombre del diccionario con unos parentesis
declarando dentro de estos con una comillas simples la variable que deseamos imprimir de tal manera que nos de su valor sin"""
print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')
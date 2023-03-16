"""En este capitulo se tomaron las operaciones basicas para explicar como funcionan en python"""

"""Cabe destacar que en estos casos tenemos que fijarnos muy bien que al momento de realizar alguna operacion la variable que
vallamos a utilizar sea un numero y no una cadena de caracteres. Asi tambien no es necesario declarar los numeros dentro de una
variable ya que estos pueden ser sumados de manera directa en la operacion la cual si tiene que ir en una variable"""
sum1 = 20
sum2 = 23
sum3 = 44
sumres = sum1 + sum2 + sum3
"""En la parte de arriba tenemos la suma (+) como operador principipal"""

res1 = 20
res2 = 23
res3 = 84
resres = res1 - res2 - res3
"""En la parte de arriba tenemos la resta (-) como operador principipal"""

mul1 = 20
mul2 = 23
mul3 = 20
mul4 = 21
mulres = mul1 * mul2 + mul3 * mul4
"""En la parte de arriba tenemos la multiplicacion (*) como operador principipal"""

div1 = 5000
div2 = 230
div3 = 2.1722
divres = div1 / div2 / div3
"""En la parte de arriba tenemos la multiplicacion (/) como operador principipal"""

ope1 = 10
ope2 = 5
ope3 = 15
ope4 = 17
resul = ope1 / ope2 + ope3 - ope4
"""En este ultimo ejercicio tenemos que utilizar los diferentes operadores para que el resultado final sea 0"""

print("La suma es:",sumres,"\nLa resta es:",resres,"\nLa multiplicacion es:",mulres,"\nLa division es:",divres)
print("El resultado de la operacion es:",resul)
"""Al final para poder visualizar los resultados los ponemos en un print el cual esta conformado por algunos Strings y las
variables que necesito imprimir despues de una coma"""
"""En este capitulo tenemos 3 ejercicios sobre concatenacion y cada uno tiene su propio print ya que imprimen cosas diferentes"""

"""En el primer ejemplo tenemos el como se concatenan diferentes Strings en la misma linea y en la misma variable utilizano el signo
de '+' al final podemos ver como es que se concatena en otra variable la cual se llama 'res1' y al final dentro de la instruccion
print tambien podemos concatenar otro String concatenandolo igual con un +"""
var1 = "Si" + " " + "se"
var2 = " puede concatenar"
res1 = var1 + var2
print(res1 + " 2 string")

"""En este segundo ejemplo tenemos al igual que en el anterior 2 varibles las cuales se concatenan en una tercera agregando un 
espacio entre cada variable por lo tanto al imprimirla en el print saldra con las 2 variables y 1 espacio entre ellas"""
nombre = "Jesus Eduardo"
apellido = "Alvarado Medrano"
nom_com = nombre + " " + apellido
print(nom_com)

"""En esta ultimo caso es importante destacar que las variables no son valores numericos son String los cuales tienen un caracter
numerico por lo cual al contanenar las variables no se sumaran si no que se podran el segundo al siguiente del primero"""
num1 = "2"
num2 = "5"
junta = num1 + num2
print(junta)
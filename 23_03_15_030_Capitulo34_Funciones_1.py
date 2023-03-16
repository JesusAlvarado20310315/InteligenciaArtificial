"""Para continuar con el curso tenemos las funciones las cuales se utilizan para guardar ya sean ciertos datos o hacer algo con ellos
de esta manera los puedas ocupar mas adelante sin la necesidad de volver a escribir varias veces el codigo y solo llamar la funcion
con lo que quieras que haga"""


"""Para el ejercicio teniamos que declarar una funcion la cual tuviera una suma dentro del ella asi como tambien una impresion de lo
que se va a realizar en este caso teniamos que hacer 3 sumas con un resultado de '30', '50' y '70', para ello primero teniamos que
declarar la funcion son cu palabra clave 'def' seguido de su nombre con unos parentesis; estos pueden ir vacios o pueden llevar los
datos que esta va a utilizar, para el ejemplo se le indico que va a tomar 2 valores numericos y dentro de la funcion tenemos que va a
imprimir la suma de los 2 valores numericos declarados"""
def suma(num1, num2):
	print(num1 + num2)

"""Ya por ultimo solo tenemos que llamar a la funcion y dentro de esta vamos a declarar los valores numericos que van a entrar dentro
de la funcion, para el primmer caso declaramos un 10 y un 20 para que la suma sea de 30, para el segundo caso declaramos un 20 y un 30
para que la suma sea 50 y para el ultimo caso declaramos un 50000 y un 7000 para que nos de de suma 57000"""
suma(10, 20)
suma(20, 30)
suma(50000, 7000)
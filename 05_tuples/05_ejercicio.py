# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprimela.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.
my_tuple = (100, 200, 300, 400, 500)
print(my_tuple[1])  

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
# my_tuple = (1, 2, 3)
# my_tuple[0] = 10
# print(my_tuple) # Esto genera un error

# 4. Cuenta cuantas veces aparece el numero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
my_tuple = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple.count(3))

# 5. Encuentra el indice de la primera aparicion de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
my_tuple = ("Java", "Python", "JavaScript", "Python")
print(my_tuple.index("Python")) # Devuelve 2

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tuple_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_concatenada = tuple_1 + tupla_2
print(tupla_concatenada)

# 7. Crea una subtupla con los elementos desde la posicion 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2:5])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" 
# y vuelve a convertirla en una tupla. Imprime la tupla resultante.
my_tuple = ("rojo", "verde", "azul")
lista = list(my_tuple)
lista[1] = "amarillo"
my_tuple = tuple(lista)
print(my_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3)
del my_tuple

# 10. Crea una tupla con un solo elemento (el numero 100) e impri­mela. 
# Asegurate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tuple = (100,)  # Asignar un solo elemento a la tupla con la sintaxis (100,)
print(tuple)
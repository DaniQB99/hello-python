# 1. Crea un set con los números 1, 2, 3, 4, 5 e imprimelo.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprí­melo.
my_set = {1, 2, 3, 4, 5}
my_set.add(6) # Añade el valor
print(my_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
my_set = {1, 2, 3, 4, 5}
my_set.add(5) # No se puede añadir el valor
print(my_set)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set) # True   

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set = {1, 2, 3, 4, 5}
my_set.remove(4) # Elimina el valor
print(my_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
my_set.clear() # Elimina todos los valores del set
print(len(my_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
my_set = {"manzana", "naranja", "plátano"}
my_list = list(my_set)
print(my_list[0])

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
my_set = {1, 2, 3}
my_other_set = {4, 5, 6}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
my_set = {1, 2, 3, 4}
my_other_set = {3, 4, 5, 6}
print(my_set.difference(my_other_set))

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
del my_set
# print(my_set) # Esto genera un error
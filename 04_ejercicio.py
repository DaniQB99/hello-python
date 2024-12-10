# 1. Crea una lista con los números del 1 al 5 e imprí­mela.
list = [1, 2, 3, 4, 5]
print(list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
new_list = [10, 20, 30, 40, 50]
print(new_list[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprí­mela.
list.append(6)
print(list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
new_list.insert(1, 15)
print(new_list)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
new_list.remove(30)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. 
# Imprime la variable y la lista.
pop_list = list.pop(5)
print(pop_list)
print(list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprí­mela.
reverse_list = [100, 200, 300, 400, 500]
print(reverse_list)

reverse_list.reverse()
print(reverse_list)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprí­mela.
sort_list = [3, 1, 4, 2, 5]
print(sort_list)

sort_list.sort()
print(sort_list)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
my_new_list = list_1 + list_2
print(my_new_list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
my_list = [10, 20, 30, 40, 50]
my_sublist = my_list[1:3]
print(my_sublist)
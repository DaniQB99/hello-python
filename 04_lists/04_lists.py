### LISTAS ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [25, 30 ,52, 62 , 41, 30]

print(my_list)
print(len(my_list))

my_other_list = [25, 1.73, "Daniel", "Quirós"] # Lista con varias variables

print(type(my_list)) # Type: list
print(type(my_other_list)) # Type: list

print(my_other_list[0]) # 25
print(my_other_list[1]) # 1.73
print(my_other_list[-1]) # Quirós
print(my_other_list[-2]) # Daniel
print(my_list.count(20))
#print((my_other_list[6])) # IndexError

age, height, name, surname = my_other_list # Desempaquetado de los atributos de la lista (Tiene que desempaquetarse todos los atributos)
print(name)

# AÑADIR VALOR
my_other_list.append("Daniqb99")
print(my_other_list)

# INSERTAR EN POSICIÓN CONCRETA
my_other_list.insert(1, "Rojo") # Insert
print(my_other_list)

my_other_list[1] = "Azul" # Posición de la lista
print(my_other_list)

# ELIMINAR VALOR
my_other_list.remove("Rojo")

my_list.remove(30) # Elimina el primer valor indicado de la lista

del my_list[2] # Elimina el valor de la posición indicada

print(my_list.pop()) # Elimina el último valor de la lista

print(my_list.pop(2)) # Elimina el valor de la posición asociado y te lo recoge 

my_new_list = my_list.copy() # Copia la lista

my_list.clear() # Elimina toda la lista

my_new_list.reverse() # Da la vuelta a la lista

my_new_list.sort() # Ordena de menor a mayor la lista


### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.78, "Daniel", "Quirós")
my_other_tuple = (30, 40, 55)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])
#print(my_tuple[-6])

print(my_tuple.count('Daniel'))
print(my_tuple.index('Quirós'))
print(my_tuple.index('Daniel'))

#my_tuple[1] = 1.80 # La tupla esta cerrada y no se puede modificar

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # Covertir a lista para poder modificarla
print(my_tuple)

my_tuple[3]= 'DanielQB'
my_tuple.insert(1, 'Azul')
print(tuple(my_tuple)) # Convertir de lista a tupla de nuevo

del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined






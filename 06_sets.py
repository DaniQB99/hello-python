### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'>
print(type(my_other_set)) # <class 'dict'>

my_other_set = {'Daniel', 'Quirós', 25}

my_other_set.add('Daniqb99') # Un set no admite valores repetidos

print('Daniel' in my_other_set) # True
print('Dani' in my_other_set) # False

my_other_set.remove('Daniel') # Elimina el valor
print(my_other_set)

my_other_set.clear() # Elimina todos los valores del set
print(len(my_other_set))

del my_other_set # Elimina el set

my_set = {'Daniel', 'Quirós', 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_new_set = {'Python', 'Java', 'C++', 'JavaScript'} # Crea un nuevo set
print(my_new_set.union(my_new_set).union({'SQL', 'HTML', 'CSS'})) # Agrega los elementos de los sets

print(my_new_set.difference(my_set)) # Elimina los elementos que están en el set
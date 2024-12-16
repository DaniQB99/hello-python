### DICTS ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {'Nombre': 'Daniel', 'Apellido': 'Quirós', 'Edad': 25, 1:'Python'}

my_dict = {
    'Nombre': 'Daniel',
    'Apellido': 'Quirós',
    'Edad': 25,
    'Lenguajes': {'Python', 'Java', 'C++'},
    1:1.75,
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

print(my_dict['Nombre']) # Daniel
my_dict['Nombre'] = 'Juan' # Cambia el valor

print(my_dict['Nombre']) # Juan

my_dict['Calle'] = 'Avd de Canovas' # Agrega un nuevo atributo
print(my_dict)

del my_dict['Calle'] # Elimina el valor
print(my_dict)

print('Daniel' in my_dict) # False
# print('Dani' in my_dict) # False
print('Nombre' in my_dict) # True

print(my_dict.items()) # Lista de los atributos y sus valores
print(my_dict.keys()) # Lista de los atributos
print(my_dict.values()) # Lista de los valores

my_new_dict = dict.fromkeys(('Nombre', 1)) # Crea un nuevo dict con los mismos atributos y valores
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, 'Daniqb99') # Crea un nuevo dict con los mismos atributos y valores
print(my_new_dict)

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict)) 

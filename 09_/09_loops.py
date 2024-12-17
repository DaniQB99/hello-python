### LOOPS ###

# While loop

my_condition = 0

while my_condition < 10:  # Se ejecuta hasta que la condicion se cumpla
    print(my_condition)
    my_condition += 1
else:  # Es opcional
    print('Mi condicion es falsa')


while my_condition < 20:  # Se ejecuta hasta que la condicion sea verdadera
    my_condition += 1
    if my_condition == 15:
        print('Mi condicion es 15')
        break
    print(my_condition)


# For loop

# List
my_list = [20, 29, 10, 52, 34, 15]
for element in my_list: # Se ejecuta una vez por elemento
    print(element)

# Set
my_set = {'Daniel', 'Quiros', 25}
for element in my_set:
    print(element)

# Tuple
my_tuple = ('Daniel', 'Quiros', 25)
for element in my_tuple:
    print(element)

# Dictionary
my_dict = {'Nombre': 'Daniel', 'Apellido': 'Quiros', 'Edad': 25, 'Pais': 'España'}
for element in my_dict:
    print(element)
    if element == 'Edad':
        continue  # Se salta el siguiente elemento
    print('Se ejecuta')
else:
    print('El diccionario ha terminado')


print('La ejecucion continua')
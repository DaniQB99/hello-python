str_variable = 'My String Variable'
print(str_variable)

int_variable = 25
print(int_variable)

bool_variable = False
print(bool_variable)

# Concatenacion de variables
print(str_variable, int_variable, bool_variable)

# Funciones del sistema
print(len(str_variable)) # len: Cuenta cuantos caracteres tiene la variable asociada a la funcion

# Variables en una sola linea
name, surname, alias, age = 'Daniel', 'Quiros', 'Dani', 25
print('Me llamo:', name, surname, '. Mi edad es:', age, '. Y mi alias es: ', alias)

# Inputs
first_name = input('Cual es tu nombre? ')
print('Hola ', first_name)

"""
Python no tiene un tipado especifo. Una variable predefinida con una valor cualquiera puede convertirse pasar 
a tener otro tipo de valor. 
    string -> int
    int -> string
    int -> bool
    ...
"""
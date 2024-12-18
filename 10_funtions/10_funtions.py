### FUNCTIONS ###

def my_function():
    print("Esto es una funcion")

my_function()

# Funciones con parametros

def sum_two_values(a, b):
    print(a + b)

sum_two_values(1, 2)
sum_two_values(456, 472)
sum_two_values('5', '7')
sum_two_values('hello', 'world')

# Funciones con parametros y retorno

def sum_two_values(a, b):
    return a + b

my_result = sum_two_values(1, 2)
print(my_result)

def print_name (name, surname, age = 25):
    print(f'{name} {surname} {age}')              

print_name('Daniel', 'Quiros')

def print_text(*texts):
    for text in texts:
        print(text)

print_text('Hola', 'Mundo')


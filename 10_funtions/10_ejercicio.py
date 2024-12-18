# 1. Crea una funcion llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". 
# Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name):
    if name:
        print(f'Hola, {name}')
    else:
        print('Hola, desconocido')
personalized_greeting('Daniel')

# 2. Escribe una funcion llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(a, b):
    return a * b 

# 3. Crea una funcion llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(number):
    return number % 2 == 0

# 4. Escribe una funcion llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text):
    return text.upper()

# 5. Crea una funcion llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos 
# y retorne la suma de todos ellos.
def arbitrary_sum(*numbers):
    return sum(numbers)

# 6. Escribe una funcion llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, 
# y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    return f'Hola, {name} {surname}'    

# 7. Crea una funcion llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponent):
    return base ** exponent

# 8. Escribe una funcion llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(a, b, c):
    return (a + b + c) / 3

# 9. Crea una funcion llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text):
    return len(text)

# 10. Escribe una funcion llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, 
# una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*messages):
    for message in messages:
        print(message.upper())
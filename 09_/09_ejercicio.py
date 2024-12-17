# 1. Usa un bucle while para imprimir los números del 1 al 10.
num = 1
while num < 10:
    print(num)
    num += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
num = 1
suma = 0
while num < 101:
    suma += num
    num += 1
print(suma) 

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
my_string = 'Python'
for letter in my_string:
    print(letter)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
num = 1
while num < 50:
    if num % 7 == 0:
        print(num)
        break
    num += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
my_dict = {'name': 'Brais', 'age': 37, 'country': 'Galicia'}
for key in my_dict:
    print(key)

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
num = 1
while num < 21:
    if num % 2 == 0:
        print(num)
    num += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
num = 10
for i in range(num, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
my_list = [30, 10, 30, 20, 30, 40]
count = 0
for element in my_list:
    if element == 30:
        count += 1
print(count)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
my_list = ['Pedro', 'Maria', 'Juan', 'Brais', 'Jose', 'Luis']
for name in my_list:
    if name == 'Brais':
        break
    print(name)
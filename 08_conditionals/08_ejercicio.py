# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
my_condition = 5
if my_condition > 0:
    print("El número es positivo")
elif my_condition < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
ege = input("Ingrese su edad: ")
if ege >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad") 

# 3. Escribe un programa que verifique si una cadena de texto está vací­a y muestre un mensaje en consecuencia.
my_string = ""
if my_string == "":
    print("La cadena de texto está vací­a")
else:
    print("La cadena de texto no está vací­a")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. 
# Si son iguales, muestra un mensaje indicando la igualdad.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El primer número es mayor")
elif num1 < num2:
    print("El segundo número es mayor")
else:
    print("Son iguales")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
num1 = int(input("Ingrese un número: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("El número es divisible por 3 y por 5")
else:
    print("El número no es divisible por 3 y por 5")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
num1 = int(input("Ingrese un número: "))
if num1 % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). 
# Si tiene 16 o 17 años, indica que puede votar con permiso especial.
age = int(input("Ingrese su edad: "))
if age >= 18:
    print("Puede votar")    
else:
    print("No puede votar")     

# 8. Crea un programa que solicite una contraseñaa al usuario y verifique si coincide con una contraseñaa predefinida. 
# Si no coincide, muestra un mensaje de error.
password = input("Ingrese su contraseña: ")
if password == "123456":
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")    

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
num1 = int(input("Ingrese un número: "))
if num1 >= 10 and num1 <= 20:
    print("El número está entre 10 y 20")
else:
    print("El número no está entre 10 y 20")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) 
# y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color = input("Ingrese un color: ")
if color == "rojo":
    print("Debe detenerse")
elif color == "amarillo":
    print("Estará alerta")
else:
    print("Avanzará")
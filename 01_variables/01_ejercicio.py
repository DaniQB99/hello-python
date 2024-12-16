# 1. Declara y asigna valores a las siguientes variables:

#	name: una cadena que contenga tu nombre.
name = 'Daniel Quiros Barroso'
#	age: un numero entero que represente tu edad.
age = 25
#	height: un numero flotante que represente tu altura.
height = 1.75
#	Imprime cada variable en una lÃ­nea separada.
print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuantos años tienes.
print('Tengo', str(age), 'años')

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. 
# Usa True o False segun corresponda e imprimela.
is_student = True
print(is_student)

# 4. Usa la funcion len() para calcular cuantos caracteres tiene tu nombre completo, almacenado en una variable.
print('Mi nombre tiene: ', len(name), 'caracteres')


# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. 
# Luego, imprime estos valores.
name, surname, city = 'Daniel', 'Quiros Barroso', 'Don Benito'
print('Mi nombre es', name, surname, 'y vivo en', city)

# 6. Usa la funcion input() para solicitar al usuario su color favorito y almacenalo en una variable color. 
# Luego, imprime el valor ingresado.
color = input('Cual es tu color favorito? ')
print('Tu color favorito es el', color)

# 7. Declara una variable fruit e inicializala con un valor. 
# Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = 'Manzana'
print('La primera fruta es:', fruit)
fruit = 'Sandia'
print('La segunda fruta es:', fruit)

# 8. Convierte un numero decimal, almacenado en la variable price, a un numero entero y luego impri­melo.
price = 1.5
print('El precio es', int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direccion 
# usando la funcion len(). Imprime el resultado.
adress = 'Calle San Pablo, 88'
address_len = len(adress)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurandote de que siempre sera un numero. 
# Luego, cambia su valor a un numero diferente y verifica el tipo de la variable con type().
phone: int = 924001122
print(type(phone))
phone = 123456789
print(phone)
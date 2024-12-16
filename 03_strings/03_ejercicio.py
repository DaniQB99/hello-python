# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola lí­nea.
print("Hola" + "Python")

# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprí­mela para ver el resultado.
string_salto_linea = "Hola \n Python"
print(string_salto_linea)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "Daniel", "Quirós Barroso", 25
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelos uno por uno.
string = "Python"
a, b ,c , d, e, f = string
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
string_1 = "Programación"
slice_string = string_1[3:7]
print(slice_string)

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.
reverse_string = string[::-1]
print(reverse_string)

# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprí­mela.
upper_string = "aprendiendo python"
print(upper_string.upper())

# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".
count_string = "Programación en Python"
print(count_string.count("n"))

# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
num_string = "12345"
print(num_string.isnumeric())
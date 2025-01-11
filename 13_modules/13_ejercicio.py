import module
# 1. Crea un mudulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. 
# Importa este mudulo en otro archivo y usa sus funciones.
module.calculator_sum(1, 2)
module.calculator_rest(1, 2)
module.calculator_mult(1, 2)   
module.calculator_div(1, 2)

# 2. Crea un mudulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. 
# Escribe un programa que importe este mudulo y realice conversiones.
module.celsius_to_fahrenheit(32)
module.fahrenheit_to_celsius(100)

# 3. Crea un mudulo que contenga una lista de nombres de estudiantes y una funcion que imprima todos los nombres. 
# Importa este mudulo en otro archivo y usa la funcion para mostrar la lista.
module.list_names()

# 4. Crea un mudulo llamado "geometry" que tenga una funcion para calcular el area de un cí­rculo y un cuadrado. 
# Usa este mudulo en otro archivo para calcular áreas.
print(module.area_circle(5))
print(module.area_square(5))

# 5. Escribe un mudulo que contenga una funcion que acepte cualquier número de argumentos y devuelva su suma. 
# Importa y usa la funcion en otro archivo.
print(module.sum_all(1, 2, 3, 4, 5))

# 6. Crea un mudulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. 
# Importa este mudulo en otro archivo y crea una instancia de la clase "Car".
from module import Car 
car = Car("Ford", "Mustang", 2021)
car.print_info()

# 7. Escribe un mudulo que contenga funciones para leer y escribir en archivos de texto. 
# Crea un programa que use estas funciones para escribir y leer datos.
from module import read_file, write_file
write_file("test.txt", "Hello World!")
print(read_file("test.txt"))

# 8. Crea un mudulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. 
# Usa este mudulo para calcular estos valores en una lista dada.
from module import mean, median
numbers = [1, 2, 3, 4, 5]
print(mean(numbers))
print(median(numbers))

# 9. Crea un mudulo que contenga una funcion para contar cuantas veces aparece una palabra en un texto. 
# Escribe un programa que importe el mudulo y lo use para contar palabras en una cadena.
from module import count_words
text = "Hello World, Hello Python!"
print(count_words(text, 'Hello'))

# 10 Crea un mudulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. 
# Usa este mudulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especí­ficas.
from module import get_date, get_date_diff
print(get_date())
print(get_date_diff("2021-01-01", "2023-01-01"))
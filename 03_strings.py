### STRINGS ###
my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


# FORMATEO

name, surname, age = "Daniel", "Quirós Barroso", 25

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Pasamos los datos formateados
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Indicamos los datos especificos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Mejor forma, pasamos los datos formateados

# DESEMPAQUETADO DE CARACTERES
lenguage = "Python"
a, b ,c , d, e, f = lenguage
print(a)
print(e)

# DIVISIÓN
lenguage_slice = lenguage[1:3] # Coge de la 1-3
print(lenguage_slice) 

lenguage_slice = lenguage[1:] # Coge de la 1 en adelante
print(lenguage_slice) 

lenguage_slice = lenguage[-2] # Empieza por el final y coge la 2ª posición
print(lenguage_slice) 

lenguage_slice = lenguage[0:6:2] # Coge de la posición 0 a la 6, saltando 2 carácteres
print(lenguage_slice) 

# REVERSE
reverse_lenguage = lenguage[::-1] # Escribe el texto al revés
print(reverse_lenguage) 

# FUNCIONES
print(lenguage.capitalize()) # Primera letra en mayúsculas
print(lenguage.upper()) # Todas las letra en mayúsculas
print(lenguage.count("t")) # Cuenta las letras que hay dentro de la función
print(lenguage.isnumeric()) # Dice si es numerico o no
print("1".isnumeric()) # Primera letra en mayúsculas
print(lenguage.lower()) # Todas las letras en minúsculas
print(lenguage.lower().isupper()) # Todas las letras en minúsculas + Valida si todas son minúsculas
print(lenguage.startswith("Py")) # Empieza con ()

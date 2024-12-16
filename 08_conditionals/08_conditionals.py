### CONDITIONALS ###

# if/elif/else

my_condition = True

if my_condition:
    print("Se ejecutará la condición")

print("La ejecución continúa aquí")

my_condition = 5 * 3

if my_condition > 10:
    print("La condición es verdadera")    
else:
    print("La condición es falsa")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 15:
    print("Es igual a 15")
else:
    print("Es menor que 10 o mayor que 20")

    
print("La ejecución continúa aquí")
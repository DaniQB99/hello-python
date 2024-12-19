### EXCEPTIONS ###

# Ejemplo de una excepción 

num1 = 1
num2 = 4
num2 = '2'

# Try except
try:
    result = num1 / num2
    print(f'El resultado es {result}')
except:
    print('Se ha producido un error')

# Try except else finally
try:
    print(num1 / num2)
except:
    print('Se ha producido un error')
else:
    print('Todo ha ido bien')
finally:
    print('Finalizando el programa')

# Excepciones por tipo
try:
    print(num1 + num2)
    print('No se ha producido ningún error')
except ValueError:
    print('Se ha producido un error de tipo ValueError')
except TypeError:
    print('Se ha producido un error de tipo TypeError')

# Excepciones personalizadas
try:
    print(num1 + num2)
    print('No se ha producido ningún error')
except ValueError as error:
    print(error  )
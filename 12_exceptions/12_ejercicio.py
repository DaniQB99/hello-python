# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de division (por ejemplo, division por cero).
def divide(num1, num2):
    try:
        result = num1 / num2
        print(f'El resultado es {result}')
    except ZeroDivisionError:
        print('No se puede dividir por cero')

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversion.
def convert_to_number(string):
    try:
        number = int(string)
        print(f'El número es {number}')
    except ValueError:
        print('No se puede convertir a entero')

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). 
# Usa try-except para gestionar las operaciones de archivos de forma segura.
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f'El contenido del archivo es {content}')
    except FileNotFoundError:
        print('No se pudo encontrar el archivo')

# 4. Crea una función que realice múltiples operaciones (suma, resta, division, multiplicacion) con dos números. 
# Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def perform_operations(num1, num2):
    try:
        print('Suma:', num1 + num2)
        print('Resta:', num1 - num2)
        print('División:', num1 / num2)
        print('Multiplicación:', num1 * num2)
    except ZeroDivisionError:
        print('Se ha producido un error')
    else:
        print('Todo ha ido bien')
    finally:
        print('Finalizando el programa')

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. 
# Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def get_age():
    try:
        age = int(input('Ingrese su edad: '))
        if age <= 0:
            raise ValueError('La edad debe ser un número entero positivo')
        print(f'Tu edad es {age}')
    except ValueError as error:
        print(error)

# 6. Crea una función que intente acceder a un elemento de una lista por í­ndice. Usa try-except para manejar el caso donde el í­ndice esta fuera de rango.
def access_list(list, index):
    try:
        element = list[index]
        print(f'El elemento es {element}')
    except IndexError:
        print('El índice no es válido')

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def multiple_exceptions(num1, num2):
    try:
        result = num1 / num2
        print(f'El resultado es {result}')
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    except ValueError:
        print('Error: Valores no válidos')
    except TypeError:
        print('Error: Tipos no compatibles')

# 8. Crea una función que simule una transaccion. Lanza una excepcion personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
class InsufficientFundsError(Exception):
    pass

def simulate_transaction(balance, amount):
    if balance < amount:
        raise InsufficientFundsError('No hay suficiente fondos')
    else:
        balance -= amount
        print(f'Se ha retirado {amount} de su saldo')   

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.
def convert_list_to_numbers(list):
    try:
        numbers = [int(num) for num in list]
        print(f'Los números son {numbers}')
    except ValueError:
        print('No se pueden convertir a enteros')
# 10. Crea una función que calcule la raí­z cuadrada de un número. Lanza un ValueError si el número es negativo.
def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError('El número debe ser un número positivo')
        return number ** 0.5
    except ValueError as error:
        print(f'Error: {error}')
    
### CLASSES ###

# Clase con atributos dentro de la clase
class Person: 
    def __init__(self):
        self.name = 'Daniel'
        self.age = 25

my_person = Person()

print(f'{my_person.name}{my_person.age}') 


# Clase con atributos asociados a un atributo 
class Person: 
    def __init__(self, name, surname, age = 25): # __init__ es un metodo especial que se ejecuta cuando se crea una nueva instancia de la clase
        self.full_name = f'{name} {surname} {age}'
 
    def walk(self): 
        print(f'Hola {self.full_name} esta caminando')

my_person = Person('Daniel', 'Quiros')

print(my_person.full_name) # 'Daniel Quiros'
my_person.walk() # 'Hola Daniel Quiros esta caminando'

my_other_person = Person('Juan', 'Perez', 30)
print(my_other_person.full_name) # 'Juan Perez 30'
my_other_person.walk() # 'Hola Juan Perez 30 esta caminando'
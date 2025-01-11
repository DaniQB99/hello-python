### EJERCICIO 1 ###

def calculator_sum(num1, num2):
    print(num1 + num2)

def calculator_rest(num1, num2):
    print(num1 - num2)

def calculator_mult(num1, num2):
    print(num1 * num2)

def calculator_div(num1, num2):
    print(num1 / num2)

### EJERCICIO 2 ###

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

### EJERCICIO 3 ###

student_names = ["Africa", "Paco", "Daniel", "Joel", "Maria"]

def list_names():
    for name in student_names:
        print(name)

### EJERCICIO 4 ###

import math

def area_circle(radius):
    area = math.pi * radius ** 2
    return area

def area_square(side):
    area = side * side
    return area

### EJERCICIO 5 ###

def sum_all(*args):
    return sum(args)

### EJERCICIO 6 ###

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

### EJERCICIO 7 ### 

def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

### EJERCICIO 8 ###

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (sorted_numbers[middle-1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]
    
### EJERCICIO 9 ###

def count_words(text, word):
    return text.lower().count(word.lower())

### EJERCICIO 10 ###

from datetime import datetime

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_date_diff(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)
# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#  1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#  2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#  3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
import math

def isPrime(number):
    if number < 2:
        return False
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for num in range(5, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    
    return True
        

def prime_numbers(numbers_list):
    primes_list = []
    for number in numbers_list:
        if isPrime(number):
            primes_list.append(number)
        
    
    return primes_list
            
    
print(f'Ejemplo 1: {prime_numbers([1, 4, 6, 7, 13, 9, 67])}')
print(f'Ejemplo 2: {prime_numbers([29, 25, 37, 42 , 49, 88 , 89, 97])}')
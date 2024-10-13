# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

def sum_list_numbers(number_list):
    total = 0
    for number in number_list:
        total += number
    
    return total

print(f'Ejemplo 1: {sum_list_numbers([4, 6, 2, 29])}')
print(f'Ejemplo 2: {sum_list_numbers([4, 9, 27, 35, -21])}')
# 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8`]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11]
even_numbers_list = []
for index in range(0, len(number_list)):
    if number_list[index] % 2 != 0:
        odd_numbers_list = [number_list[index]]
        print(f'numero eliminado {number_list[index]}')
    else:
        even_numbers_list.append(number_list[index])

print(f'lista de numeros pares {even_numbers_list}')
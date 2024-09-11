# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def reverse_string(str):
    new_str = ""
    for char in range(len(str), 0, -1):
        new_str += str[char - 1]
    return new_str

reversed_string_ex1 = reverse_string("Hola mundo")
reversed_string_ex2 = reverse_string("This is a super long phrase that is super fun to revert")

print(f'Ejemplo 1: {reversed_string_ex1}')
print(f'Ejemplo 2: {reversed_string_ex2}')

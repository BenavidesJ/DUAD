# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = 'Pizza con piña'

for char in range(len(my_string) - 1, 0, -1):
    print(my_string[char - 1])
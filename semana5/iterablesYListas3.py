# Cree un programa que intercambie el primer y 
# ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [9, 3, 6, 1, 7,21,8,75]

print(f'Lista inicial: {my_list}')

primer_elemento = my_list[0]
ultimo_elemento = my_list[len(my_list) - 1]

for index in range(0, len(my_list)):
    if index == 0:
        my_list[index] = ultimo_elemento
    elif index == (len(my_list) - 1):
        my_list[(len(my_list) - 1)] = primer_elemento
    else:
        continue

print(f'Lista modificada: {my_list}')
    
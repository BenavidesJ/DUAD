# Cree un programa que le pida al usuario 10 números,
#  y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

posicion = 0
lista_numeros = []
mayor = 0

while posicion <= 10:
    numero_ingresado = int(input('Ingrese un número\n'))
    if numero_ingresado > mayor:
        mayor = numero_ingresado

    # lista_numeros.insert(posicion, numero_ingresado)
    lista_numeros.append(numero_ingresado)
    posicion += 1

print(f'Los numeros ingresados son {lista_numeros} y el mas alto ingresado es {mayor}')
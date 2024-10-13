# Cree un programa que le pida tres números al usuario y muestre el mayor.

numero_mayor = 0
contador = 1


while contador <= 3:
    numero_ingresado = int(input("Ingrese un numero"))

    if numero_ingresado > numero_mayor:
        numero_mayor = numero_ingresado

    contador += 1

print(f'El numero mayor es {numero_mayor}')

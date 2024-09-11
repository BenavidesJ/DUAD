# Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.
import random

numero_secreto = random.randint(1, 10)
numero_adivinado = 0

while numero_adivinado != numero_secreto:
    numero_adivinado = int(input('Ingrese un numero\n'))
    if numero_adivinado != numero_secreto:
        print('Número equivocado, Intentelo nuevamente!')

print('Felicidades adivino el numero secreto')
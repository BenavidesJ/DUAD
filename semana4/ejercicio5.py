# Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.

contador_de_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input('Ingrese la cantidad de notas a calcular\n'))

while contador_de_nota <= total_de_notas:

    nota_actual = int(input(f'Ingrese la nota # {contador_de_nota}\n'))

    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas += nota_actual

    promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)

    contador_de_nota += 1

promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas

print(f''' 
    El estudiante tiene {cantidad_de_notas_desaprobadas} notas desaprobadas,
    ademas tiene {cantidad_de_notas_aprobadas} notas aprobadas,
    El promedio de las notas aprobadas es {promedio_de_notas_aprobadas},
    mientras que el promedio de las notas desaprobadas es {promedio_de_notas_desaprobadas},

    El promedio total de notas es {promedio_de_notas_total}
''')
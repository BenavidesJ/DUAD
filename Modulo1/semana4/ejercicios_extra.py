precio_producto = float(input('Ingrese el precio del producto\n'))
precio_producto_descuento = 0

if precio_producto < 100:
    precio_producto_descuento = precio_producto - precio_producto * 0.02
else:
    precio_producto_descuento = precio_producto - precio_producto * 0.10

print(f'El precio del producto es {precio_producto_descuento}')

diez_minutos_en_segundos = 10 * 60
tiempo_segundos = int(input('Ingrese la cantidad de segundos que desea comparar\n'))

if tiempo_segundos < diez_minutos_en_segundos:
    tiempo_faltante = diez_minutos_en_segundos - tiempo_segundos
    print(f'Faltan {tiempo_faltante} segundos para llegar a 10 minutos')

else:
    print('Mayor')

numero_ingresado = int(input('Ingrese un numero\n'))
suma = 0
contador = 1

while contador <= numero_ingresado:
    suma += contador
    contador += 1

print(f'La suma de todos los numeros hasta {numero_ingresado} es = {suma}')

primer_numero = int(input('Ingrese un numero\n'))
segundo_numero = int(input('Ingrese otro numero\n'))

if primer_numero > segundo_numero:
    auxiliar = primer_numero
    primer_numero = segundo_numero
    segundo_numero = auxiliar

print(f'A: {primer_numero} B: {segundo_numero}')

cantidad_hombres = 0
cantidad_mujeres = 0
promedio_hombres = 0
promedio_mujeres = 0
contador = 1

print('Calculo de porcentaje de hombres y mujeres')
while contador <= 6:
    sexo_ingresado = int(input('Ingrese un 1 para mujer, 2 si es hombre\n'))

    if sexo_ingresado == 1:
        cantidad_mujeres += 1
    elif sexo_ingresado == 2:
        cantidad_hombres += 1
    else:
        print('Ingrese una opcion correcta\n')

    contador += 1

promedio_mujeres = ( cantidad_mujeres / 6 ) * 100
promedio_hombres = ( cantidad_hombres / 6 ) * 100

print(f'El promedio de hombres es: {promedio_hombres} y el de mujeres es: {promedio_mujeres}')


# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

"""Funcion para sumar dos numeros
    params: num type int, entered_num type int
    return: int
    
    cuando tiene un error lo muestra por consola y retorna el
    valor actual a 0
"""
def add(num, entered_num):
    print(f'El valor actual es: {num}') 
    try:
        result = entered_num + num
        return result
    except Exception as error:
        print(f'La suma no se puede realizar. Error: {error}')
        return 0
    

"""Funcion para restar dos numeros
    params: num type int, entered_num type int
    return: int
    
    cuando tiene un error lo muestra por consola y retorna el
    valor actual a 0
"""        
def diff(num, entered_num):
    print(f'El valor actual es: {num}')  
    try:
        if num > 0:
            result = num - entered_num
        else:
            result = entered_num - num   
        return result
    except Exception as error:
        print(f'La resta no se puede realizar. Error: {error}')
        return 0
    
    
"""Funcion para multiplicar dos numeros
    params: num type int, entered_num type int
    return: int

    cuando tiene un error lo muestra por consola y retorna el
    valor actual a 0
"""
def mult(num, entered_num):
    print(f'El valor actual es: {num}')  
    try:
        result = entered_num * num
        return result
    except Exception as error:
        print(f'La multiplicacion no se puede realizar. Error: {error}')
        return 0
    
    
"""Funcion para dividir dos numeros
    params: num type int, entered_num type int
    return: int
    
    cuando tiene un error lo muestra por consola y retorna el
    valor actual a 0
"""
def div(num, entered_num):
    print(f'El valor actual es: {num}')  
    try:
        if num > 0:
            result = num / entered_num
        else:
            result = entered_num / num  
        return result
    except Exception as error:
        print(f'La division no se puede realizar. Error: {error}')
        return 0
    
    
"""Funcion para limpiar resultados
    params: NO
    return: int
"""      
def eliminate_result():
    result = 0
    return result


"""Funcion para mostrar el menu al usuario
    y capturar su opcion elegida
    
    params: NO
    return: int
""" 
def print_menu():
    option = int(input(""" ***Calculadora por linea de comandos*** 
    Ingrese alguna de las siguientes opciones:
    1. Sumar
    2. Restar
    3. Mutiplicar
    4. Dividir
    5. Borrar resultado\n """))
    return option

"""Metodo main
    
    params: NO
    return: NO
""" 
def main():
    actual_value = 5
    
    def capture_user_number():
        print(f' Valor actual = {actual_value}\n')
        user_number = int(input('Ingrese un numero!\n'))
        return user_number
    
    while True:
        try:
            menu_option = print_menu()
            if int(menu_option) == 1:
                number = capture_user_number()
                actual_value = add(actual_value, number)
            elif int(menu_option) == 2:
                number = capture_user_number()
                actual_value = diff(actual_value, number)
            elif int(menu_option) == 3:
                number = capture_user_number()
                actual_value = mult(actual_value, number)
            elif int(menu_option) == 4:
                number = capture_user_number()
                actual_value = div(actual_value, number)
            elif int(menu_option) == 5:
                actual_value = eliminate_result()
            else:
                print('Esa no es una opcion correcta!\n')
                  
            print(f'El resultado de la operacion es: {actual_value}\n')   
        except KeyboardInterrupt:
            ## el ciclo se rompe al presionar control + C
            print(f'Fin de la ejecucion de la calculadora! Vuelve pronto!!\n')
            break
        except Exception as error:
            ## En caso de error se rompe el ciclo
            print(f'Se ha producido un error:\n ---> {error}')
            break


"""Programa: Calculadora de consola
""" 
if __name__ == '__main__':
	main()
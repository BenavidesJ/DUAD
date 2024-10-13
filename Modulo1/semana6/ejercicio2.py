# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

def my_important_function():
    list_odd_numbers = [1,3,5,7,9]
    
print(f'Access a local variable from outside a function {list_odd_numbers}')

## en este caso VScode me muestra un warning que dice: "list_odd_numbers" is not defined
# y al correr el script en consola se muestra el siguiente error:
#  File "d:\FullStack_Programa\Python\semana6\ejercicio2.py", line 8, in <module>
#     print(f'Access a variable from outside a function {list_odd_numbers}')    
#                                                        ^^^^^^^^^^^^^^^^
# NameError: name 'list_odd_numbers' is not defined

list_even_numbers = [0,2,4,6,8,10]

def add_more_even_numbers():
    more_even_numbers = [12,14,16,18,20]
    list_even_numbers.extend(more_even_numbers)

add_more_even_numbers()

print(f'Access and modify a global variable inside a function {list_even_numbers}')
# en este caso la variable global fue accesada desde la funcion y se le logro
# cambiar valores por lo que se puede decir que la lista inicial se muto
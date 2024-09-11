# 1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
print('hola' + 'mundo') # res= holamundo concatenacion
# print('hola' + 5) # res= error TypeError: can only concatenate str (not "int") to str
# print(97 + 'hola') # res= error TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(['a', 1, 'b', 17.89] + ['x', 987, 'y', 'mundo', '@']) # res= ['a', 1, 'b', 17.89, 'x', 987, 'y', 'mundo', '@'] union de listas
# print('hola' + ['a', 1, 'b', 17.89]) # res= error can only concatenate str (not "list") to str
print(19.64 + 5) # res= 24.64
print(19 + 51.97) # res= 70.97
print(True + True) # res= 2 ??
print(False + True) # res= 1 ??
print(True + False) # res= 1 ??

print(bool(True) + bool(False)) #res = 1
print(int(True), int(False)) # True = 1, False = 0

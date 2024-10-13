list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

deleted_data = []

for key in list_of_keys:
    if key in employee:
        deleted = employee.pop(key)
        deleted_data.append(f'key: {key}, data: {deleted}')

print(f' Resultado Ejercicio 3: {employee}\n')
print(f' Lista de datos eliminados del diccionario: {deleted_data}\n')
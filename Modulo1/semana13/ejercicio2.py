# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
# y arroje una excepción de no ser así.

def validate_params(fn):
    def wrapper_function(*params):
        params_list = list(params)
        for idx, p in enumerate(params_list):
            if not isinstance(p, (int, float)):
                raise ValueError(f'El parametro ingresado => {p} <= en la posicion => {idx + 1} <= no es un numero')
            
        return fn(*params)
        
    return wrapper_function


@validate_params
def suma_varios_numeros(*nums):
    result = sum(nums)
    return result

print(suma_varios_numeros(5,10,8,-5)) # esto funciona bien
print(suma_varios_numeros(5,10.98,8,-57.35)) # esto funciona bien
print(suma_varios_numeros(5,10.98,8,'a')) # esto debe retornar un error y mostrar cual es el error
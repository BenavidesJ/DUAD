# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def log_function_details(fn):
    def wrapper_function(*params):
        
        params_list = list(params)
        
        result = fn(*params)
        
        print(f'Function {fn.__name__}: params {params_list} => return {result}')
        
        return result
    return wrapper_function


@log_function_details
def suma(a, b):
    result = a + b
    return result


@log_function_details
def concatenate_strings(a, b, c):
    greeting = f'{a} {b} {c}!!!!!!!'
    return greeting

suma(5,7)
concatenate_strings('Hello','World', 'of Python')
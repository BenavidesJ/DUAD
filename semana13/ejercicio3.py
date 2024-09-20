# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
#     Luego cree un decorador para funciones que acepten un `User` 
# como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.
from datetime import date

def check_is_adult(fn,  *args, **kwargs):
    def wrapper(user: User):
        if user.age < 18:
            raise ValueError(f'El usuario no es mayor de edad')
        return fn(user, *args, **kwargs)
    return wrapper


class User:
    start_date = date(1960, 1, 1)
    def __init__(self, date_of_birth= start_date):
        self.date_of_birth = date_of_birth
        self.age = self.calculate_age()
        
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age
        
juan = User()
maria = User(date(1990,6,5))
carlos = User(date(2018,8,30))

@check_is_adult
def access_to_pub(user: User):
    print(f'Welcome to the pub!!! you are {user.age} old!')
    
access_to_pub(juan) # este es mayor de edad
access_to_pub(maria) # este es mayor de edad
access_to_pub(carlos) # este es menor de edad y debe fallar
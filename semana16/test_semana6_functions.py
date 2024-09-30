## copie las funciones aca, debido a que me da un error porque importar las funciones desde la carpeta de semana6
# no es posible, ya que esa carpeta no funciona como modulo. Como el ejercicio es de unit testing especificamente
# voy a hacerlo de esta manera
import math
import pytest

def count_capital_lower_chars(str):
    count_upper = 0
    count_lower = 0
    for char in str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    return f'There is {count_upper} upper cases and {count_lower} lower cases'


def isPrime(number):
    if number < 2:
        return False
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for num in range(5, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    
    return True
        

def prime_numbers(numbers_list):
    primes_list = []
    for number in numbers_list:
        if isPrime(number):
            primes_list.append(number)
        
    
    return primes_list

def test_count_capital_lower_chars_in_phrase():
    phrase= "test PHRASE"
    
    result = count_capital_lower_chars(phrase)
    
    assert result == "There is 6 upper cases and 4 lower cases"
    
def test_count_capital_lower_chars_in_phrase_wrong_params():
   with pytest.raises(TypeError, match="'int' object is not iterable"):
        count_capital_lower_chars(123456)
        
        
def test_is_prime():
    no_prime_number= 15
    prime_number = 13
    
    result = isPrime(no_prime_number)
    result2 = isPrime(prime_number)
    
    assert result == False
    assert result2 == True
    
def test_prime_numbers_list():
   numbers_list = [2, 4, 3, 5, 7, 9, 11, 12]
   
   result = prime_numbers(numbers_list)
   
   assert result == [5, 7, 11]
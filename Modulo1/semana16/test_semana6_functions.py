## copie las funciones aca, debido a que me da un error porque importar las funciones desde la carpeta de semana6
# no es posible, ya que esa carpeta no funciona como modulo. Como el ejercicio es de unit testing especificamente
# voy a hacerlo de esta manera
import pytest
from semana6.ejercicio3 import sum_list_numbers
from semana6.ejercicio4 import reverse_string
from semana6.ejercicio5 import count_capital_lower_chars
from semana6.ejercicio6 import sort_list_of_words
from semana6.ejercicio7 import isPrime, prime_numbers


def test_sum_list_numbers():
    list_numbers = [4, 6, 2, 29]
    
    result = sum_list_numbers(list_numbers)
    
    assert result == 41
    
    
def test_sum_list_numbers():
    no_list_numbers = ['a', 'b', 'c']
    
    with pytest.raises(TypeError):
        sum_list_numbers(no_list_numbers)


def test_reverse_string():
    test_phrase = "Hola mundo"
    result = reverse_string(test_phrase)
    assert result == "odnum aloH"
  
    
def test_reverse_string_empty():
    test_phrase = ""
    result = reverse_string(test_phrase)
    assert result == ""
  
    
def test_reverse_string_special_chars():
    test_phrase = "!@#$$#@!"
    result = reverse_string(test_phrase)
    assert result == "!@#$$#@!"


def test_sort_list_of_words():
    test_phrase = "python-variable-funcion-computadora-monitor"
    result = sort_list_of_words(test_phrase)
    assert result == "computadora-funcion-monitor-python-variable"


def test_sort_list_of_words_repeated():
    test_phrase = "apple-banana-apple-cherry-banana"
    result = sort_list_of_words(test_phrase)
    assert result == "apple-apple-banana-banana-cherry"


def test_sort_list_of_words_sorted():
    test_phrase = "ant-bat-cat-dog"
    result = sort_list_of_words(test_phrase)
    assert result == "ant-bat-cat-dog"


def test_count_capital_lower_chars_in_phrase():
    phrase= "test PHRASE"
    
    result = count_capital_lower_chars(phrase)
    
    assert result == "There is 6 upper cases and 4 lower cases"
    
    
def test_count_capital_lower_chars_in_phrase_wrong_params():
   with pytest.raises(TypeError, match="'int' object is not iterable"):
        count_capital_lower_chars(123456)
      
        
def test_count_capital_lower_chars_in_phrase_empy_params():
   with pytest.raises(TypeError):
        count_capital_lower_chars()
        
        
def test_is_prime():
    prime_number = 13
    
    result = isPrime(prime_number)
    
    assert result == True


def test_is_prime_no_prime_number():
    no_prime_number= 15
    
    result = isPrime(no_prime_number)
    
    assert result == False
    
    
def test_is_prime_number_one():
    result = isPrime(1)
    assert result == False
   
   
    
def test_prime_numbers_list():
   numbers_list = [2, 4, 3, 5, 7, 9, 11, 12]
   
   result = prime_numbers(numbers_list)
   
   assert result == [5, 7, 11]
   
   
   
def test_prime_numbers_list_with_str_list():
   no_numbers_list = ['a', 'b', 'c']
   with pytest.raises(TypeError):
        prime_numbers(no_numbers_list)
      
      
        
def test_prime_numbers_list_with_no_params():
    no_numbers_list = []
    result = prime_numbers(no_numbers_list)
    assert result == []
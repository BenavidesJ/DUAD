# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_list_of_words(list_of_words_str):
    separator = "-"
    words_list = list_of_words_str.split(separator)
    words_list.sort()
    return separator.join(words_list)
    
print(f' Primer ejemplo: {sort_list_of_words('python-variable-funcion-computadora-monitor')}')
print(f' Segundo ejemplo: {sort_list_of_words('music-headphones-car-violin-guitar-house-dog-cat')}')
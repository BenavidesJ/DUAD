# Ejercicios

1. Analice el algoritmo de `bubble_sort` usando la Big O Notation.

```python
def bubble_sort(list_to_sort):
    for outer_idx in range(0, len(list_to_sort) - 1): #O(n)
        already_swapped = False
        for idx in range(0, len(list_to_sort) - 1 - outer_idx): #O(n) como son dos ciclos anidados se convierne en O(n^2)

        #Hay casos en los que si la lista ya se encuentra ordenada que solo recorreria la lista una sola vez
            current_element = list_to_sort[idx]
            next_element = list_to_sort[idx + 1]

            if current_element > next_element:
                list_to_sort[idx] = next_element
                list_to_sort[idx + 1] = current_element
                already_swapped = True

        if not already_swapped:
            return
```

Entonces del algoritmo anterior se puede deducir:

- En el caso que la lista ya este ordenada O(n)
- Pero para la mayoria de los casos, (que es cuando medimos realmente la complejidad algoritmica) es un O(n^2)

2. Analice los siguientes algoritmos usando la Big O Notation:

## print_numbers_times_2

```python
def print_numbers_times_2(numbers_list):
    for number in numbers_list: # O (n)
        print(number * 2) # O(1)
        # como solo hay un ciclo podriamos decir que la complejidad es un O(n)
```

Entonces se puede deducir que la funcion anterior es un O(n)

## check_if_lists_have_an_equal

```python
def check_if_lists_have_an_equal(list_a, list_b):
    for element_a in list_a: #O(n)
        for element_b in list_b:# O(m) porque no intera sobre los elementos de list_a sino de otra lista list_b de m elementos
            if element_a == element_b: # la comparacion es O(1)
                return True
    return False
```

Entonces se puede deducir que la funcion anterior es un O(n\*m)

## print_10_or_less_elements

```python
def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print) # O(1) Investigando, en python la longitud se almacena internamente y no se requiere recorrer la lista como pareceria a un inicio
    for index in range(min(list_len, 10)): # O(1) porque recorre la lista solo 10 veces SIEMPRE
        print(list_to_print[index]) # O(1)
```

Entonces se puede deducir que la funcion anterior es un O(1) ya que en el peor de los casos el nivel de complejidad es constante debido a que sin importar el tamano de la lista el bucle esta limitado a 10

## generate_list_trios

```python
def generate_list_trios(list_a, list_b, list_c):
    result_list = []
    for element_a in list_a: # O(n)
        for element_b in list_b: # O(m)
            for element_c in list_c: # O(p)
                result_list.append(f'{element_a} {element_b} {element_c}') # O(1)
    return result_list
```

Entonces se puede deducir que el algoritmo anterior tiene una complejidad de O (n _ m _ p)
en este caso el tiempo de ejecucion crece en funcion del tamano de las tres listas, se multiplica

# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_capital_lower_chars(str):
    count_upper = 0
    count_lower = 0
    for char in str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    return f'There is {count_upper} upper cases and {count_lower} lower cases'
        
        
print(count_capital_lower_chars('I love Nación Sushi'))
print(count_capital_lower_chars('This is a super fun string that I Want To check How Many Lower case chars AND how MANY Uppers are'))
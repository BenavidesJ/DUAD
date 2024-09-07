# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def print_hello_world():
    print_important_message()
    print('Hello!, this is my first function in python.... or not? :D')
    
def print_important_message():
    print('Attention please: This is an important message!!')
    
print_hello_world()
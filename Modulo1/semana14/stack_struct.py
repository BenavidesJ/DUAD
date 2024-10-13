# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

from Node import Node
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        
        
    def pop(self):
        if self.length == 0:
            return
        else:
            pointer = self.top
            self.top = self.top.next
            pointer.next = None
        self.length -= 1
        
    def print_structure(self):
        pointer = self.top
        while (pointer is not None):
            print(pointer.value, end=" => ")
            pointer = pointer.next    
        print("Null")
        
print('Utilizacion de stack')
my_stack = Stack(5)
my_stack.push('2nd')
my_stack.push(99)
my_stack.print_structure()
print('---------------------')
my_stack.pop()
my_stack.print_structure() 
# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

from Node import Node

class Double_Ended_Node(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None
        
class Double_Ended_Queue:
    def __init__(self, value):
        new_node = Double_Ended_Node(value)
        self.left = new_node
        self.right = self.left
        self.length = 1
        
    def push_right(self, value):
        new_node = Double_Ended_Node(value)
        if (self.left is None):
            self.left = new_node
            self.right = new_node
        else:
            self.right.next = new_node
            new_node.prev = self.right
            self.right = new_node
        self.length += 1
    
    def pop_right(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.left = None
            self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None
        self.length -= 1
    
    def push_left(self, value):
        new_node = Double_Ended_Node(value)
        if self.left is None:  
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        self.length += 1
    
    def pop_left(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.left = None
            self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        self.length -= 1

    def print_structure(self):
        pointer = self.left
        while pointer is not None:
            print(pointer.value, end=" => ")
            pointer = pointer.next
        print("Null")
        
print('Utilizacion de double ended queue')
my_dbe_queue = Double_Ended_Queue('Hello')
my_dbe_queue.push_left('This is coming first')
my_dbe_queue.push_right('This is coming last')
my_dbe_queue.push_left('Other coming first')
my_dbe_queue.print_structure()
print('----------------------------')
my_dbe_queue.pop_left()
my_dbe_queue.pop_right()
my_dbe_queue.print_structure()
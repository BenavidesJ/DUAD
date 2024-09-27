from Node import Node
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    
    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def dequeue(self):
        pointer = self.head
        self.head = pointer.next
        self.length -= 1
        
    def print_structure(self):
        pointer = self.head
        while (pointer is not None):
            print(pointer.value, end=" => ")
            pointer = pointer.next
        print("Null")

print('Utilizacion de Queue')       
my_queue = Queue(11)
my_queue.enqueue(3)
my_queue.enqueue(23)
my_queue.print_structure()
print('-----------------')
my_queue.enqueue('Hello')
my_queue.print_structure()
my_queue.dequeue()
print('-----------------')
my_queue.print_structure()
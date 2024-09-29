class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def print_structure(self):
        pointer = self.head
        while (pointer is not None):
            print(pointer.value, end=" =next=> ")
            pointer = pointer.next
        print("Null")
        
    def get_node_by_index(self, index):
        if index < 0 or index >= self.length:
            return None
        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer
    
    def set_node_to_index(self,index, value):
        pointer = self.get_node_by_index(index)
        if pointer is not None:
            pointer.value = value
        
        return pointer
        
    def linked_list_bubble_sort(self):
        for outer_idx in range(0, self.length - 1):
            already_swapped = False
            for idx in range(0, self.length - 1 - outer_idx):
                current_node = self.get_node_by_index(idx)
                next_node = self.get_node_by_index(idx + 1)
                
                if current_node.value > next_node.value:
                    current_node.value, next_node.value = next_node.value, current_node.value
                    already_swapped = True
        
            if not already_swapped:
                return
                
                 
linked_list_to_sort = LinkedList(5)
linked_list_to_sort.push(8)
linked_list_to_sort.push(-11)
linked_list_to_sort.push(900)
linked_list_to_sort.push(25)

print('-------------sin ordenar------------')
linked_list_to_sort.print_structure()
print('----------------ordenada------------')
linked_list_to_sort.linked_list_bubble_sort()
linked_list_to_sort.print_structure()
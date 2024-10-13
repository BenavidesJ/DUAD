class BT_Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Binary_Tree:
    
    def __init__(self):
        self.root = None
        
    def insert_node(self, value):
        new_node = BT_Node(value)
        if self.root is None: # si root esta vacio inserta el nuevo nodo ahi
           self.root = new_node
           
        temp = self.root # variable para recorrer la estructura
        while True:
            if new_node.value == temp.value:
                return
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right     

    def _go_through_structure(self, current_node):
        if current_node is not None:
            self._go_through_structure(current_node.left)
            
            print(current_node.value)
            
            self._go_through_structure(current_node.right)
            
    def print_structure(self):
        if self.root is None:
            print('Null')
        else:
            self._go_through_structure(self.root)
                

                    
my_binary_tree = Binary_Tree()
my_binary_tree.insert_node(15)
my_binary_tree.insert_node(8)
my_binary_tree.insert_node(3)
my_binary_tree.insert_node(27)
my_binary_tree.insert_node(12)
my_binary_tree.insert_node(45)

my_binary_tree.print_structure()
                
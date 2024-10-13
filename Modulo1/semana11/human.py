class Torso():
    
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
    
    
    def display(self):
        print("Esta es el torso")
        self.head.display()
        self.left_arm.display()
        self.right_arm.display()
        self.right_leg.display()
        self.left_leg.display()
        
        
class Head():
    
    def display(self):
        print("Esta es la cabeza")
        
class Arm():
    
    def __init__(self, side, hand):
        self.side = side
        self.hand = hand
        
    def display(self):
        print(f"Esta es el brazo {self.side} y tengo la mano {self.side}")
        
class Hand():
        
    def display(self):
        print(f"Esta es la mano")
        
class Leg():
    
    def __init__(self, side, feet):
        self.side = side
        self.feet = feet
        
    def display(self):
        print(f"Esta es la pierna {self.side} y tengo el pie {self.side}")
        
class Feet():
        
    def display(self):
        print(f"Este es el pie")
        
class Human():
    
    def __init__(self, name, head, torso):
        self.name = name
        self.head = head
        self.torso = torso
        
        
    def display(self):
        print(f'Hola soy un humano y mi nombre es {self.name}')
        self.head.display()
        self.torso.display()

      
mano_derecha = Hand()
pie_derecho = Feet()
brazo_derecho = Arm('derecho', mano_derecha)
pierna_derecha = Leg('derecha', pie_derecho)

mano_izquierda = Hand()
pie_izquierdo = Feet()
brazo_izquierdo = Arm('izquierdo', mano_izquierda)
pierna_izquierda = Leg('izquierda', pie_izquierdo)

cabeza = Head()     
torso = Torso(cabeza, brazo_derecho, brazo_izquierdo, pierna_derecha, pierna_izquierda)
jhon_doe = Human('Jhon Doe', cabeza, torso)
jhon_doe.display()
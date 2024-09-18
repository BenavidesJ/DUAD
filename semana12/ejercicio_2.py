# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
        
    def calculate_perimeter(self):
        perimeter = pi * (self.radius * 2)
        return perimeter
    
    
    def calculate_area(self):
        area = pi * (self.radius ** 2)
        return area
    
class Square(Shape):
    
    def __init__(self, side_length):
        self.side_length = side_length
        
        
    def calculate_perimeter(self):
        perimeter = self.side_length * 4
        return perimeter
    
    
    def calculate_area(self):
        area = self.side_length * self.side_length
        return area
    
class Rectangle(Shape):
    
    def __init__(self, long_side_length, short_side_length):
        self.long_side_length = long_side_length
        self.short_side_length = short_side_length
        
        
    def calculate_perimeter(self):
        perimeter = (2 * self.long_side_length) + (2 * self.short_side_length)
        return perimeter
    
    
    def calculate_area(self):
        area = self.long_side_length * self.short_side_length
        return area
    
circle = Circle(5)
square = Square(13)
rectangle = Rectangle(6,9)

circle_perimeter = circle.calculate_perimeter()
circle_area = circle.calculate_area()
square_perimeter = square.calculate_perimeter()
square_area = square.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
rectangle_area = rectangle.calculate_area()

print(f'El area del circulo es {circle_area} y su perimetro es {circle_perimeter}')
print(f'El area del cuadrado es {square_area} y su perimetro es {square_perimeter}')
print(f'El area del rectangulo es {rectangle_area} y su perimetro es {rectangle_perimeter}')
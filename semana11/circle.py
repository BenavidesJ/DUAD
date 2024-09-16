from math import pi

class Circle():
    unit = 'm'
    def __init__(self, radius, unit):
        self.radius = radius
        self.unit = unit
    
    def get_area(self):
        area = pi * (self.radius) ** 2
        rounded_area = round(area, 2)
        return f'{rounded_area} {self.unit}^2'
    

circle_1 = Circle(3, 'cm')
circle_1_area = circle_1.get_area()

circle_2 = Circle(55, 'mm')
circle_2_area = circle_2.get_area()

print(circle_1_area)
print(circle_2_area)
    
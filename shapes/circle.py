from shapes.shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return self.color.name + ' ' + self.__class__.__name__ + ' (radius: ' + str(self.radius) + ')'

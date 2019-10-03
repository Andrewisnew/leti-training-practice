from shapes.circle import Circle
from shapes.shape import Shape
import math


class Ellipse(Circle):

    def __init__(self, radius, second_radius, color):
        super().__init__(radius, color)
        self.second_radius = second_radius

    def area(self):
        return math.pi * self.radius * self.second_radius

    def perimeter(self):
        a = max(self.radius, self.second_radius)
        b = min(self.radius, self.second_radius)
        return 4 * (math.pi * a * b + (a - b)) / (a + b)

    def __repr__(self):
        return self.color.name + ' ' + self.__class__.__name__ + ' (radius: ' + str(self.radius) + ', second radius: ' + str(self.second_radius) + ')'

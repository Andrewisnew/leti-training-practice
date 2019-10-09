from shapes.shape import Shape


class Square(Shape):

    def __init__(self, width, color):
        super().__init__(color)
        self.width = width

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return 4 * self.width

    def __repr__(self):
        return self.color.name + ' ' + self.__class__.__name__ + '(width: ' + str(self.width) + ')'

    def __hash__(self):
        hash = 7
        hash = 31*hash + self.color.value
        hash = 31*hash + self.width
        return hash

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.color == other.color and self.width == other.width

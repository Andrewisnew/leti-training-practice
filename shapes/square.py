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

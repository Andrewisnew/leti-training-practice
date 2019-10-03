from shapes.square import Square


class Rectangle(Square):

    def __init__(self, width, height, color):
        super().__init__(width, color)
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return self.color.name + ' ' + self.__class__.__name__ + '(width: ' + str(self.width) + ', height: ' + str(self.height) +')'

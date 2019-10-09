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

    def __hash__(self):
        hash = super().__hash__()
        hash = 31*hash + self.height
        return hash

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.color == other.color and self.width == other.width and self.height == other.heidht
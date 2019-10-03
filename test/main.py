from shapes.ellipse import Ellipse
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shape_list.shape_list import ShapeList
from color.color import Color


shape_list = ShapeList()

try:
    shape_list.append(1)
except TypeError:
    print('Only shape append support')

shape_list.append(Circle(5, Color.BLUE))
shape_list.append(Rectangle(2,3, Color.RED))
shape_list.append(Square(5, Color.BLUE))
shape_list.append(Ellipse(2,3, Color.GREEN))

print(shape_list)
print(shape_list.shapes_areas(Color.BLUE))

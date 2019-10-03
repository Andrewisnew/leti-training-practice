from shapes.shape import Shape


class ShapeList(list):
    def append(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError('Only shape append support')
        super().append(shape)

    def sorted_shapes_areas(self, color):
        return sorted(list(map(lambda shape: shape.area(), filter(lambda shape: shape.color == color, self))))

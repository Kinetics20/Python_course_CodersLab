class Shape:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def describe(self):
        print(f'figure in colour {self.colour} nad the center in the point {self.x, self.y}')

    def distance(self, other_shape):
        distance = ((self.x - other_shape.x) ** 2 + (self.y - other_shape.y) ** 2) ** 0.5
        return distance

    def __str__(self):
        return print(f'figure in colour {self.colour} nad the center in the point {self.x, self.y}')


shape_1 = Shape(0, 5, 'Blue')
shape_2 = Shape(3, 8, 'Red')

shape_1.describe()
shape_2.describe()

distance_between_shapes = shape_1.distance(shape_2)
print(f'distance between shapes : {distance_between_shapes}')

print(str(shape_1))
print(str(shape_2))

class Square:
    def __init__(self, side):
        self.set_side(side)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_side):
        self._side = new_side
        self._perimeter = new_side * 4
        self._area = new_side ** 2
        self._diagonal = new_side * 2 ** 0.5

    def set_perimeter(self, new_perimeter):
        self.set_side(new_perimeter / 4)

    def set_area(self, new_area):
        self.set_side(new_area ** 0.5)

    def set_diagonal(self, new_diagonal):
        self.set_side(new_diagonal / (2 ** 0.5))

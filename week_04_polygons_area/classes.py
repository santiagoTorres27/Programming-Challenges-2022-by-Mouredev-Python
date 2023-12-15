from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def __str__(self):
        return f"Square | side: {self.side}"


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return f"Triangle | base: {self.base}, height: {self.height}"


class Rectangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height

    def __str__(self):
        return f"Rectangle | base: {self.base}, height: {self.height}"

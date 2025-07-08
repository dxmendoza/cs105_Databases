from typing import Tuple, Type
import math

RectangleType = Type["Rectangle"]
CircleType = Type["Circle"]
CylinderType = Type["Cylinder"]
class Rectangle(object):
    def __init__(self: RectangleType, a: float, b: float, c: float, d: float) -> None:
        self.lower_left: Tuple[float, float] = (a, b)
        self.upper_right: Tuple[float, float] = (c, d)
        self.width: float = c - a
        self.height: float = d - b
    def max_dim(self: RectangleType) -> float:
        if self.width > self.height:
             return self.width
        else:
            return self.height
    def perim(self: RectangleType) -> float:
        return 2 * (self.width + self.height)
    def area(self: RectangleType) -> float:
        return self.width * self.height

class Circle(object):
    def __init__(self: CircleType, a: float, b:float, r: float) -> None:
        self.center: Tuple[float, float] = (a, b)
        self.radius: float = r
    def perim(self: CircleType) -> float:
        return 2 * math.pi * self.radius
    def area(self: CircleType) -> float:
        return math.pi * self.radius * self.radius

class Cylinder(object):
    def __init__(self: CylinderType, a: float, b: float, r: float, h: float) -> None:
        self.circle: Circle = Circle(a, b, r)
        self.height: float = h
    def perim(self: CylinderType) -> float:
        return (4 * self.circle.radius) + (2 * self.height)
    def area(self: CylinderType) -> float:
        r1: float = self.circle.radius
        return (2 * math.pi * r1 * self.height) + (2 * math.pi * r1 * r1)


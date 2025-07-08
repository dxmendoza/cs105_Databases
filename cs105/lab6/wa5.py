from operator import truediv
from typing import List, Tuple, Type
import math

RectangleType = Type["Rectangle"]
CylinderType = Type["Cylinder"]
def list_length(s: List) -> int:
    idk: int = 0
    while idk < len(s):
        idk += 1
    return idk
def list_length2(s: List) -> int:
    idk: int = 0
    for val in s:
        idk+= 1
    return idk
def list_length3(s: List) -> int:
    if s == []:
        return 0
    x: int = s.pop()
    return list_length3(s) + 1

def mean(s: List) -> int:
    if s == []:
        return 0
    x: int = s.pop()
    return mean(s) + x

def mean3(s: List) -> int:
    idk: int = 0
    sum_mean: int = 0
    while idk < len(s):
        sum_mean = sum_mean + s[idk]
        idk += 1
    return sum_mean/idk

def mean2(s: List) -> int:
    idk: int = 0
    sum_mean: int = 0
    for val in s:
        sum_mean = sum_mean + val
        idk += 1
    return sum_mean/idk




x: List[int] = [1, 3, 6, 2, 9]
print(list_length(x))
print(list_length2(x))
print(mean(x))
print(mean(x))
print(mean2(x))


#def list_length2(s: List) -> int:

class Cylinder(object):
    def __init__(self: CylinderType, a: float, b: float, r: float, h: float) -> None:
        self.radius: float = r
        self.height: float = h
    def volume(self: CylinderType) -> float:
        return math.pi * self.radius * self.radius * self.height

class Rectangle(object):
    def __init__(self: RectangleType, a: float, b: float, c: float, d: float) -> None:
        self.lower_left: Tuple[float, float] = (a, b)
        self.upper_right: Tuple[float, float] = (c, d)
        self.width: float = c - a
        self.height: float = d - b

    def area(self: RectangleType) -> float:
        return self.width * self.height
    def contains(self: RectangleType, x: int, y: int) -> bool:
        coor: Tuple[float, float] = (x, y)
        if self.lower_left[0] <= coor[0] <= self.upper_right[0]:
            if self.lower_left[1] <= coor[1] <= self.upper_right[1]:
                return True
        else:
            return False

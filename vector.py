import math

class Vector3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if type(other) == Vector3: return self.x*other.x + self.y*other.y + self.z*other.z
        else: return Vector3(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other):
        if type(other) == Vector3: raise Exception
        else: return Vector3(self.x/other, self.y/other, self.z/other)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def cross(self, other):
        return Vector3(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

def vector3_distance(vec1: Vector3, vec2: Vector3):
    return abs(vec1-vec2)
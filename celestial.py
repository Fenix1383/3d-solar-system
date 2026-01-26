from config import *
from vector import Vector3, vector3_distance

class Celestial:
    def __init__(self, mass: int, radius: int, position: Vector3, velocity: Vector3, color: list[int], name="None"):
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.color = color
        self.name = name

def celestial2_scalar_force(cel1: Celestial, cel2: Celestial) -> float:
    dist = vector3_distance(cel1.position, cel2.position)
    return ((GRAVITATION_CONSTANT*cel1.mass*cel2.mass)
            /
            (dist*dist + SOFTENING_SQ))

def celestial2_vector_force(cel1: Celestial, cel2: Celestial) -> Vector3:
    dist = vector3_distance(cel1.position, cel2.position)
    scalar = celestial2_scalar_force(cel1, cel2)
    vector = cel2.position - cel1.position
    return (vector/abs(vector))*scalar

def result_force(cel: Celestial, all_cels: list[Celestial]) -> Vector3:
    result = Vector3(0, 0, 0)
    for i in all_cels:
        if i is not cel:
            result += celestial2_vector_force(cel, i)
    return result

from celestial import Celestial, result_force
from render import Renderer
from vector import Vector3
import math
import time
import random

count = 50

sun = Celestial(1e30, 6e8, Vector3(0, 0, 0), Vector3(0, 0, 0))
earth = Celestial(6e24, 6e3, Vector3(1.5e11, 12345, 34632), Vector3(0, 0, 0))
jupiter = Celestial(1.9e27, 6e4, Vector3(5.88e11, 0, 0), Vector3(0, 0, 0))
moon = Celestial(7.5e22, 1e3, Vector3(1.5e11 + 4e8, 12345, 34632), Vector3(0, 0, 0))
moon2 = Celestial(7.5e22, 1e3, Vector3(5.88e11 + 4e8, 12345, 34632), Vector3(0, 0, 0))
additions = [Celestial(random.randint(1, 1000)*1e23, 1e3, Vector3(random.randint(-1000, 1000)*1e8, 0, 0), Vector3(0,0,0))
             for _ in range(count-5)]

all_cels = [sun, earth, jupiter, moon, moon2, *additions]
current_cel = sun
sec = time.time()
for _ in range(int(1e4)):
    res = str(result_force(current_cel, all_cels)/current_cel.mass)
print(time.time()-sec)
print(len(all_cels))
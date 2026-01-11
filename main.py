import math
import pygame
from config import *
from celestial import Celestial
from vector import Vector3
from render import Renderer

pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sun = Celestial(1e30, 7e8, Vector3(0, 0, 0), Vector3(0, 0, 0), ORANGE, "sun")
earth = Celestial(6e24, 6e6, Vector3(1.5e11, 0, 0), Vector3(0, 0, 0), SKYBLUE, "earth")
jupiter = Celestial(1.9e27, 6e7, Vector3(5.88e11, 0, 0), Vector3(0, 0, 0), YELLOW, "jupiter")
moon = Celestial(7.5e22, 2e5, Vector3(1.5e11 + 4e8, 12345, 34632), Vector3(0, 0, 0), GRAY)
moon2 = Celestial(7.5e22, 2e5, Vector3(5.88e11 + 4e8, 12345, 34632), Vector3(0, 0, 0), RED)
all_cels = [sun, earth, jupiter, moon, moon2]

renderer = Renderer(scr, clock, all_cels)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    scr.fill(BLACK)

    renderer.render_cels(all_cels)
    renderer.render_fps()
    renderer.movement()
    # renderer.camera_pos.y -= 1e7
    # renderer.camera_rotation[0] += 1e-5
    # renderer.camera_rotation[1] -= 1e-5

    pygame.display.flip()
    clock.tick()
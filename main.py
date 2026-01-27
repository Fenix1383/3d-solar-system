import math
import pygame
from config import *
from celestial import Celestial
from vector import Vector3
from render import Renderer
from physics import update_physics
from writer import input_text


def create_solar_system():
    # Данные: (Масса, Радиус, Дистанция, Цвет, Имя)
    planets_data = [
        (3.302e23, 2.440e6, 5.79e10, (169, 169, 169), "Mercury"),
        (4.869e24, 6.052e6, 1.082e11, (255, 198, 73), "Venus"),
        (5.972e24, 6.371e6, 1.496e11, (100, 149, 237), "Earth"),
        (6.417e23, 3.390e6, 2.279e11, (188, 39, 50), "Mars"),
        (1.898e27, 6.991e7, 7.786e11, (233, 193, 110), "Jupiter"),
        (5.683e26, 5.823e7, 1.434e12, (244, 230, 157), "Saturn"),
        (8.681e25, 2.536e7, 2.871e12, (127, 255, 212), "Uranus"),
        (1.024e26, 2.462e7, 4.495e12, (65, 105, 225), "Neptune"),
    ]

    sun_mass = 1.9885e30
    sun = Celestial(
        mass=sun_mass, 
        radius=6.957e8, 
        position=Vector3(0, 0, 0), 
        velocity=Vector3(0, 0, 0), 
        color=(255, 255, 0), 
        name="Sun"
    )

    cels = [sun]

    for data in planets_data:
        mass, radius, distance, color, name = data
        
        # 1. Позиция: смещаем по оси X
        pos = Vector3(distance, 0, 0)
        
        # 2. Расчет скорости для круговой орбиты: v = sqrt(G * M_sun / R)
        # Важно: учитываем только массу Солнца, так как масса планет пренебрежимо мала
        velocity_scalar = math.sqrt(g.gravitation_constant * sun_mass / distance)
        
        # 3. Направление скорости: перпендикулярно радиус-вектору (по оси Z)
        vel = Vector3(0, 0, velocity_scalar)

        cels.append(Celestial(mass, radius, pos, vel, color, name))

    return cels


pygame.init()
scr = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sun = Celestial(2e30, 7e8, Vector3(0, 0, 0), Vector3(0, 0, 0), ORANGE, "sun")
earth = Celestial(6e24, 6e6, Vector3(1.5e11, 0, 0), Vector3(0, 0, 0), SKYBLUE, "earth")
# jupiter = Celestial(1.9e27, 6e7, Vector3(5.88e11, 0, 0), Vector3(0, 0, 0), YELLOW, "jupiter")
# moon = Celestial(7.5e22, 2e5, Vector3(1.5e11 + 4e8, 12345, 34632), Vector3(0, 0, 0), GRAY)
# moon2 = Celestial(7.5e22, 2e5, Vector3(5.88e11 + 4e8, 12345, 34632), Vector3(0, 0, 0), RED)
# all_cels = [sun, earth, jupiter, moon, moon2]

# all_cels = [sun, earth]

all_cels = create_solar_system()

writing = [False, 'g']
renderer = Renderer(scr, clock, all_cels)

unfixed_dt = True
while True: 
    if unfixed_dt: dt_for_physics = (clock.get_time() / 1000.0) * TIME_SCALE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and not writing[0]:
            if event.key == pygame.K_g:
                writing = [True, 'g']
                print("enter G")
            elif event.key == pygame.K_t:
                writing = [True, 'dt']
                print("enter dt")

        elif writing[0]:
            code = input_text(event)
            if code:
                try:
                    if writing[1] == 'g':
                        g.gravitation_constant = float(code)*(10**-11)
                        if not float(code):
                            g.gravitation_constant = DEFAULT_G
                        print("NEW G =", g.gravitation_constant)
                    if writing[1] == 'dt':
                        dt_for_physics = int(code)
                        unfixed_dt = False
                        if not int(code):
                            unfixed_dt = True
                        print("NEW dt =", dt_for_physics)
                    
                except: pass
                writing[0] = False

    scr.fill(BLACK)

    renderer.render_cels(all_cels)
    renderer.render_fps()
    renderer.movement()
    update_physics(all_cels, dt_for_physics)

    # renderer.camera_pos.y -= 1e7
    # renderer.camera_rotation[0] += 1e-5
    # renderer.camera_rotation[1] -= 1e-5

    pygame.display.flip()
    clock.tick(FPS)
import pygame
import math
from vector import Vector3
from config import *
from celestial import Celestial
import typing

class Renderer:
    def __init__(self, scr: pygame.Surface, clock: pygame.time.Clock, cels: list[Celestial], camera_pos: typing.Optional[Vector3] = None):
        if camera_pos: self.camera_pos = camera_pos
        else: self.camera_pos = self.auto_camera_pos(cels)
        self.camera_rotation = [0, math.pi]
        self.scr = scr
        self.clock = clock
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def auto_camera_pos(self, cels: list[Celestial], koef = 50) -> Vector3:
        # for cel1 in cels:
        #     for cel2 in cels:
        real_height = max([max([abs(cel1.position-cel2.position) for cel2 in cels]) for cel1 in cels])
        real_width = real_height * RESOLUTION
        real_distance = real_width * SCR_DISTANCE / WIDTH
        return Vector3(0, real_distance + real_distance * koef/100, 0)
        
    def rotation_to_vector(self, rot: list[float]):
        return Vector3(math.sin(rot[0])*math.sin(rot[1]), math.cos(rot[1]), math.cos(rot[0])*math.sin(rot[1]))

    def vector_to_rotation(self, vec: Vector3):
        length = abs(vec)
        if length == 0: return [0, 0]
        # Угол theta (зенитный)
        theta = math.acos(vec.y / length)
        # Угол phi (азимутальный)
        phi = math.atan2(vec.x, vec.z)
        return [phi, theta]

    def world_to_camera_space(self, vec: Vector3, default_vectors = []):
        # Векторы системы координат камеры
        if not default_vectors:
            forward = self.rotation_to_vector(self.camera_rotation)
            up = self.rotation_to_vector([self.camera_rotation[0], self.camera_rotation[1]-math.pi/2])
            right = forward.cross(up)
        else:
            forward, up, right = default_vectors
        # Проекция world_vec на оси камеры
        x = right*vec
        y = up*vec
        z = forward*vec
        # print(forward, up, right)
        return Vector3(x, y, z)

    def render_cels(self, cels: list[Celestial]):
        draws = []
        default_vectors = [self.rotation_to_vector(self.camera_rotation),
        self.rotation_to_vector([self.camera_rotation[0], self.camera_rotation[1]-math.pi/2])]
        default_vectors.append(default_vectors[0].cross(default_vectors[1]))
        for cel in cels:
            vec = cel.position - self.camera_pos # От камеры до центра тел
            vec = self.world_to_camera_space(vec, default_vectors) # Перевод в локальную систему координат
            rot_vec = self.vector_to_rotation(vec) # Перевод в rotation
            rot_vec = rot_vec[0], rot_vec[1] - math.pi/2
            # rot_vec = [rot_vec[0] - self.camera_rotation[0], rot_vec[1] - self.camera_rotation[1]] # Относительная rotation
            if (rot_vec[0] >= -HALF_FOV and rot_vec[0] <= HALF_FOV) and \
                (rot_vec[1] >= -HALF_FOV/RESOLUTION and rot_vec[1] <= HALF_FOV/RESOLUTION): # Попадает ли в экран
                scr_radius = cel.radius * SCR_DISTANCE // abs(vec)
                scr_position = [HALF_WIDTH + rot_vec[0] * WIDTH // (HALF_FOV * 2), 
                                HALF_HEIGHT - WIDTH * rot_vec[1] // (HALF_FOV * 2)]
                # scr_position = [HALF_WIDTH + (vec.x / vec.z) * SCR_DISTANCE, 
                #                 HALF_HEIGHT - (vec.y / vec.z) * SCR_DISTANCE]
                if scr_radius <= 0: scr_radius = 1

                draws.append([cel, scr_position, scr_radius, abs(vec)])
        draws.sort(key=lambda x: x[3], reverse=True)

        for cel, scr_position, scr_radius, abs_vec in draws:
            pygame.draw.circle(self.scr, cel.color, scr_position, scr_radius)
            # print(cel.color)
            # if cel.radius == 6e3: 
            #     print(rot_vec)
            #     print([HALF_FOV, HALF_FOV/RESOLUTION])
        # print('----')
                
    def render_fps(self):
        display_fps = str(int(self.clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.scr.blit(render, FPS_POS)
    
    def movement(self):
        keys = pygame.key.get_pressed()
        fps = self.clock.get_fps()
        if keys[pygame.K_LEFT]:
            self.camera_rotation[0] -= ROTATE_SPEED * FPS / fps
        elif keys[pygame.K_RIGHT]:
            self.camera_rotation[0] += ROTATE_SPEED * FPS / fps
        if keys[pygame.K_UP]:
            self.camera_rotation[1] += ROTATE_SPEED * FPS / fps
        elif keys[pygame.K_DOWN]:
            self.camera_rotation[1] -= ROTATE_SPEED * FPS / fps
        if keys[pygame.K_w]:
            self.camera_pos += self.rotation_to_vector(self.camera_rotation)*MOVEMENT_SPEED * FPS / fps
        elif keys[pygame.K_s]:
            self.camera_pos -= self.rotation_to_vector(self.camera_rotation)*MOVEMENT_SPEED * FPS / fps
        # print(self.camera_rotation)
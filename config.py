import math

# Pygame config

WIDTH, HEIGHT = 1200, 800
FPS = 60
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
RESOLUTION = WIDTH / HEIGHT
FPS_POS = (WIDTH-65, 5)

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
RED = (220, 0 ,0)
GREEN = (0, 220, 0)
GRASSGREEN = (44, 95, 52)
BLUE = (0, 0, 220)
SKYBLUE = (135, 206, 235)
GRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
YELLOW = (220, 220, 0)
ORANGE = (255, 165, 0)

# Physics config

GRAVITATION_CONSTANT = 6.67430e-11
SUN_MASS = 1.98892e30

TIME_SCALE = FPS * 1440  # Один шаг симуляции равен 1 суткам (в секундах)

# Camera config

MOVEMENT_SPEED = 1e8
ROTATE_SPEED = 5e-3
FOV = math.pi/2
HALF_FOV = FOV / 2
SCR_DISTANCE = WIDTH // (math.tan(HALF_FOV) * 2)

# INITED Physics

SOFTENING = 1e5
SOFTENING_SQ = SOFTENING**2  # Предварительный расчет
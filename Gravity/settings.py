import random
WIDTH = 700
HEIGHT = 450
FPS = 30
TITLE = "Test"

# Player properties
PLAYER_ACC = 2
PLAYER_FRICTION = -0.2
PLAYER_GRAV = 1

# Platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (random.randint(1, WIDTH - 100), random.randint(1, HEIGHT), 200, 40)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#gravity simulation displaying two objects and the force acting between them:
#importing necessary modules:

import pygame
import math
import matplotlib.pylplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#screen dimensions:
WIDTH, HEIGHT = 1200, 870
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

#initializing pygame:
pygame.init()
pygame.font.init()

#colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (135, 206, 250)
YELLOW = (255, 255, 0)

#gravitational constant:
G = 13

#storage cap on position and velocity values:
MAX_PATH_LENGTH = 500
MAX_V_LENGTH = 500

#this class represents each object in the simulation
#includes properties for position, velocity, mass, radius, color and path:
class Body:
    def __init__(self, x, y, mass, radius, color):
        self.pos = [x, y]
        self.vel = [0, 0]
        self.mass = mass
        self.radius = radius
        self.color = color
        self.path = []
















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


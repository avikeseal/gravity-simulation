#gravity simulation displaying two objects and the force acting between them:
#importing necessary modules:

import pygame
import math
import matplotlib.pyplot as plt
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

    #apply gravity method calculates gravity:
    def apply_gravity(self, other):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        distance = math.sqrt( (dx**2) + (dy**2) )

        if distance > 0:
            force = (G * self.mass * other.mass)/(distance**2)
            angle = math.atan2(dy, dx)
            force_x = force * math.cos(angle)
            force_y = force * math.sin(angle)

            self.vel[0] += force_x / self.mass
            self.vel[1] += force_y / self.mass

    #update_position method updates the position based on velocity:
    def update_position(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.path.append((int(self.pos[0]), int(self.pos[1])))

        #remove old path data to free up memory:
        if len(self.path) > MAX_PATH_LENGTH:
            self.path.pop(0)


    #draw method handles drawing the object:
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
        if len(self.path) > 1:
            pygame.draw.lines(screen, YELLOW, False, self.path, 2)

#this function creates a graph that displays velocities over time:
def create_graph(velocities, figsize=(5, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(velocities, label='Velocity')
    ax.axhline(y=np.min(velocities), color='r', linestyle='--', label='Min Velocity')
    ax.axhline(y=np.max(velocities), color='g', linestyle='--', label='Max Velocity')
    ax.legend()

    #draws the plot:
    canvas = FigureCanvas(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()

    #close the figure to free up memory:
    plt.close(fig)
    return raw_data, size

#the main function initializes the pygame screen, 
#creates the objects and runs the main loop:
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Gravity Simulation')
    clock = pygame.time.Clock()

    #initializing fonts:
    font_path = 'Cyberspace Raceway Front.otf'
    font = pygame.font.Font(font_path, 45)
    font_color = YELLOW

    #initializing bodies:
    central_body =  Body(WIDTH//2 + 250, (HEIGHT//2 - 100), 1000, 60, RED)
    moving_body = Body((WIDTH//2 + 500), (HEIGHT//2 - 100), 1, 15, BLUE)
    #initial velocity:
    moving_body.vel = [-3.5, -6]

    bodies = [central_body, moving_body]
    velocities = []

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #calculates gravity and updates position:
        for body in bodies:
            if body != central_body:
                body.apply_gravity(central_body)
            if body != moving_body:
                body.apply_gravity(moving_body)
            body.update_position()

        #calculate and store velocity for the moving body:
        velocity = math.sqrt((moving_body.vel[0]**2) + (moving_body.vel[1]**2))
        velocities.append(velocity)
        #removing old velocity data to free up memory:
        if len(velocities) > MAX_V_LENGTH:
            velocities.pop(0)
        
        #creating the graph:
        raw_data, size = create_graph(velocities)
        graph_surface = pygame.image.fromstring(raw_data, size, 'RGB')

        #drawing everything:
        screen.fill(BLACK)

        #render the heading:
        heading = font.render('Welcome to Gravity Simulation', True, YELLOW)
        screen.blit(heading, (WIDTH//2 - heading.get_width()//2, 10))

        for body in bodies:
            body.draw(screen)

        
        #displaying the graph:
        #adjusted position:
        screen.blit(graph_surface, (40, 80))

        #cap the frame rate to 60 fps:
        clock.tick(60)

        #update the display:
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

        















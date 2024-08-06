#importing tkinter:
import tkinter as tk
import math
import random
from tkinter import ttk
from PIL import Image, ImageTk




root = tk.Tk()
root.title('Gravity Simulation')

#setting the window size (width x height):
#root.geometry('400x300')

#setting a fixed window size:
fixed_width =   600
fixed_height = 415
root.geometry(f'{fixed_width}x{fixed_height}') 

#restricting the window from being resized:
root.resizable(False, False)

#constants--------------

#gravitational constant
G = 1
#number of celestial objects:
PLANET_COUNT = random.randint(2,5)
print(f"Creating {PLANET_COUNT} planets")
PLANET_SIZE = 30 

#---tkinter testing--------------------------------------------------------
#Adding a label:
#button = tk.Button(root, text='Click Me!', command=lambda: print('Button Clicked'))
#button.pack(pady=10)

#Adding a text entry box:
#entry = tk.Entry(root)
#entry.pack(pady=10)

#Adding another label:
#label = tk.Label(root, text='Hello Tkinter world')
#label.pack(pady=10)
#--------------------------------------------------------------------------

#loading the bg image:
bg_image  = Image.open(r"C:\Users\PC\Desktop\projects\gravity-simulation\images\istockphoto-498478219-612x612.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

#creating canvas:
canvas = tk.Canvas(root, width=800, height=580)
canvas.pack(fill='both', expand=True)

#setting the background image on canvas:
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

#creating a planet class to manage each planet's properties and methods:
class Planet:
    def __init__(self, canvas, x, y, size, mass):

        #assigns provided values to instance attributes:
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x + size, y + size, fill='blue')
        self.size = size
        self.mass = mass
        self.x = x

        #horizontal velocity:
        self.vx = random.uniform(-10, 10)
        #vertical velocity: 
        self.y = y
        self.vy = random.uniform(-10, 10)
    
    #this function will update the planet's position
    #(self.x and self.y) based on  its current velocity.
    #Handles boundary collision so the planet bounces back 
    #when it hit the edges of the window.
    #updates the position of the planet on the canvas to reflect the new coordinates.
    def move(self):
        #by adding the velocity components it updates the planet position:
        self.x += self.vx
        self.y += self.vy 

        #checks if the planet has collided with the right or left edge of the canvas:
        if self.x + self.size > self.canvas.winfo_width() or self.x < 0:
            #if true the velocity is reversed and the planet bounces back into the window:
            self.vx =- self.vx
        #checks if the planet has collided with the top or bottom edge of the canvas:
        if self.y + self.size > self.canvas.winfo_height() or self.y < 0:
            self.vy =- self.vy

        #updates the postion on the canvas to reflect new coordinates:
        #'coords' method of the canvas widget changes the
        #coordinates of the canvas object - self.id to the new position:
        #self.x and self.y
        self.canvas.coords(self.id, self.x, self.y, (self.x + self.size), (self.y +  self.size) )

    #calculating and applying gravitational force between planets:
    def apply_gravity(self, other):
        #evaluating distance components:
        #using the differences in x and y coordinatesv of the two planets
        #are also used to calculate the angle of the force vector
        dx = other.x - self.x
        dy = other.y - self.y

        #calculating distance using the Pythagorean theorem
        #this is the Euclidean distance in 2D space
        distance = math.sqrt( dx ** 2 + dy ** 2 )
        #to ensure that planets do not overlap for being too close 
        #to each other (closer than the radius of the planet)
        #in that case the force will not be applied:
        if distance < self.size:
            return
        #calculating gravitational force using Newton's law of univeral gravitation:
        force = G * ( self.mass * other.mass ) / (distance ** 2)
        
        #calculating the angle of the force:
        #the angle of the force vector is calculated using the
        #atan2 function which returns the arctan of dy/dx
        #this angle represents the direction of the gravitational force from self to other
        angle = math.atan2(dy, dx)
        #updating velocities based on force:
        #x and y components are calculated using cos(angle) amd sin(angle):
        #dividing the components by the mass (self.mass) to get acceleration:
        #acceleration components are then added to current velocities
        #(self.vx and self.vy)to update them based on the gravitational force
        self.vx += (force * math.cos(angle) ) / (self.mass)
        self.vy += (force * math.sin(angle) ) / (self.mass)

#creating and initializing planets:
#a list to hold planets:
planets =  []
#loop to create planets:
#this will run 6 times and generate a sequene of numbers from 0 to 4:
#underscore is used as a variable name since we do not need the loop variable:
for _ in range(PLANET_COUNT):
    #generating random position and mass:
    #random intial x position:
    x = random.randint(300, 780)
    #random intial y position:
    y = random.randint(100, 580)
    #random mass within a specified range:
    mass = random.uniform(1, 10)
    #new planet instance:
    #a new 'Planet' object with specified canvas, position, size (50) and mass
    planet = Planet(canvas, x, y, PLANET_SIZE, mass)
    planets.append(planet)

#defining the animation loop:
def animate():
    
    #iterates over each planet in the 'planets' list
    #enumerate function provides both the index (i) and the planet object ('planet')
    for  i, planet in enumerate(planets):
        
        #calculate gravitational forces:
        #the inner loop iterates over all planets again
        #for each pair of 'planet' and 'other' it checks if they are not the same planet (i != j):
        for j, other in enumerate(planets):
            if i != j:
                planet.apply_gravity(other)
        
        #updating planet position:
        #after applying the G fores from all other planets, the 'move'
        #method is called for the current 'planet' to update its position based on velocity
        planet.move()

    #repeating the animation:
    #'root.after' function call schedules the 'animate' fcunction
    #to be called again after 20 ms:
    root.after(20, animate)
    print("Animation Step")






#starting the event loop to display the window and respond to user interactions:
animate()
root.mainloop()
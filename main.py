#importing tkinter:
import tkinter as tk
import math
import random
from tkinter import ttk
from PIL import Image, ImageTk




root = tk.Tk()
root.title('Gravity Simulation App')

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
G = 6.67430e-11
#number of celestial objects:
PLANET_COUNT = 3
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
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill='both', expand=True)

#setting the background image on canvas:
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

#creating a planet class to manage each planet's properties and methods:
class Planet:
    def __init__(self, canvas, x, y, size, mass):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x + size, y + size, fill='blue')
        self.size = size
        self.mass = mass
        self.x = x

        #horizontal velocity:
        self.vx = random.uniform(-2, 2)
        #vertical velocity: 
        self.y = y
        self.vy = random.uniform(-2, 2)
    
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
            self.vx = -self.vx
        #checks if the planet has collided with the top or bottom edge of the canvas:
        if self.y + self.size > self.canvas.winfo_height() or self.y < 0:
            self.vy = -self.vy

        #updates the postion on the canvas to reflect new coordinates:
        #'coords' method of the canvas widget changes the
        #coordinates of the canvas object - self.id to the new position:
        #self.x and self.y
        self.canvas.coords(self.id, self.x, self.y)






#starting the event loop to display the window and respond to user interactions:
root.mainloop()
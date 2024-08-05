#importing tkinter:
import tkinter as tk
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



#starting the event loop to display the window and respond to user interactions:
root.mainloop()
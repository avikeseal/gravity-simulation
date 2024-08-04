#importing tkinter:
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Gravity Simulation App')

#setting the window size (width x height):
root.geometry('400x300')

#Adding a label:
button = tk.Button(root, text='Click Me!', command=lambda: print('Button Clicked'))
button.pack(pady=10)

#Adding a text entry box:
entry = tk.Entry(root)
entry.pack(pady=10)

#Adding another label:
label = tk.Label(root, text='Hello Tkinter world')
label.pack(pady=10)

#starting the event loop to display the window and respond to user interactions:
root.mainloop()
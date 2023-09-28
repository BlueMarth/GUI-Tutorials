import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Place')
window.geometry('400x600')

label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
button = ttk.Button(window, text = 'Button')

label1.place(x = 300, y = 100, width = 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5) # much easier to use
x3 = 400*0.2
y3 = 600*0.1
wid3 = 400*0.4
hei3 = 600*0.5
label3.place(x = x3, y = y3, width = wid3, height = hei3)
# anchor: choose the positioning point on the widget
button.place(relx = 1, rely = 1, anchor = 'se')


window.mainloop()
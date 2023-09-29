# 3 scrollable widgets: canvas, text, treeview
# canvas is the most useful since it can display widgets

import tkinter as tk
from tkinter import ttk
from random import randint, choice

window = tk.Tk()
window.title('Scrolling')
window.geometry('600x400')

# canvas
canvas = tk.Canvas(window, bg = 'grey', scrollregion = (0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 5000, fill = 'cyan', width = 10)
for i in range(100):
    left = randint(0, 2000)
    top = randint(0, 5000)
    right = left + randint(10, 500)
    bottom = top + randint(10, 500)
    colour = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(left, top, right, bottom, fill = colour)
canvas.pack(expand = True, fill = 'both')

# vertical mousewheel scrolling
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta/60), "units")) # delta always 120 or -120
# vertical mousewheel scrolling
canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta/60), "units"))

# vertical scrollbar
scrollbar_vert = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
canvas.configure(yscrollcommand = scrollbar_vert.set) # make the scroll handle to scale
scrollbar_vert.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# horizontal scrollbar
scrollbar_horz = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
canvas.configure(xscrollcommand = scrollbar_horz.set) # make the scroll handle to scale
scrollbar_horz.place(relx = 0, rely = 1, relwidth = 1, anchor = 'sw')

window.mainloop()
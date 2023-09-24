import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400') 
# when window size is not specified, it conforms to the widgets
window.title('Frames & Parenting')

# frame
frame = ttk.Frame(window, width = 200, height = 200,
                  borderwidth = 10, relief = tk.GROOVE) # FLAT, RAISED, SUNKEN, RIDGE
frame.pack_propagate(False)
## otherwise ttk tries to set the size of a widget by its CHILDREN
frame.pack(side = 'left')

# master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'label outside frame')
label2.pack(side = 'left')

## exercise
ex_frame = ttk.Frame(window)
ttk.Label(ex_frame, text = 'exercise label').pack()
ttk.Button(ex_frame, text = 'exercise button').pack()
ttk.Entry(ex_frame).pack()
ex_frame.pack(side = 'left')

# run
window.mainloop()
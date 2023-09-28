### ways to create custom components
# 1. Classes - inherit from a widget and add custom parts
#   :) can create complex layouts                               :( end up creating lots of classes
# 2. Functional - create a widget in a function and return it
#   :) easier to organise when creating smaller components      :( more limited for the layouts


import tkinter as tk
from tkinter import ttk

# option 2
def create_segment(parent, label_text, button_text):
    frame = ttk.Frame()
    
    # grid layout
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')

    # widgets
    ttk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

    return frame
    
# option 1
class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(parent)

        # grid layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        ttk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')
        

        self.pack(expand = True, fill = 'both', padx = 10, pady = 10)


# window
window = tk.Tk()
window.title('Combined layout')
window.geometry('400x600')

# widgets
create_segment(window, 'label', 'button').pack(expand = True, fill = 'both', padx = 10, pady = 10)
create_segment(window, '1', 'a').pack(expand = True, fill = 'both', padx = 10, pady = 10)
create_segment(window, '2', 'b').pack(expand = True, fill = 'both', padx = 10, pady = 10)
create_segment(window, '3', 'c').pack(expand = True, fill = 'both', padx = 10, pady = 10)
create_segment(window, '4', 'd').pack(expand = True, fill = 'both', padx = 10, pady = 10)

# Segment(window, '1', 'a')
# Segment(window, '2', 'b')
# Segment(window, '3', 'c')
# Segment(window, '4', 'd')

# run
window.mainloop()
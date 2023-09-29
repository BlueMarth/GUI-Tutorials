# thresholds    width   height
# small:        300     150
# medium:       600     300
# large:        1200    600
# whenever the window resizes we check the width and build a new layout if it crosses a threshold
# use event binding

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, start_size):
        super().__init__()
        self.title(title)
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        # size dictionary relates size of window to layout change
        SizeNotifier(
            self,
            {
                300: self.create_small_layout,
                600: self.create_medium_layout,
                1200: self.create_large_layout
            })

        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text = 'Label 1', background = 'red').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 2', background = 'green').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 5)
        self.frame.pack(expand = True, fill = 'both')
        
    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.rowconfigure((0,1), weight = 1, uniform = 'a')
        self.frame.columnconfigureconfigure((0,1), weight = 1, uniform = 'a')
        self.frame.pack(expand = True, fill = 'both')

        ttk.Label(self.frame, text = 'Label 1', background = 'red').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 2', background = 'green').grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        
    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.rowconfigure(0, weight = 1, uniform = 'a')
        self.frame.columnconfigureconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.frame.pack(expand = True, fill = 'both')

        ttk.Label(self.frame, text = 'Label 1', background = 'red').grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 2', background = 'green').grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 3', background = 'blue').grid(row = 0, column = 2, sticky = 'nsew', padx = 10, pady = 10)
        ttk.Label(self.frame, text = 'Label 4', background = 'yellow').grid(row = 0, column = 3, sticky = 'nsew', padx = 10, pady = 10)

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items())} # dictionary
        self.current_min_size = None
        self.window.bind('<Configure>', self.check_size)
        
        self.window.update()

        min_height = self.window.winfo_screenheight()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width,min_height)
        # self.window.bind('<Configure>', self.check_size)
            
    def check_size(self, event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                delta = window_width - min_size
                if delta >= 0:
                    checked_size = min_size
            
            if checked_size != self.current_min_size: # check if theres a change in size threshold
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]() # set min size same as small layout size to avoid error

# run
app = App('Responsive Layout', (400,300))
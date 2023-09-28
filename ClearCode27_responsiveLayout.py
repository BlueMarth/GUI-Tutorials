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
            {300: self.create_small_layout,
            600: self.create_medium_layout,
            1200: self.create_large_layout
            })

        self.mainloop()

    def create_small_layout(self):
        print('small')
    def create_medium_layout(self):
        print('medium')
    def create_large_layout(self):
        print('large')

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        # dictionary
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None
        # self.window.bind('<Configure>', self.check_size)
        self.window.bind('<Configure>', self.check_size)
    
    def check_size(self, event):
        window_width = event.width
        checked_size = None

        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size
        
        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()



# widgets

# run
app = App('Responsive Layout', (400,300))
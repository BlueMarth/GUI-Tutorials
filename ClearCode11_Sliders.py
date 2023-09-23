import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('Sliders')

# slider
scale_float = tk.DoubleVar(value = 15)
scale = ttk.Scale(window,
                  command = lambda value: progress.stop,
                  from_ = 0, to = 25,
                  length = 300,
                  orient = 'horizontal',
                  variable = scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(window, variable = scale_float,
                           maximum = 25,
                           orient = 'horizontal',
                           mode = 'indeterminate',
                           length = 400)
progress.pack()

# progress.start(100)

# Scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

## exercise
ex_int = tk.IntVar()
ex_progress = ttk.Progressbar(window, variable = ex_int,
                              orient = 'vertical',)
ex_progress.pack()
ex_progress.start()

label = ttk.Label(window, textvariable = ex_int)
label.pack()

ex_scale = ttk.Scale(window, variable = ex_int, from_ = 0, to = 200)
ex_scale.pack()

# run
window.mainloop()
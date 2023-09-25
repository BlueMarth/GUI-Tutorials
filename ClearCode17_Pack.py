import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

## widgets
# label1 = ttk.Label(window, text = 'Label 1', background = 'red')
# label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
# label3 = ttk.Label(window, text = 'Label 3', background = 'green')
# button = ttk.Button(window, text = 'Button')

# label1.pack(side = 'top', expand = True, fill = 'both')
# label2.pack(side = 'top', fill = 'x')
# label3.pack(side = 'top')
# button.pack(side = 'top', expand = True, fill = 'both')

## exercise
ex_label1 = ttk.Label(window, text = 'Ex label 1', background = 'red')
ex_label2 = ttk.Label(window, text = 'Ex label 2', background = 'blue')
ex_label3 = ttk.Label(window, text = 'Ex label 3', background = 'green')
ex_button = ttk.Button(window, text = 'Ex Button')
# pad -> create empty space     ipad -> expand widget size
ex_label1.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)
ex_label2.pack(side = 'left', expand = True, fill = 'both')
ex_label3.pack(side = 'top', expand = True, fill = 'both')
ex_button.pack(side = 'top', expand = True, fill = 'both')

# run
window.mainloop()
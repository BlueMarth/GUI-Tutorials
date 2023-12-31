import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# combobox
items = ('Item A', 'Item B', 'Item C')
item_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = item_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

# events
combo.bind('<<ComboboxSeleted>>', lambda event: combo_label.config(text = f'Selected value: {item_string.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, from_ = 3, to = 20, increment = 3,
                   command = lambda: print(spin_int.get()),
                   textvariable = spin_int) # goes as high as it can get
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5)
spin.pack()

## exericse
ex_chars = ('A', 'B', 'C', 'D', 'E')
ex_string = tk.StringVar(value = ex_chars[0])
ex_spin = ttk.Spinbox(window, textvariable = ex_string, values = ex_chars)
ex_spin.pack()

ex_spin.bind('<<Decrement>>', lambda event: print(ex_string.get()))

# run
window.mainloop()
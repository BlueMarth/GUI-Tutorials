import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar(value = 'start value')

# widgets (they share all the same string variable)
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise
ex_stringvar = tk.StringVar(value = 'test')
# ex_stringvar.set('test')
ex_entry1 = ttk.Entry(master = window, textvariable = ex_stringvar)
ex_entry1.pack()
ex_entry2 = ttk.Entry(master = window, textvariable = ex_stringvar)
ex_entry2.pack()
ex_label = ttk.Label(master = window, textvariable = string_var)
ex_label.pack()

# run
window.mainloop()
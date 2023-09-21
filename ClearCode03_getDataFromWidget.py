import tkinter as tk
from tkinter import ttk

def button_func():
    # get content of the entry
    entry_text = entry.get()
    
    # update the label
    # label.configure(text = 'some other text')
    label['text'] = entry_text
    print(label.configure())

def toggle_btn():
    if entry['state'] == 'enabled':
        entry['state'] = 'disabled'
        button['state'] = 'disabled'
    else:
        entry['state'] = 'enabled'
        button['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

toggle_btn = ttk.Button(master = window, text = 'Toggle', command = toggle_btn)
toggle_btn.pack()

# run
window.mainloop()
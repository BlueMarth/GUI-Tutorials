import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Toggle')
window.geometry('600x400')

# place
def toggle_label_place():
    global label_visible

    if label_visible:
        label.place_forget()
        label_visible = False
    else:
        label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        label_visible = True

button = ttk.Button(window, text = 'toggle label', command = toggle_label_place)
button.place(relx = 0.5, rely = 0.9, anchor = 'center')

label_visible = True
label = ttk.Label(window, text = 'A label')
label.place(relx = 0.5, rely = 0.5, anchor = 'center')

# grid
window.columnconfigure((0, 1), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1, uniform = 'a')

# run
window.mainloop()

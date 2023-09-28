import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Toggle')
window.geometry('600x400')

### optino 1 ###
# place
# def toggle_label_place():
#     global label_visible

#     if label_visible:
#         label.place_forget()
#         label_visible = False
#     else:
#         label.place(relx = 0.5, rely = 0.5, anchor = 'center')
#         label_visible = True

# button = ttk.Button(window, text = 'toggle label', command = toggle_label_place)
# button.place(relx = 0.5, rely = 0.9, anchor = 'center')

# label_visible = True
# label = ttk.Label(window, text = 'A label')
# label.place(relx = 0.5, rely = 0.5, anchor = 'center')


### optino 2 ###
# grid
# def toggle_label_grid():
#     global label_visible

#     if label_visible:
#         label.grid_forget()
#         label_visible = False
#     else:
#         label.grid(row = 0, column = 1)
#         label_visible = True


# window.columnconfigure((0, 1), weight = 1, uniform = 'a')
# window.rowconfigure(0, weight = 1, uniform = 'a')
# button = ttk.Button(window, text = 'toggle label', command = toggle_label_grid)
# button.grid(row = 0, column = 0)

# label_visible = True
# label = ttk.Label(window, text = 'A label')
# label.grid(row = 0, column = 1)


### option 3 ###
def toggle_label_pack():
    global label_visible

    if label_visible:
        label.pack_forget()
        frame.pack(expand = True, before = button)
        label_visible = False
    else:
        frame.pack_forget()
        label.pack(expand = True, before = button)
        label_visible = True


label_visible = True
label = ttk.Label(window, text = 'A label')
label.pack(expand = True)

button = ttk.Button(window, text = 'toggle', command = toggle_label_pack)
button.pack()

frame = ttk.Frame(window)

# run
window.mainloop()

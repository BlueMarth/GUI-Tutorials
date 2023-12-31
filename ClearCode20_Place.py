import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Place')
window.geometry('400x600')

label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
button = ttk.Button(window, text = 'Button')

label1.place(x = 300, y = 100, width = 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5) # much easier to use
label3.place(x = 80, y = 60, width = 160, height = 300)
# anchor: choose the positioning point on the widget
button.place(relx = 1, rely = 1, anchor = 'se')


# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text = 'Frame label', background = 'yellow')
frame_btn = ttk.Button(frame, text = 'Frame button')

# frame layout
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)
frame_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
frame_btn.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

## exercise
ex_label = ttk.Label(window, text = 'Exercise label', background = 'orange')
ex_label.place(relx = 0.5, rely = 0.5, relwidth  = 0.5, height = 200, anchor = 'center')

# run
window.mainloop()

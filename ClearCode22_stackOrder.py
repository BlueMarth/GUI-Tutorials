import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Stacking order')
window.geometry('400x400')

label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(window, text = 'Label 2', background = 'red')
label3 = ttk.Label(window, text = 'Label 3', background = 'blue')

# label.lower()
# aboveThis: raise widget ONLY on top of that widget
button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.lift(aboveThis = label2))
# button1 = ttk.Button(window, text = 'raise label 1', command = lambda: label1.tkraise())
# label.tkraise() is the same as label.lift()
button2 = ttk.Button(window, text = 'raise label 2', command = lambda: label2.lift())
button3 = ttk.Button(window, text = 'raise label 3', command = lambda: label3.lift())

# layout
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)
label3.place(x = 20, y = 150, width = 160, height = 120)

button1.place(rely = 1, relx = 0.6, anchor = 'se')
button2.place(rely = 1, relx = 0.8, anchor = 'se')
button3.place(rely = 1, relx = 1, anchor = 'se')

# run
window.mainloop()

import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def ex_func():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label =  ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk text
text = tk.Text(master = window)         # multi line
text.pack()

# ttk entry
entry = ttk.Entry(master = window)      # single line
entry.pack()

# exercise
exercise_Label = ttk.Label(master = window, text = 'my label')
exercise_Label.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

#exercise_Button = ttk.Button(master = window, text = 'Ex btn', command = ex_func)
exercise_Button = ttk.Button(master = window, text = 'Ex btn', command = lambda: print('hello'))
exercise_Button.pack()

# run
window.mainloop() # won't stop until the window is closed

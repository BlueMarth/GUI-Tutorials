import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')
    
button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar()
check1 = ttk.Checkbutton(
    window,
    text = 'Checkbox 1',
    command = lambda: print(check_var.get()),
    # command = lambda: print(type(check_var.get())),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check1.pack()
check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command = lambda: check_var.set(5)
)
check2.pack()

# radio buttons
### if radio button 'values' are not set or are the same, they are all toggled at once! ###
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radiobutton1',
    value = 'radio1',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(
    window,
    text = 'Radiobutton2',
    value = 'radio2',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio2.pack()


## exercise start
def ex_radio_func():
    print(ex_check_bool.get())
    ex_check_bool.set(False)
# data
ex_radio_string = tk.StringVar()
ex_check_bool = tk.BooleanVar()
# widgets
ex_radio1 = ttk.Radiobutton(window, text = 'Radio A', value = 'A', command = ex_radio_func)
ex_radio2 = ttk.Radiobutton(window, text = 'Radio B', value = 'B', command = ex_radio_func)
ex_check = ttk.Checkbutton(window, text = 'exercise check', variable = ex_check_bool,
                           command = lambda: print(ex_radio_string.get()))
# layout
ex_radio1.pack()
ex_radio2.pack()
ex_check.pack()


## exercise end


# run
window.mainloop()
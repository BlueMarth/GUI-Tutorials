import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'Label 1', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')

# middle widget
label3 = ttk.Label(window, text = 'Label 3', background = 'green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Label 4', background = 'orange')
button1 = ttk.Button(bottom_frame, text = 'Button 1')
button2 = ttk.Button(bottom_frame, text = 'Button 2')

# exercise widgets
ex_frame = ttk.Frame(bottom_frame)
ex_button1 = ttk.Button(ex_frame, text = 'Ex Button 1')
ex_button2 = ttk.Button(ex_frame, text = 'Ex Button 2')
ex_button3 = ttk.Button(ex_frame, text = 'Ex Button 3')

# top layout
label1.pack(side = 'left', fill = 'both', expand = True)
label2.pack(side = 'left', fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# middle layout
label3.pack(expand = True)

# bottom layout
button1.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

## exercise layout
ex_button1.pack(expand = True, fill = 'both')
ex_button2.pack(expand = True, fill = 'both')
ex_button3.pack(expand = True, fill = 'both')
ex_frame.pack(side = 'left', expand = True, fill = 'y')
# run
window.mainloop()
# imports
import tkinter as tk
from tkinter import ttk


# setups
rootWidth = 800
rootHeight = 500
rootOffsetx = 100
rootOffsety = 50
root_geometry = str(rootWidth) + 'x' + str(rootHeight) + '+' + str(rootOffsetx) + '+' + str(rootOffsety)
root = tk.Tk()
root.geometry(root_geometry)
root.title('Root')


# widgets
ttk.Button().pack()
ttk.Checkbutton().pack()
ttk.Combobox().pack()
ttk.Entry().pack()
ttk.Frame().pack()
ttk.Label(text = 'label').pack()
ttk.Notebook().pack()
ttk.Progressbar().pack()
ttk.Radiobutton().pack()
ttk.Scale().pack()
ttk.LabeledScale().pack()
ttk.Scrollbar().pack()
ttk.Sizegrip().pack()
ttk.Spinbox().pack()
ttk.Treeview().pack()


# run
root.mainloop()
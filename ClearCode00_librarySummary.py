# imports
import tkinter as tk
from tkinter import ttk


# setup
root = tk.Tk()
root.geometry('600x400+200+100')
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
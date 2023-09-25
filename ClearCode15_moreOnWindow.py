import tkinter as tk
from tkinter import ttk

# window (exercise)
window = tk.Tk()
window.title('window')
window.iconbitmap('python_icon.ico') ### change icon!

displayWidth = 1000
displayHeight = 500
center_x = window.winfo_screenwidth() / 2
center_y = window.winfo_screenheight() / 2
corner_x = int(center_x - displayWidth / 2)
corner_y = int(center_y - displayHeight / 2)
window_geometry = str(displayWidth) + 'x' + str(displayHeight) + '+' + str(corner_x) + '+' + str(corner_y)
window.geometry(window_geometry)


# window sizes
minWidth = 200
minHeight = 100
maxWidth = 800
maxHeight = 600
resize_x = True
resize_y = True
window.minsize(minWidth, minHeight)
# window.maxsize(maxWidth, maxHeight)
# window.resizable(resize_x, resize_y)

# screen attributes
print(window.winfo_screenwidth(), window.winfo_screenheight())

# window attributes
transparency = 0.8
topmost = True
window.attributes('-alpha', transparency)
window.attributes('-topmost', topmost)

# security event
window.bind('<Escape>', lambda event: window.quit())
disable = False
window.attributes('-disable', disable)
fullscreen = False
window.attributes('-fullscreen', fullscreen)

# title bar
hide_title_bar = True
window.overrideredirect(hide_title_bar)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()
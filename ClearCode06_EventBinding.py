# Events:
# Keyboard inputs, widgets getting changed/ selected/ unselected
# Mouse click/ motion/ wheel etc.
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/

### BIND EVENETS TO A WIDGET!! ###
# widget.bind(event, function)
# format: modifier-type-detail

import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y:{event.y}')

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
#window.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
#window.bind('<Alt-KeyPress-a>', lambda event: print(event))
button.bind('<Alt-KeyPress-a>', lambda event: print(event))
#window.bind('<Motion>', get_pos)
text.bind('<Motion>', get_pos)

#window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# run
window.mainloop()
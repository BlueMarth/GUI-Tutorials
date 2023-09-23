import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Surname')
table.heading('email', text = 'Email')
table.pack()

# insert values into a table
table.insert(parent = '', index = 0, values = ('John','Doe','JohnDoe@email.com'))
for i in range(50):
    first = choice (first_names)
    last = choice(last_names)
    email = f'{first[0]}{last}@email.com'
    data = (first, last, email)
    table.insert(parent = '', index = 0, values = data)

# add new item at the bottom of the table
table.insert(parent = '', index = tk.END, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    # table.item(table.selectio())

def delete_items(_):
    for i in table.selection():
        table.delete(i)
    # print('delete')

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()
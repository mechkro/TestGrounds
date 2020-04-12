from tkinter import *
from tkinter import ttk





root = Tk()
root.resizable(FALSE, FALSE)
menu = Menu(root)

p = ttk.Panedwindow(root, orient=VERTICAL)
# first pane, which would get widgets gridded into it:
f1 = ttk.Labelframe(p, text='Pane1', width=100, height=50)
f2 = ttk.Labelframe(p, text='Pane2', width=100, height=50)   # second pane
p.add(f1)
p.add(f2)
p.grid(row = 0, column = 0)

p2 = ttk.Panedwindow(root, orient= HORIZONTAL)
# first pane, which would get widgets gridded into it:
f3 = ttk.Labelframe(p2, text='Pane1', width = 50, height=100)
f4 = ttk.Labelframe(p2, text='Pane2', width= 50, height=100)   # second pane
p2.add(f3)
p2.add(f4)
p2.grid(row = 0, column = 1)


label = Label(root, text = 'Right Click GUI').grid(row = 1,columnspan = 2,padx = 5, pady = 5)
lbox = Listbox(root, width = 25, height = 8)
lbox.grid(row =2, columnspan = 2, padx = 5, pady = 5)

#mapping what should pop up options be in context menu
context_map = {'panned':[],
               'lbox':[],
               'label':[]
               }

for i in ('Copy', 'Edit', 'Remove', 'Tag', 'Select'):
    menu.add_command(label=i)

def what_widget_clicked(x,y):
    
    
if (root.tk.call('tk', 'windowingsystem')=='aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
root.mainloop()

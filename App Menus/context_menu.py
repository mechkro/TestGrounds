import tkinter as tk
from tkinter import ttk


class main:
    def __init__(self, parent, *args):
        self.parent = parent
        self.parent.resizable(tk.FALSE, tk.FALSE)
        self.menu = tk.Menu(self.parent)

        self.frm1 = tk.Frame(self.parent)
        self.frm1.grid(row=0, column = 0, padx = 5, pady = 5)

        self.frm2 = tk.Frame(self.parent)
        self.frm2.grid(row=0, column = 1, padx = 5, pady = 5)


        self.p = ttk.Panedwindow(self.frm1, orient=tk.VERTICAL)
        # first pane, which would get widgets gridded into it:
        self.f1 = ttk.Labelframe(self.p, text='Pane1', width=100, height=50)
        self.f2 = ttk.Labelframe(self.p, text='Pane2', width=100, height=50)   # second pane
        self.p.add(self.f1)
        self.p.add(self.f2)
        self.p.grid(row = 0, column = 0)

        self.p2 = ttk.Panedwindow(self.frm1, orient= tk.HORIZONTAL)
        # first pane, which would get widgets gridded into it:
        self.f3 = ttk.Labelframe(self.p2, text='Pane1', width = 50, height=100)
        self.f4 = ttk.Labelframe(self.p2, text='Pane2', width= 50, height=100)   # second pane
        self.p2.add(self.f3)
        self.p2.add(self.f4)
        self.p2.grid(row = 0, column = 1)


        self.label = tk.Label(self.frm1, text = 'Right Click GUI').grid(row = 1,columnspan = 2,padx = 5, pady = 5)
        self.lbox = tk.Listbox(self.frm1, width = 25, height = 8)
        self.lbox.grid(row =2, columnspan = 2, padx = 5, pady = 5)

        #mapping what should pop up options be in context menu
        self.context_map = {'panned':[],
                       'lbox':[],
                       'label':[]
                       }

        for i in ('Copy', 'Edit', 'Remove', 'Tag', 'Select', 'Cancel'):
            self.menu.add_command(label=i)
            
        if (self.parent.tk.call('tk', 'windowingsystem')=='aqua'):
            self.parent.bind('<2>', lambda e: self.menu.post(e.x_root, e.y_root))
            self.parent.bind('<Control-1>', lambda e: self.menu.post(e.x_root, e.y_root))
        else:
            self.parent.bind('<3>', lambda e: self.menu.post(e.x_root, e.y_root))


        self.nbook = ttk.Notebook(self.frm2)
        self.nbook.bind('<<NotebookTabChanged>>', self.print_changed())

        self.tab1 = tk.Frame(self.nbook)
        self.tab2 = tk.Frame(self.nbook)
        self.tab3 = tk.Frame(self.nbook)
        self.tab4 = tk.Frame(self.nbook)
        self.tab5 = tk.Frame(self.nbook)
        self.tab6 = tk.Frame(self.nbook)
        
        self.b = tk.Button(self.tab1, text='Exit', command= self.parent.destroy)
        self.b.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.EW)

        self.b1 = tk.Button(self.tab1, text='Exit', command= self.parent.destroy)
        self.b1.grid(row = 0,column = 1, padx = 5, pady = 5, sticky = tk.EW)

        self.b2 = tk.Button(self.tab1, text='Exit', command= self.parent.destroy)
        self.b2.grid(row = 0,column = 2, padx = 5, pady = 5, sticky = tk.EW)

        self.b3 = tk.Button(self.tab1, text='Exit', command= self.parent.destroy)
        self.b3.grid(row = 0,column = 3, padx = 5, pady = 5, sticky = tk.EW)

        self.b4 = tk.Button(self.tab1, text='Exit', command= self.parent.destroy)
        self.b4.grid(row = 0,column = 4, padx = 5, pady = 5, sticky = tk.EW)

        self.txt = tk.Text(self.tab1)
        self.txt.grid(row = 1,column = 0, columnspan = 5, padx = 5, pady = 5)


        self.l1 = tk.Listbox(self.tab2)
        self.l1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.EW)
        self.l2 = tk.Listbox(self.tab2)
        self.l2.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.EW)
        self.l3 = tk.Listbox(self.tab2)
        self.l3.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = tk.EW)
        self.l4 = tk.Listbox(self.tab2)
        self.l4.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = tk.EW)
        self.l5 = tk.Listbox(self.tab2)
        self.l5.grid(row = 0, column = 4, padx = 5, pady = 5, sticky = tk.EW)

        self.nbook.add(self.tab1, text = "Not Started", compound= tk.TOP)
        self.nbook.add(self.tab2, text = "In Progress")
        self.nbook.add(self.tab3, text = "Completed")
        self.nbook.add(self.tab4, text = "Not Started", compound= tk.TOP)
        self.nbook.add(self.tab5, text = "In Progress")
        self.nbook.add(self.tab6, text = "Completed")
        self.nbook.grid(row = 0,rowspan = 7, padx = 5, pady = 5, sticky = 'nsew')


    def what_widget_clicked(self,x,y):
        pass

    def print_changed(self,*args):
        print('tab changed')


if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.mainloop()

import tkinter as tk
from test3 import newwin3


class newwin2(object):
    """ """
    
    def __init__(self, master):
        self.master = master
        self.emptycurrent()
        self.addnew()

    #--------------------------------------
    def emptycurrent(self):
        """ """
        
        for i in self.master.winfo_children():
            i.destroy()
        return

    #--------------------------------------
    def addnew(self):
        """ """
        
        self.f = tk.Frame(self.master, bg = 'blue')
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 2',
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        
        self.nw = newwin3(self.master)

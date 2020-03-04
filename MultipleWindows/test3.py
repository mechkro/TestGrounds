import tkinter as tk



class newwin3(object):
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
        self.f = tk.Frame(self.master, bg = 'green')
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 3',
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        self.ll = tk.Label(self.f, text = 'Tada',
                           bg = 'green')
        self.ll.grid(row = 1, padx = 5, pady = 5)

        self.b2 = tk.Button(self.f, text = 'back',
                            command = lambda: self.backwin())
        self.b2.grid(row = 2, padx = 5, pady = 5)

    #--------------------------------------
    def backwin(self):
        """ """
        from oldwin import Recalled
        self.bw = Recalled(self.master)

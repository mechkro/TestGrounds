import tkinter as tk
from test2 import newwin2




class Main(object):
    """ """
    def __init__(self, parent):
        self.parent = parent
        self.f = tk.Frame(self.parent, bg = 'red')
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 1',
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """Func to make an instance in seperate file and use method to pass root frame
        and delete all current child widgets (format) and then create new widgets
        """
        
        self.nw = newwin2(self.parent)




class Recalled(object):
    """If this file wants to be called back, created this to mimic
    the other files which have been called prior.
    I feel this is incorrect way of performing thiscallback but my
    lack of deep understanding of OOP is the cause
    """
    
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
        self.f = tk.Frame(self.master, bg = 'red')
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 1 is back!',
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        self.nw = newwin2(self.master)

    


#--------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()

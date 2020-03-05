import tkinter as tk
from test3 import newwin3


BG = '#0C1021'
FG = 'white'


class newwin2(object):
    """ """
    
    def __init__(self, master, frm, chc):
        self.master = master
        self.frm = frm
        self.chc = chc
        self.emptycurrent()
        self.addnew()

    #--------------------------------------
    def emptycurrent(self):
        """ """
        
        for i in self.frm.winfo_children(): #.master.winfo_children():
            i.destroy()
        return

    #--------------------------------------
    def addnew(self):
        """ """
        
        self.f = tk.Frame(self.frm, bg = BG)
        self.f.grid(padx = 2, pady = 2)

        self.lab = tk.Label(self.f, text = self.chc.upper(), bg = BG,
                            fg = FG)
        self.lab.grid(padx = 5, pady = 5)

        self.l = tk.Button(self.f, text = 'Win 2', bg = BG, fg = FG,
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        
        self.nw = newwin3(self.master, self.frm)



#-------------------------------------------
class Recalled(object):
    """If this file wants to be called back, created this to mimic
    the other files which have been called prior.
    I feel this is incorrect way of performing thiscallback but my
    lack of deep understanding of OOP is the cause
    """
    
    def __init__(self, master, frm):
        self.master = master
        self.frm = frm
        self.emptycurrent()
        self.addnew()

    #--------------------------------------
    def emptycurrent(self):
        """ """
        
        for i in self.frm.winfo_children():  #master.winfo_children():
            i.destroy()
        return

    #--------------------------------------
    def addnew(self):
        """ """
        
        self.f = tk.Frame(self.frm, bg = BG)
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 1 is back!', bg = BG, fg = FG,
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        
        self.nw = newwin2(self.master,self.frm)

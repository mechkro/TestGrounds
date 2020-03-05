import tkinter as tk


BG = '#0C1021'
FG = 'white'



class newwin3(object):
    """ """
    
    def __init__(self, master, frm):
        self.master = master
        self.frm = frm
        self.emptycurrent()
        self.addnew()

    #--------------------------------------
    def emptycurrent(self):
        """ """
        for i in self.frm.winfo_children(): #master.winfo_children():
            i.destroy()
        return

    #--------------------------------------
    def addnew(self):
        """ """
        self.f = tk.Frame(self.frm, bg = BG)
        self.f.grid(padx = 2, pady = 2)

        self.l = tk.Button(self.f, text = 'Win 3', bg = BG, fg = FG,
                           command = lambda: self.newwin())
        self.l.grid(padx = 10, pady = 10)

    #--------------------------------------
    def newwin(self):
        """ """
        self.ll = tk.Label(self.f, text = 'Tada', bg = BG, fg = FG)
        self.ll.grid(row = 1, padx = 5, pady = 5)

        self.b2 = tk.Button(self.f, text = 'back', bg = BG, fg = FG,
                            command = lambda: self.backwin())
        self.b2.grid(row = 2, padx = 5, pady = 5)

    #--------------------------------------
    def backwin(self):
        """ """
        from oldwin import Recalled
        self.bw = Recalled(self.master, self.frm)





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

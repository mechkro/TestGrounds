import tkinter as tk

#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
#-----------------------------------------------------------------------------------

class newtop(tk.Toplevel):
    
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self)
        self.config(bg = BG)
        
        self.parent = parent
        self.parent.iconify()
        
        self.l = tk.Label(self, text = 'YES!!!!!', bg = BG, fg = FG)
        self.l.pack(padx = 10, pady = 10)
        
        self.b = tk.Button(self, text = 'Go back', bg = BG, fg = FG, command = lambda: self.return_to_main())
        self.b.pack(padx = 10, pady = 10)
        
        self.mainloop()
        
        
    def return_to_main(self):
        
        self.destroy()
        self.quit()
        self.parent.deiconify()
        return 
        

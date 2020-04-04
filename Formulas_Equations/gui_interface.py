import systemhead as syshead
import tkinter as tk


params_list = ('Flow rate (Q)(gpm)', 
                        'Pipe Diam. (d)(in)',
                        'Atm Pressure (P)(psi/ft)')
                        



class Main:
    
    #-----------------------------------------------------------------------------
    def __init__(self, parent):
        """ """
        self.parent = parent
        self.f = tk.Frame(self.parent)
        self.f.grid(column = 0)
        
        self.fparams = tk.Frame(self.parent)
        self.fparams.grid(column = 1)
        
        #Iterate through the parameters list to add them as labels along with entry widgets.
        for n,i in enumerate(params_list):
            tk.Label(self.fparams, text = i).grid(row = n, column = 0, padx = 3, pady = 3)
            tk.Entry(self.fparams).grid(row = n, column = 1, padx = 3, pady = 3)
            
        intro = """Welcome to the TDH Calculator interface.
This tool will guide you through the calculation process
for coming up with TDH, NPSHa, Suction Lift...etc"""
        
        self.main_l = tk.Label(self.f, text = intro).grid(row = 0)
        self.main_butt = tk.Button(self.f, text = 'Begin', command = lambda: self.start())
        self.main_butt.grid(row = 1)
    
    
    #-----------------------------------------------------------------------------
    def start(self):
        """ """
        self.f.destroy()
        self.f2 = tk.Frame(self.parent)
        self.f2.grid()
        
        self.l2 =tk.Label(self.f2, text = 'Velocity Head').grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.l3 =tk.Label(self.f2, text = 'Flow (gpm)').grid(row = 1, column = 0,  padx = 5, pady = 5)
        self.l4 =tk.Label(self.f2, text = 'Diam (in)').grid(row = 2, column = 0,  padx = 5, pady = 5)
        
        self.ent1 = tk.Entry(self.f2)
        self.ent1.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        self.ent2 = tk.Entry(self.f2)
        self.ent2.grid(row = 2, column = 1, padx = 5, pady = 5) 
        
        self.butt2 = tk.Button(self.f2, text = 'Calculate', command = lambda: self.vel_head())
        self.butt2.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    
        
    #-----------------------------------------------------------------------------
    def vel_head(self):
        """ """
        e1 = float(self.ent1.get())
        e2 = float(self.ent2.get())
        vhead = syshead.velocity_head(Q = e1, d = e2)
        
        self.butt2.config(text = 'Next')
        self.l5 = tk.Label(self.f2, text = 'Velocity Head = {} ft.'.format(vhead)).grid(row = 4, column = 0, columnspan = 2,  padx = 5, pady = 5)


#-----------------------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    root.title('TDH Calculator')
    Main(root)
    root.mainloop()


import systemhead as syshead
import tkinter as tk


#-----------------------------------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'


#-----------------------------------------------------------------------------
params_list = ('Flow rate (Q)(gpm)', 
                        'Pipe Diam. (d)(in)',
                        'Atm Pressure (P)(psi/ft)')
                        

k = syshead.Variables_present
k.sort()

class Main:
    
    #-----------------------------------------------------------------------------
    def __init__(self, parent):
        """ 
        
        """
        
        self.parent = parent
        
        self.f = tk.Frame(self.parent, bg = BG)
        self.f.grid(row = 0, column = 0, ipadx = 10, ipady = 10)
        
        self.fparams = tk.Frame(self.parent, bg = BG)
        self.fparams.grid(row = 0, column = 1, ipadx = 10, ipady = 10)
        
        self.lf_par = tk.LabelFrame(self.fparams, text = 'Parameters List', bg = BG, fg = FG)
        self.lf_par.grid(padx = 5, pady = 5)
        
        
        ##Iterate through the parameters list to add them as labels along with entry widgets
        #This will auto update each entry with solved values sp user cam have all variables visable
        
        for n,i in enumerate(k[:]):
            tk.Label(self.lf_par, text = i,  bg = BG, fg = FG).grid(row = n, column = 0, padx = 3, pady = 3)
            tk.Entry(self.lf_par, bg = BG, fg = FG ).grid(row = n, column = 1, padx = 3, pady = 3)            
        
            
        intro = """Welcome to the TDH Calculator interface.
This tool will guide you through the calculation process
for coming up with TDH, NPSHa, Suction Lift...etc"""
        
        self.main_l = tk.Label(self.f, text = intro,  bg = BG, fg = FG).grid(row = 0, padx = 10, pady = 5)
        self.main_butt = tk.Button(self.f, text = 'Begin', command = lambda: self.start(), bg = BG, fg = FG)
        self.main_butt.grid(row = 1)
    
    
    #-----------------------------------------------------------------------------
    def start(self):
        """ 
        Function to -----
        """
        
        self.f.destroy()
        self.f2 = tk.Frame(self.parent, bg = BG)
        self.f2.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.l2 =tk.Label(self.f2, text = 'Velocity Head', bg = BG, fg = FG).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.l3 =tk.Label(self.f2, text = 'Flow (gpm)',  bg = BG, fg = FG).grid(row = 1, column = 0,  padx = 5, pady = 5)
        self.l4 =tk.Label(self.f2, text = 'Diam (in)',  bg = BG, fg = FG).grid(row = 2, column = 0,  padx = 5, pady = 5)
        
        self.ent1 = tk.Entry(self.f2,  bg = BG, fg = FG)
        self.ent1.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        self.ent2 = tk.Entry(self.f2,  bg = BG, fg = FG)
        self.ent2.grid(row = 2, column = 1, padx = 5, pady = 5) 
        
        self.butt2 = tk.Button(self.f2, text = 'Calculate', command = lambda: self.vel_head(),  bg = BG, fg = FG)
        self.butt2.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
    
        
    #-----------------------------------------------------------------------------
    def vel_head(self):
        """ """
        
        try:
            e1 = float(self.ent1.get())
            e2 = float(self.ent2.get())
            vhead = syshead.velocity_head(Q = e1, d = e2)
            self.butt2.config(text = 'Next')
            self.l5 = tk.Label(self.f2, text = 'Velocity Head = {} ft.'.format(vhead),  bg = BG, fg = FG).grid(row = 4, column = 0, columnspan = 2,  padx = 5, pady = 5)
            
        except Exception as e:
            tk.Label(self.f2, text = 'Error!', bg = BG, fg = FG, font = ('Verdana', 16, 'bold')).grid(row = 4, column = 0, columnspan = 2,  padx = 5, pady = 5)
            tk.Label(self.f2, text = 'Please revise entered values', bg = BG, fg = FG).grid(row = 5, column = 0, columnspan = 2,  padx = 5, pady = 5)
            print(e)
            
        return


#-----------------------------------------------------------------------------
if __name__ == '__main__':
    """
    """
    
    root = tk.Tk()
    root.title('TDH Calculator')
    root.config( bg = BG)
    Main(root)
    root.mainloop()


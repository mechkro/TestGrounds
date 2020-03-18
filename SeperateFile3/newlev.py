import tkinter as tk
import random
from toplev import newtop


#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'   
#-----------------------------------------------------------------------------------

class Main(object):
    
    fitr = 0
    
    def __init__(self, master):
        
        self.master = master
        self.master.config(bg = BG)
        
        self.cancel_id = None
        
        self.fmaster = tk.Frame(self.master, bg = BG)
        self.fmaster.pack(padx = 5, pady = 5)
        
        self.butt = tk.Button(self.fmaster, text = 'Click\nHere', command = lambda: self.toplev(),
                              bg = BG, fg = FG)
        self.butt.pack(padx = 10, pady = 10)
        
        self.children = self.fmaster.winfo_children()
        self.master.protocol('WM_WINDOW_DELETE', self.destroy_main)
    
    #https://stackoverflow.com/questions/31410462/how-to-stop-a-running-function-without-exiting-the-tkinter-window-entirely
    #def start(self):
            #if(self.cancel_id==None):
                #self.count = 0
                ##self.cancel_id = None
                #self.counter()    
    
    #def counter(self):
        ##self.textBox.delete("1.0", END)
        #if (self.count < 10):
            #self.count += 1
            #self.textBox.insert(END, str(self.count)+'\n\n')
            #self.cancel_id = self.textBox.after(1000, self.counter)
            
    #def stop(self):
            #if self.cancel_id is not None:
                #self.textBox.after_cancel(self.cancel_id)
                #self.cancel_id = None
     
    #---------------------------------------------------------           
    def toplev(self):
        """ 
        """

        newtop(self.master)
        self.master.update()
        
        self.children = self.fmaster.winfo_children()
        self.clearchildren()
        
        self.newwidges()
     
    
    #---------------------------------------------------------
    def clearchildren(self):
        """
        """
        
        for i in self.children:
            i.destroy()
        return
            
            
    #---------------------------------------------------------        
    def newwidges(self):
        """ 
        """
        
        if Main.fitr == 0:
            for g in range(5):
                tk.Button(self.fmaster, text = 'Click\nHere', command = lambda: self.toplev(),
                                      bg = BG, fg = FG).pack(padx = 10, pady = 10) 
            Main.fitr += 1
            return 
        
        if Main.fitr == 1:
            for g in range(5):
                tk.Button(self.fmaster, text = 'Next Buttons', command = lambda: self.toplev(),
                                      bg = BG, fg = FG).pack(padx = 10, pady = 10) 
            Main.fitr += 1
            return
        
        else:
            print('Out of Range')
     
     
    #---------------------------------------------------------  
    def destroy_current_widge(self):
        """ 
        """
        
        k = self.fmaster.winfo_children()
        for i in range(len(k)):
            k[i].destroy()
        print('Succesful deployment')
        return
    
    
    #---------------------------------------------------------
    def destroy_main(self):
        """ 
        """
        
        self.master.destroy()
        



#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    """ """
    
    root = tk.Tk()
    Main(root)
    root.mainloop()

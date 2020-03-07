import tkinter as tk


#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
###########################################

class Initiate(object):
    
    
    #-----------------------------------------------------------------------------------
    def __init__(self, master):
        
        self.master = master
        self.master.config(bg = BG)
        
        self.framehold = {}
        self.labelhold = {}
        self.labelframehold = {}
        itr = 0
        
        for i in range(3):
            for j in range(3):
                
                self.framehold[itr] = self.make_frame().grid(row = i, column = j, padx = 10, pady = 10)   #*[int(i), int(j)])
                if itr <= 2:
                    self.labelframehold[j] = self.make_labelframe(self.framehold[itr], 'Frame {}'.format(itr), *[i, j])
                    self.labelhold[itr] = self.make_label(self.labelframehold[itr], '{}'.format(itr), *[ i, j])
                else:
                    self.labelhold[itr] = self.make_label(self.framehold[itr], '{}'.format(itr), *[ i, j])
                    
                itr += 1
                
                
    
    #-----------------------------------------------------------------------------------
    def make_frame(self,*args):
        """ """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return tk.Frame(self.master, bg = BG)
    
    
    #-----------------------------------------------------------------------------------
    def make_labelframe(self, parent, txt, *args):
        """ """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        lf = tk.LabelFrame(parent, text = txt, bg = BG, fg = FG, font = ('impact',18,'bold'))
        lf.grid(row = args[0], column = args[1], padx = 12, pady = 12)
        return lf
    
    
    #-----------------------------------------------------------------------------------
    def make_label(self, parent,  txt, *args):
        """ 
        After frame is made - we create a label instance for parent frame and then return.
        During creation we call to binding function to add enter and leave functionality
        """
        
        l = tk.Label(parent, text = txt, bg = BG, fg = FG, font = ('impact',18,'bold'))
        l.grid(row = args[0], column = args[1], padx = 12, pady = 12)
        self.add_binding(l)     #Add Binding to functionality before returning the label to dictionary
        
        return l   
    
    
    #-----------------------------------------------------------------------------------
    def add_binding(self, widge):
        """ """
        
        widge.bind('<Enter>', self.change_txt_color)
        widge.bind('<Leave>', self.change_txt_def_color)
        return
        
    
    #-----------------------------------------------------------------------------------
    def change_txt_color(self, event):
        """ """
        
        event.widget.config(fg = DGR, font = ('impact',24,'bold'))
        return 
        
    #-----------------------------------------------------------------------------------
    def change_txt_def_color(self, event):
        """ """
        
        event.widget.config(fg = FG, font = ('impact',18,'bold'))
        return         
        
    
        



if __name__ == '__main__':
    root = tk.Tk()
    Initiate(root)
    root.mainloop()
        

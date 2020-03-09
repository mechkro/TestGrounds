import tkinter as tk
import random


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
        """ 
        
        """
        
        self.master = master
        self.master.title('Trello Clone')
        self.master.config(bg = BG)
        
        #Create the dictionariess to hold our widgets
        self.framehold = {}
        self.labelhold = {}
        self.labelframehold = {}
        self.texthold = {}
        self.listboxhold = {}
        
        col_titles = ['Not Started', 'In Progress', 'Completed']
        col_desc = ['items that have not been looked into', 'Click each line for entry details', 'Items that have been completed']
        itr = 0
        
        for i in range(3):
            for j in range(3):
                
                self.framehold[itr] = self.make_frame().grid(row = i, column = j, padx = 5, pady = 5)   #*[int(i), int(j)])
                
                if itr <= 2:
                    self.labelframehold[j] = self.make_labelframe(self.framehold[itr], '{}'.format(col_titles[itr]), *[i, j])
                    self.labelhold[itr] = self.make_label(self.labelframehold[itr], '{}'.format(col_desc[itr]), *[ i, j])
                    
                if 2 < itr <= 5:
                    #self.texthold[itr-3] = self.make_text(self.framehold[itr], *[i,j])
                    self.listboxhold[itr -3] = self.make_listbox(self.framehold[itr], *[i,j])
                    txt = 'This is label frame {}'.format(itr-2)
                    self.listboxhold[itr-3].insert(tk.END, txt)
                    
                if itr > 5:
                    self.texthold[itr-3] = self.make_text(self.framehold[itr], *[i,j])
                    txt = 'This is label frame {}'.format(itr-2)
                    self.texthold[itr-3].insert(tk.END, txt)                    
                    #self.labelhold[itr] = self.make_label(self.framehold[itr], '{}'.format(itr), *[ i, j])
                    
                itr += 1
        
        
        self.butt_fwd_col1 = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        self.butt_fwd_col1.grid(row = 4, rowspan = 2, column = 0, pady = 5, sticky = tk.EW)
        
        self.butt_fwd_col1.bind('<Button-1>', self.button_binding_1)
        
        self.butt_fwd_col2_left = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        self.butt_fwd_col2_left.grid(row = 4, column = 1, pady = 5, sticky = tk.EW)
        
        self.butt_fwd_col2_left.bind('<Button-1>', self.button_binding_2_left)
        
        self.butt_fwd_col2_right = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        self.butt_fwd_col2_right.grid(row = 5, column = 1, pady = 5, sticky = tk.EW)
        
        self.butt_fwd_col2_right.bind('<Button-1>', self.button_binding_2_right)        
        
        self.butt_fwd_col3 = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        self.butt_fwd_col3.grid(row = 4, rowspan = 2, column = 2, pady = 5, sticky = tk.EW)
        
        self.butt_fwd_col3.bind('<Button-1>', self.button_binding_3)
        
        self.buttonhold = {1:self.butt_fwd_col1,
                                      2:self.butt_fwd_col2_left,
                                      3:self.butt_fwd_col2_right,
                                      4:self.button_binding_3}
        
        
        for i in range(50):
            vals = list(self.listboxhold.values())
            k = random.choice(vals)
            self.testing_entries(k,i)

                
    
    #-----------------------------------------------------------------------------------
    def testing_entries(self, widge, ent):
        """ 
        
        """    
        txt = 'This is label frame {}'.format(ent)
        return widge.insert(tk.END, txt)
        
    
    #-----------------------------------------------------------------------------------
    def make_frame(self,*args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return tk.Frame(self.master, bg = BG)
    
    
    #-----------------------------------------------------------------------------------
    def make_labelframe(self, parent, txt, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
            
        lf = tk.LabelFrame(parent, text = txt, bg = BG, fg = FG, font = ('Vardana',18,'bold'))
        lf.grid(row = args[0], column = args[1], padx = 5, pady = 5, sticky = tk.EW)
        return lf
    
    
    #-----------------------------------------------------------------------------------
    def make_listbox(self, parent, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        lb = tk.Listbox(parent, bg = BG, fg = FG, font = ('impact',8,'normal'), width = 37, height = 12)
        lb.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return lb   
    
    
    #-----------------------------------------------------------------------------------
    def make_text(self, parent, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        t = tk.Text(parent, bg = BG, fg = FG, font = ('impact',8,'normal'), width = 37, height = 7)
        t.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return t
    
    #-----------------------------------------------------------------------------------
    def make_label(self, parent,  txt, *args):
        """ 
        After frame is made - we create a label instance for parent frame and then return.
        During creation we call to binding function to add enter and leave functionality
        """
        
        l = tk.Label(parent, text = txt, bg = BG, fg = FG, font = ('Vardana',10,'normal'))
        l.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        self.add_binding(l)     #Add Binding to functionality before returning the label to dictionary
        
        return l   
    
    
    #-----------------------------------------------------------------------------------
    def add_binding(self, widge):
        """ 
        
        """
        
        widge.bind('<Enter>', self.change_txt_color)
        widge.bind('<Leave>', self.change_txt_def_color)
        return
        
    
    #-----------------------------------------------------------------------------------
    def change_txt_color(self, event):
        """ 
        
        """
        
        event.widget.config(fg = DGR, font = ('Vardana',10,'normal'))
        return 
        
        
    #-----------------------------------------------------------------------------------
    def change_txt_def_color(self, event):
        """ 
        
        """
        
        event.widget.config(fg = FG, font = ('Vardana',10,'normal'))
        return         
        
        
    #-----------------------------------------------------------------------------------
    def button_binding_1(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[0].get(tk.ACTIVE)
            self.listboxhold[0].delete(tk.ACTIVE)
            self.listboxhold[1].insert(tk.END, select) 
            
        except:
            print('failed')
     
       
    #-----------------------------------------------------------------------------------       
    def button_binding_2_left(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[1].get(tk.ACTIVE)
            self.listboxhold[1].delete(tk.ACTIVE)
            self.listboxhold[0].insert(tk.END, select)        
            
        except:
            print('failed')
    
    
    #-----------------------------------------------------------------------------------       
    def button_binding_2_right(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[1].get(tk.ACTIVE)
            self.listboxhold[1].delete(tk.ACTIVE)
            self.listboxhold[2].insert(tk.END, select)        
            
        except:
            print('failed')
            
    
    #-----------------------------------------------------------------------------------
    def button_binding_3(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[2].get(tk.ACTIVE)
            self.listboxhold[2].delete(tk.ACTIVE)
            self.listboxhold[1].insert(tk.END, select)      
            
        except:
            print('failed')
        
      


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    """ """
    
    root = tk.Tk()
    Initiate(root)
    root.mainloop()
        

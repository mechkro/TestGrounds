import tkinter as tk
import random as rand


BG =  '#0C1021'
FG = 'white'

chc = """COMPANY NAME
INDUSTRY
STATE
CITY
FIRST NAME
LAST NAME/SFX
LAST DATE
TYPE	NOTE
POSITION
CONT #1
CONT #2
EMAIL
MANF PURCHASED
PROCESS
OFFICE ADDRESS
DRIVE TO SITE
WEBSITE
LINKEDIN
LOC. OPENS
CONT. HOURS
BLANK""".split('\n')



#---------------------------------------------------------------------------------------------
class Main(object):
    
    #---------------------------------------------------------------------------------------------
    def __init__(self, master):
        self.master = master
        self.master.config(bg = BG)
        
        self.f = tk.Frame(self.master, bg = BG)
        self.f.grid()
        
        #self.txt = tk.Text(self.f)
        #self.txt.grid(row = 0, padx = 5, pady = 5)
        self.entr_hold = []
        
        self.lbox = tk.Listbox(self.f, bg = BG, fg = FG)
        self.lbox.grid(row = 0, padx = 5, pady = 5)
        
        self.lbox.bind('<Button-1>', self.get_rank)
        
        self.upb = tk.Button(self.f, text = 'Up', bg = BG, fg = FG, command = lambda: self.move_up(self.lbox.index(tk.ACTIVE)))
        self.upb.grid(row = 1, padx = 5, pady = 5, sticky = tk.EW)
        
        self.downb = tk.Button(self.f, text = 'Down', bg = BG, fg = FG, command = lambda: self.move_down(self.lbox.index(tk.ACTIVE)))
        self.downb.grid(row = 2, padx = 5, pady = 5, sticky = tk.EW) 
        
        self.searchlab = tk.Label(self.f, text = 'Search Listbox', bg = BG, fg = FG)
        self.searchlab.grid(row = 3, padx = 5, pady = 5)
        
        self.searchentry = tk.Entry(self.f, bg = BG, fg = FG)
        self.searchentry.grid(row = 4, padx = 5, pady = 5)
        
        self.searchbutt = tk.Button(self.f, text = 'Search', bg = BG, fg = FG, command = lambda: self.seekitem(self.searchentry.get()))
        self.searchbutt.grid(row = 5, padx = 5, pady = 5)     
        
        self.tracker = {}
        self.load_rand()
    
    
    #---------------------------------------------------------------------------------------------    
    def seekitem(self, element):
        """
        
        """
    
        temp = {}
        for x,y in enumerate(self.lbox.get(0, "end")):
            
            if y == element:
                temp[x] = y
            else:
                pass
            
        print('Matches located at the following indexes:\n')
        print(temp.keys())
        
        for k in temp.keys():
            self.lbox.itemconfig(k, bg = 'black', fg = 'dark goldenrod')
            
        
                
    #---------------------------------------------------------------------------------------------    
    def load_rand(self):
        """
        
        """
        
        for i in range(10):
            rchc = rand.choice(chc)
            self.tracker[i] = rchc
            self.entr_hold.append(rchc)
            self.lbox.insert(tk.END, rchc)
        
        self.catalog()
    
        return
    
    
    #---------------------------------------------------------------------------------------------    
    def load_refresh(self, rnk):
        """
        
        """
        
        self.lbox.delete(0, tk.END)
        for v in self.tracker.values():
            self.lbox.insert(tk.END, v)
        
        self.lbox.selection_set(rnk)            #This keeps the highlighted indicator for the current selected entry
        self.lbox.activate(rnk)                   #Even though line is highlighted it is not the "ACTIVE" entry, so we must invoke that
        
        if self.lbox.index(tk.ACTIVE) == 0:
            self.upb.config(state = tk.DISABLED)
        
        if self.lbox.index(tk.ACTIVE) == self.lbox.index(tk.END):
            self.downb.config(state = tk.DISABLED)
        
        elif 0 < self.lbox.index(tk.ACTIVE) < self.lbox.index(tk.END):
            self.upb.config(state = tk.NORMAL)
            self.downb.config(state = tk.NORMAL)
            
        #self.catalog()
        return        
    
     
    
    #--------------------------------------------------------
    def catalog(self):
        """
        
        """
        
        cat = [i for i in self.lbox.get(0, tk.END)]
        itr = 0
        self.cathold = {}
        for i in cat:
            self.cathold[i] = itr
            itr += 1
        
        print(self.cathold.items())
        return self.cathold.items()
    
    
    def pull_rank(self):
        return self.lbox.index(tk.ACTIVE)

    
    #-------------------------------------------------------
    def get_rank(self, event):
        """ 
        
        """
        pr = self.pull_rank()
        if pr == 0:#event.widget.index(tk.ACTIVE) == 0:
            self.upb.config(state = tk.DISABLED)
        if pr == self.lbox.index(tk.END):#event.widget.index(tk.ACTIVE) == self.lbox.index(tk.END):
            self.downb.config(state = tk.DISABLED)
        if pr != 0:
            self.upb.config(state = tk.NORMAL)
        else:
            pass
        
        #for k,v in self.tracker.items():
            #if v == pos:
                #return (k,v)
    
    
    #---------------------------------------------------------------------------------------------
    def move_up(self, pos):
        """
        
        """
        
        sel, bel = pos, pos-1
        tempcopy = self.tracker.copy()
        self.tracker[sel] = tempcopy[bel]
        self.tracker[bel] = tempcopy[sel]
        self.load_refresh(bel)
    
    
    #---------------------------------------------------------------------------------------------
    def move_down(self, pos):
        """
        
        """
        
        ####################################################
        #BUG - Button wont properly disable like Move up function permits
        ####################################################
        if (pos+1) == self.lbox.index(tk.END):
            self.downb.config(state = tk.DISABLED)
            self.load_refresh(pos)
            
        else:
            sel, abv = pos, pos+1
            tempcopy = self.tracker.copy()
            self.tracker[sel] = tempcopy[abv]
            self.tracker[abv] = tempcopy[sel]
            self.load_refresh(abv)
    
    
#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()

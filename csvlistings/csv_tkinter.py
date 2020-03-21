import tkinter as tk
import random as rand
from decimal import Decimal
import time

columns = """COMPANY NAME
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
BLANK"""

cols = columns.split('\n')

poss = """email1@test.com
email2@test.com
email3@test.com
email4@test.com
email5@test.com
email6@test.com
email7@test.com
email8@test.com
email9@test.com
email10@test.com
email11@test.com
"""

poss_p = poss.split('\n')


#----------------------------------------------------------------------------
class Main(object):
    
    def __init__(self, master):
        self.master = master

        self.f = tk.Frame(self.master, bg = 'dark goldenrod')
        self.f.grid(row = 0, padx = 10, pady = 10)
        
        #Mapping out the row and column coordinates for the listboxes
        grid_layout = [(0,1),(0,2),(0,3),
                       (1,1),(1,2),(1,3),
                       (2,1),(2,2),(2,3),
                       (3,1),(3,2),(3,3),
                       (4,1),(4,2),(4,3),
                       (5,1),(5,2),(5,3),
                       (6,1),(6,2),(6,3)]
        
        
        but_layout = [(0,1),(0,2),(0,3),
                       (1,1),(1,2),(1,3),
                       (2,1),(2,2),(2,3),
                       (3,1),(3,2),(3,3),
                       (4,1),(4,2),(4,3),
                       (5,1),(5,2),(5,3),
                       (6,1),(6,2),(6,3),
                       (7,1),(7,2),(7,3),
                       (8,1),(8,2),(8,3),
                       (9,1),(9,2),(9,3),
                       (10,1),(10,2),(10,3),
                       (11,1),(11,2),(11,3),
                       (12,1),(12,2),(12,3),
                       (13,1),(13,2),(13,3),
                       (14,1),(14,2),(14,3),
                       (15,1),(15,2),(15,3)]
        
        
        lf_hold = {}
        holdr = {}
        b_hold = {}
        
        self.todohold = {}
        
        self.timestart = time.time()

        #WIDGET CREATION ~~~~~~~~~~~~
        for x,i in enumerate(grid_layout):
            lf_hold[x] = self.make_lframe("{}".format(cols[x]),i[-1],i[0])
            holdr[x] = self.make_lbox(lf_hold[x], 0, 0)
            
            #This will be where we make calls to funcs to insert data to perspective 
            for z in range(25):
                pass 
                #holdr[x].insert(tk.END, rand.choice(poss_p))

        #BINDING ASSIGNMENT ~~~~~~~~~~~~
        for v in lf_hold.values():
            v.bind('<Button-1>', self.change_clr)
            v.bind('<Double-Button-1>', self.clr_def)
            
        for v in holdr.values():
            v.bind('<Enter>', self.change_clr)
            v.bind('<Leave>', self.clr_def)
            v.bind('<Double-Button-1>', self.add_time)
            

        self.bot_txt = tk.Text(self.f, height = 7, bg = 'black', fg = 'white',  cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.bot_txt.grid(row = 4, column = 0, columnspan = 7, padx = 3, pady = 3, sticky = tk.EW)
        
        
        self.botframe = tk.Frame(self.master, bg = 'black')
        self.botframe.grid(row = 1, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        
        #-----------------------------------------------------------
        for x,i in enumerate(but_layout):
            b_hold[x] = self.to_do_buttons(self.botframe, i[-1], i[0])     

    #----------------------------------------------------------------------------
    def add_time(self, event):
        """
        Func to calculate the time difference since program started and then
        insert it into the clicked widget
        """
        
        diff = time.time()-self.timestart
        diff_print = Decimal(str(diff)).quantize(Decimal("0.01"))
        if 60 <= diff <= 3600:
            minz = diff/60.0
            minz_print = Decimal(str(minz)).quantize(Decimal("0.01"))
            event.widget.insert(tk.END, '{} min'.format(minz_print))
            self.master.title("TK - Last Clicked {} mins ago".format(minz_print))
        else:
            event.widget.insert(tk.END, '{} sec'.format(diff_print))
            self.master.title("TK - Last Clicked {}'s ago".format(diff_print))
        return
            
        
    #----------------------------------------------------------------------------
    def make_lframe(self, txt, r, c):
        """
        Func to create the labelframe widgets
        """
        
        lf = tk.LabelFrame(self.f, bg = 'black', fg = 'khaki1', text = txt, font = ('Verdana',8,'bold'))
        lf.grid(row = r, column = c, padx = 3, pady = 3)
        return lf


    #----------------------------------------------------------------------------
    def make_lbox(self, par, r, c):
        """
        Func to makelistbox widget - will be used to load data into
        """
        
        lb = tk.Listbox(par, bg = 'black', fg = 'white')
        lb.grid(row = r, column = c, padx = 3, pady = 3)
        lb.insert(tk.END, 'Row = {}\nCol = {}'.format(r,c))
        return lb


    #----------------------------------------------------------------------------
    def change_clr(self, event):
        """ 
        
        """
        
        event.widget.config(bg = 'dark goldenrod')
        return


    #----------------------------------------------------------------------------
    def clr_def(self, event):
        """ 
        
        """
        
        event.widget.config(bg = 'black')
        return
    
    
    #----------------------------------------------------------------------------
    def  to_do_buttons(self, par, r, c):
        """ 
        
        """
        
        tdb = tk.Button(par, text = ' - na - ', bg = 'black', fg = 'white', command = lambda: self.load_clicked_todo(tdb))
        tdb.grid(row = r, column = c, padx = 7, pady = 5)
    
    
    def load_clicked_todo(self, w):
        """
    
        """
        if w.cget('bg') == 'black':
            w.config(bg = 'blue')
            ToDoAdd(self.master)
        else:
            w.config(bg = 'black')
        return
    
    
    
class ToDoAdd:
    def __init__(self, parent, *args):
        
        self.tl = tk.Toplevel()
        self.parent = parent
        
        self.tlframe = tk.Frame(self.tl, bg = 'black')
        self.tlframe.grid(padx = 5, pady = 5)
        
        self.L = tk.Label(self.tlframe, text = 'Hello World', bg = 'black', fg = 'white')
        self.L.grid(padx = 5, pady = 5)
        
        self.close_butt = tk.Button(self.tlframe, text = 'Ok', bg = 'black', fg = 'white', command = lambda: self.close_todo)
        self.close_butt.grid(row = 1, padx = 5, pady = 5)
        
        self.tl.mainloop()
    
    def close_todo(self):
        pass

#----------------------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()

import tkinter as tk



BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'


class WidgetMaker:
    
    #----------------------------------------------------------------------------------------------
    def create_frames(self, *args):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create Label widget 
        """
        
        t = tk.Frame(self,  bg = BG)
        t.grid(row = args[0], column = args[1], columnspan = args[2], sticky = tk.NS)
        return t
    
    #----------------------------------------------------------------------------------------------
    def create_labels(self, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create Label widget 
        """
        
        pass
    
    #----------------------------------------------------------------------------------------------
    def create_entries(self, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create Entry widget 
        """
        
        pass
    
    
    #----------------------------------------------------------------------------------------------
    def create_labframe(self, frm, txt):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create LabelFrame widget 
        """
        
        return tk.LabelFrame(frm, text = txt, bg =  BG,  fg =  FG, font = ('Verdana',8,'bold'), cursor = 'hand2')
 
    
    
    #----------------------------------------------------------------------------------------------
    def create_listbox(self, frm, h, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create LabelFrame widget 
        
        frm = Frame or parent widget
        h = height of widget
        w = width of widget
        """
        return tk.Listbox(frm, height = h, width = w, bg = BG, fg = FG, font = ('Verdana', 8, 'normal'), cursor = 'hand2')    

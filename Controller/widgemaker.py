import tkinter as tk


#---------------------------------------------------------------------------------------------------------------
class Widget_Maker:
    
    #---------------------------------------------------------------------------------------------------------------
    def __init__(self, designation, parent, *args):
        self.designation = designation
        self.parent = parent
    
        if self.designation == 'LABELFRAME':
            self.make_labelframe(parent, args)
            
        if self.designation == 'LABEL':
            self.make_label(parent, *args)
            
        if self.designation == 'ENTRY':
            self.make_entry(parent, args)
            
        if self.designation == 'BUTTON':
            self.make_button(parent, *args)
            
        if self.designation == 'TEXT':
            self.make_text(parent, args)
            
        if self.designation == 'LISTBOX':
            self.make_listbox(parent, args) 
            
        if self.designation == 'COMBOBOX':
            self.make_combobox(parent, args)
        
    
    #LABELFRAME WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_labelframe(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.lf = tk.LabelFrame(parent, text = args[0], bg = args[1], fg = args[2], font = args[3], command = None)
        self.lf.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.lf
    
    
    #LABEL WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_label(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.l = tk.Label(parent, text = args[0], bg = args[1], fg = args[2], font = args[3])
        self.l.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.l
    
    
    #ENTRY WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_entry(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.lf = tk.LabelFrame(parent, text = args[0], bg = args[1], fg = args[2], font = args[3])
        self.lf.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.lf    
    
    
    #BUTTON WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_button(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.b = tk.Button(parent, text = args[0], bg = args[1], fg = args[2], font = args[3], command = args[4])
        self.b.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.b
    
    
    #TEXT WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_text(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.lf = tk.LabelFrame(parent, text = args[0], bg = args[1], fg = args[2], font = args[3])
        self.lf.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.lf    
    
    
    #LISTBOX WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_listbox(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.lf = tk.LabelFrame(parent, text = args[0], bg = args[1], fg = args[2], font = args[3])
        self.lf.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.lf        
    
    
    #COMBOBOX WIDGET
    #---------------------------------------------------------------------------------------------------------------
    def make_combobox(self, parent, *args):
        """ 
        Parent = frame or widget to place widget in
        ARGS ORDER:
        
        -text,
        -background color
        -foreground color
        -font settings: (font, font size, bold/normal)
        -row
        -rowspan
        -column 
        -columnspan
        -padx
        -pady
        -sticky setting
        """
        
        self.lf = tk.LabelFrame(parent, text = args[0], bg = args[1], fg = args[2], font = args[3])
        self.lf.grid(row = args[-1][0], rowspan = args[-1][1], column = args[-1][2], columnspan = args[-1][3], padx = args[-1][4], pady = args[-1][5], sticky = args[-1][6])
        return self.lf           
    

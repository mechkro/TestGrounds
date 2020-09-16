import tkinter as tk
from tkinter import ttk
import datetime as dt
import tkcalendar as tcal


"""
Program Description:

After continuing to develop my DXP app there has been some concerns in regards to asthetic and feel of using the platform.
Still feels like to much going on and too many clicks required between applications you want to use.

Further optimizing the workflow is the goal with this code.
"""

BG = 'dark gray'
FG = 'grey2'
DGR = 'white'

class MainWin:

    def __init__(self, parent):
        self.parent = parent
        self.parent.config(bg = BG)
        
        self.top = tk.Frame(self.parent, bg = BG)
        self.top.grid(row = 0)
        self.bot = tk.Frame(self.parent, bg = BG)
        self.bot.grid(row = 1)
        
        
        self.menu_1 = tk.Menu(self.parent)

        menu_1_opts = {'Meeting': self.test_1,
                                    'CallLog Entry': self.test_2,
                                    'Bid Due': self.test_3,
                                    'FollowUp': self.test_4,
                                    'See All': self.test_5}

        for k,v in menu_1_opts.items():
            self.menu_1.add_command(label = k, command = v)

        self.menu_2 = tk.Menu(self.parent)
        menu_2_opts = {'Edit': self.test_6,
                                    'Delete': self.test_7,
                                    'Archive': self.test_8}

        for k,v in menu_2_opts.items():
            self.menu_2.add_command(label = k, command = v)
            
        self.lbox1 = tk.Listbox(self.top, height = 10)
        self.lbox1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NSEW)
        
        
        today = dt.date.today()
        mindate = dt.date(year=(int(2020)-1), month = int(today.month), day = int(today.day))
        maxdate = today + dt.timedelta(days=365)
        
        self.cal = tcal.Calendar(self.top, font="Arial 14", selectmode='day', locale='en_US',
                            background = BG, foreground = FG, headersbackground = BG, headersforeground = DGR,
                            bordercolor = DGR,normalbackground = BG, normalforeground = FG,
                            weekendbackground = BG, weekendforeground = FG,
                            selectbackground = DGR, selectforeground = 'black',
                            othermonthforeground = 'dim gray', othermonthbackground = BG,
                            othermonthweforeground = 'dim gray', othermonthwebackground = BG,
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            tooltipbackground = BG, tooltipforeground = DGR,
                            date_pattern = 'yyyy mm dd',
                            cursor="hand1", year = int(today.year), month = int(today.month), day = int(today.day))

        self.cal.grid(row = 1, column = 0, padx = 25, pady = 25, sticky = tk.NSEW)
        
        self.lbox2 = tk.Listbox(self.bot, height = 10)
        self.lbox2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NSEW)
        
        #MENU 1------------------------------------------------------------------
        #if (self.tk.call('tk', 'windowingsystem')=='aqua'):
        if self.lbox1.selection_get():
            self.lbox1.bind('<2>', lambda e: self.menu_1.post(e.x_root, e.y_root))
            self.lbox1.bind('<Control-1>', lambda e: self.menu_1.post(e.x_root, e.y_root))
        else:
            pass
            
        #else:
        if self.lbox1.curselection() != None:
            self.lbox1.bind('<3>', lambda e: self.menu_1.post(e.x_root, e.y_root))
            self.lbox1.bind('<Double-Button-1>', self.double_click_open)
        else:
            pass
        
        #MENU 2------------------------------------------------------------------
        #if (self.tk.call('tk', 'windowingsystem')=='aqua'):
        if self.lbox2.selection_get():
            self.lbox2.bind('<2>', lambda e: self.menu_2.post(e.x_root, e.y_root))
            self.lbox2.bind('<Control-1>', lambda e: self.menu_2.post(e.x_root, e.y_root))
        else:
            pass
            
        #else:
        if self.lbox2.curselection() != None:
            self.lbox2.bind('<3>', lambda e: self.menu_2.post(e.x_root, e.y_root))
            self.lbox2.bind('<Double-Button-1>', self.double_click_open)
        else:
            pass


    ############################################################################
    #MENU SELECTED DRIVEN OPTIONS--------------------------------------------
    #----------------------------------------------------------
    def test_1(self):
        """
        Pop up menu selection triggered -'MEETING
        """
        print('Test MEETING worked')
        return

    #----------------------------------------------------------
    def test_2(self):
        """
         Pop up menu selection triggered -'CALL LOG ENTRY
        """

        print('Test CALL LOG ENTRY worked')
        return

    #----------------------------------------------------------
    def test_3(self):
        """
         Pop up menu selection triggered -'BID DUE
        """

        print('Test BID DUE worked')
        return

    #----------------------------------------------------------
    def test_4(self):
        """
         Pop up menu selection triggered - FOLLOW UP
        """

        print('Test FOLLOW UP worked')
        return

    #----------------------------------------------------------
    def test_5(self):
        """
        Pop up menu selection triggered -'COPY'
        """
        print('Test SEE ALL worked')
        return

    #----------------------------------------------------------
    def test_6(self):
        """
         Pop up menu selection triggered -'EDIT'
        """

        print('Test EDIT worked')
        return

    #----------------------------------------------------------
    def test_7(self):
        """
         Pop up menu selection triggered -'DELETE'
        """

        print('Test DELETE worked')
        return

    #----------------------------------------------------------
    def test_8(self):
        """
         Pop up menu selection triggered -'ARCHIVE'
        """

        print('Test ARCHIVE worked')
        return


    def double_click_open(self, event):
        """ """
        
        x = event.x
        y = event.y
        print(f"Clicked @ Point {x},{y}")
        return









if __name__ == '__main__':
    root = tk.Tk()
    MainWin(root)
    root.mainloop()

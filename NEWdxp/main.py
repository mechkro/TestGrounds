import tkinter as tk
from tkinter import ttk
#import tkcalendar as tcal


"""
Program Description:

After continuing to develop my DXP app there has been some concerns in regards to asthetic and feel of using the platform.
Still feels like to much going on and too many clicks required between applications you want to use.

Further optimizing the workflow is the goal with this code.
"""


class MainWin:
    
    def __init__(self, parent):

        self.parent = parent

        self.top = tk.Frame(self.parent)
        self.top.grid(row = 0)
        self.bot = tk.Frame(self.parent)
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
        
        
        








if __name__ == '__main__':
    root = tk.Tk()
    MainWin(root)
    root.mainloop()
    

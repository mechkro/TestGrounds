import tkinter as tk
import collections as clc
#import tkMessageBox as tkm
import sqlite3 as sql


"""
Post-it type reminder board -----------

Each "Sticky" note entry is represented as a button.
    - Color designation, i.e. "red" -- urgent... etc
    - Detailed view window
        - When "Enter" button -- call to pull up buttons stored note


CURRENT ISSUES:

    - Moing in and out of the boxes is lagging and sometimes misses the binding event
    - There has to be a que function to solve this, but I dont think so without
    stalling all other actions as python does not support multiprocess
    - Could try threads, but it would be a call to it after any other action.....
    
"""


BG = 'dark goldenrod'
FG = 'black'

class MemoBoard(tk.Tk):

    current_pages = 1
    pages = clc.OrderedDict()
    
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.menu = tk.Menu(self, bg = BG, fg = FG)
        self.add_menu_commands()    
        self.bind('<3>', lambda e: self.menu.post(e.x_root, e.y_root))
        
        self.start_db_func()
        
        self.frame = tk.Frame(self, bg = 'gray')
        self.frame.grid()

        self.flab = tk.Label(self.frame, text = 'Click Button\nto ADD newnote',
                             bg = 'grey', fg = 'black',font = ('Verdana', 12, 'bold'))
        self.flab.grid(row = 0, column = 0, columnspan = 6, padx = 5, pady = 5)

        self.leftb = tk.Button(self.frame, text = '<', command = lambda: None, bg = 'grey', fg = 'black')
        self.leftb.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.rightb = tk.Button(self.frame, text = '>', command = lambda: None, bg = 'grey', fg = 'black')
        self.rightb.grid(row = 1, column = 5, padx = 5, pady = 5)

        self.noteframe = tk.LabelFrame(self.frame, text = 'Notes', bg = 'grey', fg = 'black')
        self.noteframe.grid(row = 2, column = 0, columnspan = 6, padx = 5, pady = 5)

        self.buttonmap = {}
        self.nhold = {}
        itr = 1
        
        for i in range(5):
            for j in range(6):
                self.varstr = tk.StringVar()
                self.nhold[str(itr)] = self.note_grid_config(i,j, itr)
                itr += 1

        self.pagel = tk.Label(self.frame, text = 'Page 1 of {}'.format(MemoBoard.current_pages), bg = 'grey', fg = 'black')
        self.pagel.grid(row = 3, column = 0, columnspan = 6, padx = 5, pady = 5)

        self.fbut = tk.Button(self.frame, text = 'ADD Note', command = lambda: None, bg = 'grey', fg = 'black')
        self.fbut.grid(row = 4, column = 0, columnspan = 6, padx = 5, pady = 5)

        self.wm_protocol("WM_DELETE_WINDOW", self.on_cancel)


    def add_menu_commands(self):
        """ """
        
        #for i in ('Copy', 'Edit', 'Remove', 'Tag', 'Select', 'Cancel'):
        self.menu.add_command(label='Copy', command = lambda: self.mouse_click('Copy'))
        self.menu.add_command(label='Edit', command = lambda: self.mouse_click('Edit'))
        self.menu.add_command(label='Remove', command = lambda: self.mouse_click('Remove'))
        self.menu.add_command(label='Tag', command = lambda: self.mouse_click('Tag'))
        self.menu.add_command(label='Select', command = lambda: self.mouse_click('Select'))
        self.menu.add_command(label='Cancel', command = lambda: self.mouse_click('Cancel'))
        return
    



    #----------------------------------------------------
    def mouse_click(self, txt):
        """ """

        director = {
                'Copy': self.copy_func,
                'Edit': self.edit_func,
                'Remove': self.remove_func,
                'Tag': self.tag_func,
                'Select': self.select_func,
                'Cancel': self.cancel_func,
            }

        director[txt]()


    #-----------------------------------------------------
    def copy_func(self):
        """ """
        print('copy func called')
        self.menu2 = tk.Menu(self.menu, bg = BG, fg = FG)
        self.menu2.add_command(label='Copy', command = lambda: None)
        self.bind('<3>', lambda e: self.menu2.post(e.x, e.y))
        
    #-----------------------------------------------------
    def edit_func(self):
        """ """
        print('edit func called')
    #-----------------------------------------------------
    def remove_func(self):
        """ """
        print('remove func called')
    #-----------------------------------------------------
    def tag_func(self):
        """ """
        print('tag func called')
    #-----------------------------------------------------
    def select_func(self):
        """ """
        print('select func called')
    #-----------------------------------------------------
    def cancel_func(self):
        """ """
        print('cancel func called')


    #-----------------------------------------------------
    def print_text(self):
        """ """
        
        print(self.varstr.get())




    #---------------------------------------------------
    def start_db_func(self):
        """

        """
        
        self.c = sql.connect(':memory:')
        self.c.execute("""CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, date TEXT, note TEXT);""")
        self.c.commit()
        print('Succesful DB')
        return


    #---------------------------------------
    def on_cancel(self):
        """
        On user click of the x close button in corner of window. Will destroy the window
        """
        
        self.destroy()

    
    #-------------------------------------------------------    
    def note_grid_config(self,r,c, itr):
        """

        """
        
        b = tk.Button(self.noteframe, text = 'xxxx-xx-xx', command = lambda: self.add_memo(str(itr)), bg = 'grey', fg = 'black')
        b.grid(row = r, column = c)
        self.buttonmap[str(itr)] = (r,c, b)
        #b.bind('<Enter>', self.enter_widget)
        #b.bind('<Leave>', self.leave_widget)
        return b

    #---------------------------------------------------------------------
    def check_if_txt(self, s):
        """

        """

        
        if MemoBoard.pages[s]:
            self.add_memo(s, MemoBoard.pages[s])


    #--------------------------------------------------------------------------------------
    def add_memo(self, s, txt = None):
        """Func to make new toplevel widget frame, to house a text box. Allowing the
        user to enter a new memo.

        NEED TO:
                  - destroy window after submit button is clicked
                  - Color theme add
                  - Make button just show X and change color on main page
        """
        
        self.tlevel = tk.Toplevel()

        self.memolab = tk.Label(self.tlevel, text = 'Enter MEMO', fg = 'black', font = ('Verdana', 12, 'bold'))
        self.memolab.grid(row = 0, padx = 5, pady = 5)
        
        self.txt = tk.Text(self.tlevel,bg = 'grey', fg = 'black', font = ('Verdana', 12, 'bold'))
        self.txt.grid(row = 1, padx = 5, pady = 5)

        if not txt:
            pass
        else:
            self.txt.insert(tk.END, txt)
        
        self.entb = tk.Button(self.tlevel, text = 'Submit', bg = 'grey', fg = 'black', font = ('Verdana', 12, 'bold'),
                              command = lambda: self.grab_memo(self.txt.get(1.0, tk.END), s))
        self.entb.grid(row = 2, padx = 5, pady = 5, sticky = tk.EW)

        for i in self.buttonmap.values():
            print(i[-1].cget('text'))

        self.tlevel.protocol("WM_DELETE_WINDOW", lambda: self.tlevel.destroy())
        self.tlevel.mainloop()


    #---------------------------------------------------
    def grab_memo(self, txt, w):
        """ """
        holdr = txt     #NEED to have this stored in db. where we can call on it instead of making actual dislay main show it
        date = '2020-04-17'
        c = self.c.cursor()
        c.execute("""INSERT INTO test (date, note) VALUES (?,?)""", (date, holdr))
        c.close()
        print('Succesful DB Insert')

        self.c.commit()
        self.print_db_content()
        
        self.nhold[w].config(text = date, bg = 'red', fg = 'white')
        
        MemoBoard.pages[w] = holdr
        self.tlevel.destroy()


    #----------------------------------------------------
    def print_db_content(self):
        c = self.c.cursor()
        c.execute("""SELECT * FROM test""")
        for i in c.fetchall():
            print(i)

        c.close()
        print('Succesful DB Select')

    #-------------------------------------------
    def ignore(self):
        """ """
        
        pass

    
    #-----------------------------------------
    def check_if_color(self):
        """ """
        
        for b in self.nhold.values():
            pass            


    #----------------------------------------
    def enter_widget(self, event):
        """

        """
        
        event.widget.config(bg = 'black', fg = 'white', text = 'X')
        
        return event.widget.update()
       

    #--------------------------------------
    def leave_widget(self, event):
        """ """
        
        event.widget.config(bg = 'grey', fg = 'black', text = '-')
        
        return event.widget.update()


    #-------------------------------------------------------
    def pop_up_details(self, winfoloc):
        """ """
        
        pass



#--------------------------------------------------------
if __name__ == '__main__':
    app = MemoBoard()           #Call to main app - class inherits from tkTK
    app.mainloop()

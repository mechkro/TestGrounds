import Tkinter as tk
import ttk
import calendar as cal
import collections as clc
import datetime as dt 



#Color settings
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'

class MainLogin:
    
    def __init__(self, master):
        self.master = master
        self.master.config(bg = BG)
        self.master.title('Main Login')
        
        #MENUBAR CREATION--------------------------------------------------------------------------------------------------
        self.menubar = tk.Menu(self.master, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu = tk.Menu(self.menubar, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu.add_command(label="Logout", command = lambda: None)#ToDo(master))
        #self.filemenu.add_command(label="Tools", command = lambda: None)
        #self.filemenu.add_command(label="Call Log", command = lambda: None) #CallLog(master))
        self.menubar.add_cascade(label="Account", menu = self.filemenu)
        
        self.master.config(menu = self.menubar)

        self.navtab_lframe = tk.LabelFrame(self.master, text = 'Nav Tabs', bg = BG, fg = FG)
        self.navtab_lframe.grid(row = 0, column =0, padx = 5, pady = 5, sticky = tk.NS)

        self.login_lframe = tk.LabelFrame(self.master, text = 'Login', bg = BG, fg = FG)
        self.login_lframe.grid(row = 0, column = 1, columnspan = 4, padx = 5, pady = 5, sticky = tk.NSEW)
        
        self.navtab_param = {
                            'Accounts':(0,0),
                            'Contacts':(1,0),
                            'Projects/Quotes':(2,0),
                            'To Do':(3,0),
                            'Call Log':(4,0),
                            'Calc/Convert':(5,0),
                            'Calendar':(6,0)
                            }
        
        self.navtab_butt_hold = {}

        for k,v in self.navtab_param.items():
            self.maker_button(k, *v)

        self.instruct_text = 'Please enter your username and password\nto continue. If this is your\nfirst time, please hit register!'
        self.login_instruct_label = tk.Label(self.login_lframe, text = self.instruct_text, bg = BG, fg = FG)
        self.login_instruct_label.grid(row = 0, column = 1, columnspan = 2, padx = 25, pady =  15)

        self.log_uname = tk.Label(self.login_lframe, text = 'Username', bg = BG, fg = FG)
        self.log_uname.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_uname_ent = tk.Entry(self.login_lframe, bg = BG, fg = FG)
        self.log_uname_ent.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_uname_ent.bind('<Enter>', self.change_color_event)
        self.log_uname_ent.bind('<Leave>', self.change_color_event_def)

        self.log_pass = tk.Label(self.login_lframe, text = 'Password', bg = BG, fg = FG)
        self.log_pass.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_pass_ent = tk.Entry(self.login_lframe, bg = BG, fg = FG)
        self.log_pass_ent.grid(row = 4, column = 2, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_pass_ent.bind('<Enter>', self.change_color_event)
        self.log_pass_ent.bind('<Leave>', self.change_color_event_def)

        self.log_submit_butt = tk.Button(self.login_lframe, text = 'Submit',
                                         bg = BG, fg = FG, command = lambda: self.remove_nav_disable())
        self.log_submit_butt.grid(row = 6, column = 1, columnspan = 2, padx = 5, pady = 3, sticky = tk.EW)
        
        self.register_butt = tk.Button(self.login_lframe, text = 'Register',
                                         bg = BG, fg = FG, command = lambda: self.new_register_screen())
        self.register_butt.grid(row = 7, column = 1, columnspan = 2, padx = 5, pady = 3, sticky = tk.EW)        

        self.master_widget_hold = [i for i in self.navtab_butt_hold.values()]
        for widge in self.master_widget_hold:
            widge.bind('<Enter>', self.change_color_event)
            widge.bind('<Leave>', self.change_color_event_def)
    
    
    #---------------------
    def new_register_screen(self):
        """ """
        pass
    
    
    #--------------------------------------------------------------------------
    def maker_button(self, txt, *args):
        """

        """
        
        self.navtab_butt_hold[txt] = tk.Button(self.navtab_lframe, text = txt, command = lambda: None, bg = BG, fg = FG,
                                               state = 'disabled')                                              #Disabled until user passes login checks
        self.navtab_butt_hold[txt].grid(row = args[0], column = args[1], padx = 1, pady = 1, sticky = tk.EW)

        return

    #--------------------------------------------------------------------------
    def change_color_event(self, event):
        """ """
        if event.widget == self.log_uname_ent:
            self.log_uname.config(fg = DGR)

        if event.widget == self.log_pass_ent:
            self.log_pass.config(fg = DGR)
            
        else:
            widge = [i for i in self.master_widget_hold if i == event.widget]
            if not widge:
                pass
            else:
                widge.pop().config(fg = DGR)

    #--------------------------------------------------------------------------
    def change_color_event_def(self, event):
        """ """
        if event.widget == self.log_uname_ent:
            self.log_uname.config(fg = FG)

        if event.widget == self.log_pass_ent:
            self.log_pass.config(fg = FG)
            
        else:
            widge = [i for i in self.master_widget_hold if i == event.widget]
            if not widge:
                pass
            else:
                widge.pop().config(fg = FG)        


    def remove_nav_disable(self):
        """

        """
        
        for v in self.navtab_butt_hold.values():
            v.config(state = 'normal')
        for child in self.login_lframe.winfo_children():
            child.destroy()
        h = self.after_login_window()
        print(h.items())
        self.cbox = ttk.Combobox(self.login_lframe, values = [i for i in h.values()])
        self.cbox.grid()
        
        
    def after_login_window(self):
        """ 
        Gather all of the years dates and put them in string format to pass to combo box
        """
        
        x = cal.Calendar()
        ents = x.yeardatescalendar(2020,width = 1)
        holdr = clc.OrderedDict()
        for n,a in enumerate(ents):
            holdr[n] = []
            for b in a[:]:
                for c in b[:]:
                    for d in c[:]:
                        holdr[n].append(dt.datetime.strftime(d, '%Y-%m-%d'))
        return holdr
                        


if __name__ == '__main__':
    root = tk.Tk()
    MainLogin(root)
    root.mainloop()

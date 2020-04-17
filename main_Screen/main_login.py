import tkinter as tk
from tkinter import ttk



class MainLogin:
    def __init__(self, master):
        self.master = master

        self.navtab_lframe = tk.LabelFrame(self.master, text = 'Nav Tabs')
        self.navtab_lframe.grid(row = 0, column =0, padx = 5, pady = 5, sticky = tk.NS)

        self.login_lframe = tk.LabelFrame(self.master, text = 'Login')
        self.login_lframe.grid(row = 0, column = 1, columnspan = 4, padx = 5, pady = 5, sticky = tk.NSEW)
        
        self.navtab_param = {
                            'Accounts':(0,0),
                            'Contacts':(1,0),
                            'Projects/Quotes':(2,0),
                            'To Do':(3,0),
                            'Call Log':(4,0),
                            'Calc/Convert':(5,0)
                            }
        
        self.navtab_butt_hold = {}

        for k,v in self.navtab_param.items():
            self.maker_button(k, *v)

        self.instruct_text = 'Please enter your username and password\nto continue. If this is your\nfirst time, please hit register!'
        self.login_instruct_label = tk.Label(self.login_lframe, text = self.instruct_text)
        self.login_instruct_label.grid(row = 0, column = 1, columnspan = 2, padx = 25, pady =  15)

        self.log_uname = tk.Label(self.login_lframe, text = 'Username')
        self.log_uname.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_uname_ent = tk.Entry(self.login_lframe)
        self.log_uname_ent.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_uname_ent.bind('<Enter>', self.change_color_event)
        self.log_uname_ent.bind('<Leave>', self.change_color_event_def)

        self.log_pass = tk.Label(self.login_lframe, text = 'Password')
        self.log_pass.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_pass_ent = tk.Entry(self.login_lframe)
        self.log_pass_ent.grid(row = 4, column = 2, columnspan = 2, padx = 5, pady =  5, sticky = tk.EW)

        self.log_pass_ent.bind('<Enter>', self.change_color_event)
        self.log_pass_ent.bind('<Leave>', self.change_color_event_def)

        self.log_submit_butt = tk.Button(self.login_lframe, text = 'Submit', command = lambda: self.remove_nav_disable())
        self.log_submit_butt.grid(row = 6, column = 1, columnspan = 2, padx = 5, pady = 3, sticky = tk.EW)


    def maker_button(self, txt, *args):
        """

        """
        
        self.navtab_butt_hold[txt] = tk.Button(self.navtab_lframe, text = txt, command = lambda: None,
                                               state = 'disabled')                                              #Disabled until user passes login checks
        self.navtab_butt_hold[txt].grid(row = args[0], column = args[1], padx = 1, pady = 1, sticky = tk.EW)

        return


    def change_color_event(self, event):
        """ """
        if event.widget == self.log_uname_ent:
            self.log_uname.config(fg = 'red')

        if event.widget == self.log_pass_ent:
            self.log_pass.config(fg = 'red')

    def change_color_event_def(self, event):
        """ """
        if event.widget == self.log_uname_ent:
            self.log_uname.config(fg = 'black')

        if event.widget == self.log_pass_ent:
            self.log_pass.config(fg = 'black')


    def remove_nav_disable(self):
        """

        """
        
        for v in self.navtab_butt_hold.values():
            v.config(state = 'normal')
        for child in self.login_lframe.winfo_children():
            child.destroy()
        
        return


if __name__ == '__main__':
    root = tk.Tk()
    MainLogin(root)
    root.mainloop()

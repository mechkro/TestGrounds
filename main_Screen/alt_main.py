import tkinter as tk
from test_one import ToDo



"""
This is the controller file - will act as the traffic director for active and non-active windows based
upon end user.
"""


#Color designations for the app theme to be used with widgets
#----------------------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
G = 'green'



#Storage for each of the windows paramters to be called 
#----------------------------------------------------------------
def config_frame(index):
    """ 
    Configuring the different widget types and there 'standard' settings
    - (The class window, (background clr, foreground color, (font)))
    """
    
    fconfig = {'LoginWindow':(BG,FG,('system',12,'bold')),
                    'AccountsContacts':(BG,FG,('system',12,'bold')),
                    'ToDo':(BG,FG,('system',12,'bold')),
                    'CallLog':(BG,FG,('system',12,'bold')),
                    'Projects':(BG,FG,('system',12,'bold')),
                    'BidSolicits' : (BG,FG,('system',12,'bold'))
                   }
    
    return fconfig[index]   #returns whatever key is passed as index




############ MASTER CLASS ####################################
#-----------------------------------------------------------------------------------
class MainStart(tk.Tk):
    
    #-------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """ 
        Mainstart inherits directly from tk.TK
        """
        
        tk.Tk.__init__(self, *args, **kwargs)

        #Foundation frame represents the main frame which all children widgets will be created and placed on
        #-----------------------------------------
        frame_foundation = tk.Frame(self)
        frame_foundation.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        frame_foundation.grid_rowconfigure(0, weight = 1)
        frame_foundation.grid_columnconfigure(0, weight = 1)

        #Classes are stored --- to be called and passed to show window
        #---------------------------------
        self.window_container = {}
        for wins in (LoginWindow, AccountsContacts, ToDo, CallLog, Projects, BidSolicits):
                    window = wins(frame_foundation, self)                       #Passing reference to all
                    self.window_container[wins] = window
                    window.grid(row = 0, column = 0, sticky = tk.NSEW)
        
        self.show_window(LoginWindow)


    #------------------------------------------------------------
    def show_window(self, logwin):        
        """
        Is passed the window to display as well as change of the window titile based on the 
        windo that has been passed.
        """
        window_title = {
                                LoginWindow:'Login Screen',
                                AccountsContacts:'Accounts and Contacts',    #TestWindow:'Test1',
                                ToDo:'To Do List',
                                CallLog:'CallLog Sheet',
                                Projects:'Projects and Quotes',
                                BidSolicits:'Bid Solicitations'
                            }
        
        self.title(window_title[logwin])                #Change the window titile to match the currently passed one            
        frame = self.window_container[logwin]     #Call the window class according to passed window
        frame.tkraise()






############ LOGIN WINDOW ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class LoginWindow(tk.Frame):
    
    #------------------------------------------------------
    def __init__(self, parent, controller):
        """ 
        Controller is an instance passed to provide buttons with which window
        is to be raised. Each of the windows is currently written as seperate classes.
        """
        
        tk.Frame.__init__(self, parent)
    
        conf = config_frame('LoginWindow')
        self.config(bg = conf[0]) 
        
        
        #Frame Containers
        #----------------------------------------------------------------------------------------
        self.navframe = tk.Frame(self, bg = BG)
        self.navframe.grid(row = 0, column = 0, sticky = tk.NS)        
        self.alterframe = tk.Frame(self, bg = BG)
        self.alterframe.grid(row = 0, column = 1, columnspan = 6, sticky = tk.NSEW)
        
        #Labelframe Container
        #-----------------------------------------------------------------------------------------
        self.txt_lframe = tk.LabelFrame(self.alterframe, text = 'Text Widget', bg = BG, fg = FG)
        self.txt_lframe.grid(row = 0 , column = 0, padx = 10, pady = 10, sticky = tk.NSEW) 
        
        
        #Event Bindings for the labelframe - Change color when in and out of focus
        #-----------------------------------------------------------------------------------
        self.txt_lframe.bind('<Enter>', self.widget_focus_color)
        self.txt_lframe.bind('<Leave>', self.widget_focus_color_def)
        
        
        #Text Widget creation
        #--------------------------------------------------------
        self.txt = tk.Text(self.txt_lframe, bg = BG, fg = FG,
                           selectbackground = DGR, selectforeground = 'black', selectborderwidth = 1)
        self.txt.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NSEW) 
        
        #TEXT widget tags 
        """
        The currently available configuration options for tags are: "background", "bgstipple",
        "borderwidth", "elide", "fgstipple", "font", "foreground", "justify", "lmargin1", "lmargin2",
        "offset", "overstrike", "relief", "rmargin", "spacing1", "spacing2", "spacing3", "tabs",
        "tabstyle", "underline", and "wrap". Check the reference manual for detailed descriptions of these.
        The "tag cget" method allows you to query the configuration options of a tag.
        
        Because multiple tags can apply to the same range of text, there is the possibility for conflict 
        (e.g. two tags specifying different fonts). A priority order is used to resolve these; the most 
        recently created tags have the highest priority, but priorities can be rearranged using the 
        "tag raise" and "tag lower" methods.
        """
        
        self.txt.tag_add('highlightline', '5.0', '6.0')
        self.txt.insert('end', 'new material to insert', ('highlightline', 'recent', 'warning'))
        
        self.txt.insert('end', 'first text', ('important'))
        self.txt.tag_configure('important', foreground='red')
        self.txt.insert('end', 'second text', ('important'))
        
        self.txt.tag_bind('important', '<1>', self.popupImportantMenu)
        
       
       #Button Widgets - Navigation to and from different screens
       #--------------------------------------------------------------------------------------------------------------
        b_0 = tk.Button(self.navframe, text = 'TestOne', command  = lambda: controller.show_window(TestWindow))
        b_1 = tk.Button(self.navframe, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self.navframe, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self.navframe, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self.navframe, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self.navframe, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))


        widges_buttons = [b_1, b_2, b_3, b_4, b_5]          #Store buttons in list to be iterated through
        
        
        #Provide buttons grid coordinates and binding event.
        #---------------------------------------------------------------------
        for x, i in enumerate(widges_buttons):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)
            i.bind('<Enter>', self.widget_focus_color)
            i.bind('<Leave>', self.widget_focus_color_def)


        #Configure label widget
        #----------------------------------------------------------------------
        label = tk.Label(self.navframe, text = 'Login')
        label.grid(row = 0, column = 0,  padx = 5, pady = 5, sticky = tk.EW)
        label.config(bg = BG, fg = 'green', font = 'Verdana 18 bold')
    
    
    #----------------------------------------------------------    
    def popupImportantMenu(self, event):
        """ 
        When tagged item in text widget is clicked <1> a pop up menu is rendered.
        Add commands with other function calls
        """
        radio = tk.StringVar()
        menu = tk.Menu(self, bg = BG, fg = FG, font = 'Verdana 12 bold')
        menu.add_command(label = 'Yes', command = lambda: self.pop_up_decision('yes'))
        menu.add_command(label = 'No', command = lambda: self.pop_up_decision('no'))
        menu.add_command(label = 'Cancel', command = lambda: self.pop_up_decision('cancel'))
        #menu.add_radiobutton(label='Cancel', variable=radio, value=1)
        menu.post(event.x_root, event.y_root)
    
    #----------------------------------------------------------    
    def pop_up_decision(self, response):
        """ 
        Takes the choice made from the pop up window and carries out functionality
        """
        
        if response == 'yes':
            self.txt.tag_configure('important', foreground= DGR)
        if response == 'no':
            self.txt.tag_configure('important', foreground= 'white')
        if response == 'cancel':
            pass      
    
    
    #----------------------------------------------------------
    def widget_focus_color(self, event):
        """ 
        When cursor has entered widget it triggers this event -- inteded to help user identify
        cursor location and the widget the app currently recognizes
        """
        
        return event.widget.config(fg = DGR)
    
    
    #---------------------------------------------------------
    def widget_focus_color_def(self, event):
        """ 
        This function is triggered when the mouse cursor has left the widget and it no longer
        is considered to have focus
        """
        
        return event.widget.config(fg = FG)        

            
        
            


############ ACCOUNTS AND CONTACTS ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class AccountsContacts(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        conf = config_frame('AccountsContacts')
        self.config(bg = conf[0])
        

        #Button Widgets - Navigation to and from different screens
        #--------------------------------------------------------------------------------------------------------------       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts), state = tk.DISABLED)
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo), state = tk.NORMAL)
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog), state = tk.NORMAL)
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects), state = tk.NORMAL)
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits), state = tk.NORMAL)


        widges_buttons = [b_1, b_2, b_3, b_4, b_5]       #Store buttons in list to be iterated through
        
        
        for x,i in enumerate(widges_buttons):
                i.config(bg = conf[0], fg = conf[1], font = conf[2])
                i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)
                i.bind('<Enter>', self.widget_focus_color)
                i.bind('<Leave>', self.widget_focus_color_def)
        
        
        #Configure label widget
        #----------------------------------------------------------------------        
        label = tk.Label(self, text = 'Accounts &\nContacts')
        label.grid(row = 0, column = 0,  padx = 5, pady = 5, sticky = tk.EW)
        label.config(bg = BG, fg = 'green', font = 'Verdana 16 bold')
        
        
    #----------------------------------------------------------    
    def widget_focus_color(self, event):
        """ """
        return event.widget.config(fg = DGR)
        
                                   
    #----------------------------------------------------------
    def widget_focus_color_def(self, event):
        """ """
        return event.widget.config(fg = FG)
    
    
    

############ ACCOUNTS AND CONTACTS ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class ToDo(tk.Frame):
    
    def __init__(self, parent, controller):
        """ """
        
        tk.Frame.__init__(self, parent)
        
        conf = config_frame('ToDo')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'To Dos')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts), state = tk.NORMAL)
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo), state = tk.DISABLED)
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog), state = tk.NORMAL)
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects), state = tk.NORMAL)
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits), state = tk.NORMAL)

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)

        label.config(fg = 'green')





############ ACCOUNTS AND CONTACTS ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class CallLog(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('CallLog')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Call Logs')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts), state = tk.NORMAL)
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo), state = tk.NORMAL)
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog), state = tk.DISABLED)
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects), state = tk.NORMAL)
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits), state = tk.NORMAL)

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)

        label.config(fg = 'green')




############ ACCOUNTS AND CONTACTS ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class Projects(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('Projects')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Projects')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts), state = tk.NORMAL)
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo), state = tk.NORMAL)
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog), state = tk.NORMAL)
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects), state = tk.DISABLED)
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits), state = tk.NORMAL)

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)

        label.config(fg = 'green')




############ ACCOUNTS AND CONTACTS ############################
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
class BidSolicits(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('BidSolicits')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'BidSolicits')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts), state = tk.NORMAL)
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo), state = tk.NORMAL)
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog), state = tk.NORMAL)
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects), state = tk.NORMAL)
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits), state = tk.DISABLED)

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5, sticky = tk.EW)

        label.config(fg = 'green')




#Initialize 
#-----------------------------------------
if __name__ == '__main__':
    app = MainStart()
    app.mainloop()

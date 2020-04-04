#Create hiracchical treeview Application  
import tkinter as tk 
from tkinter import ttk
import sqlite3 as sql
import random
import calendar as cal
import datetime as dt
import time
import parsedatetime as pdt
import collections as clc

BG = '#0C1021'
FG = 'white'

C = """
Here would go my contacts list
but have revised do to sensitive information
"""

cdata = '''

Here would normally be my contacts list in a CSV format
Removed due to sensitivity of information

'''


#Operations to parse the data
cdata_seperate = cdata.split('\n')
C_comma_sep = [i.split(',') for i in cdata_seperate]

C_seperate = C.split('\n')

contacts_hold = clc.OrderedDict()

for i in C_seperate:
    contacts_hold[i] = []
    
    for j in C_comma_sep:
        
        if j[0] == i:
            contacts_hold[i].append(j)
            
        else:
            pass

data_hold = clc.OrderedDict()



#GOOGLE API DRIVE CALL and STORAGE OF DATA ----------------------------------------------------------------------
def get_spreadsheet_data():
    """
    Func - to call the google spreadsheet that has been shared through Google API.
    This func will pull all the data fields and store them in a variable to be called upon.
    This will limit our API calls to a minimum (updating cells, deleting cells, etc.)

    *Must be sure the sheet file is saved as google sheet and NOT .xscl
    #Source - https://www.youtube.com/watch?v=cnPlKLEGR7E
    """
    
    try:
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("floc", scope)
        client = gspread.authorize(creds)
        sheet = client.open("Copy of Main_AccountsContacts").sheet1                 #***** Make sure file saved as sheet not excel format on drive
        data = sheet.get_all_records()
        
    except Exception as e:
        print(e)

    return


#----------------------------------------------------------------
def grab_spreadsheet_cell(row, col):
    """
    Func to pull whatever cell coorelates to the row and col values passed by user
    """

    pass

    
        
#----------------------------------------------------------
class ContactsHub(tk.Frame):

    contacts_track = []
    
    def __init__(self, parent, *args, **kwargs):
        """
        Func to house an more encompassing widget base
        - Left side listbox of account names
        - Selecting names brings up list of contacts and profile page info
        - 
        """
        self.s = None
        
        tk.Frame.__init__(self,parent, bg = BG)
        self.grid(sticky = tk.NSEW)

        #First row label ----------------------------------------------------------------------
        self.lab_top = tk.Label(self, text = 'Account Selected: -', bg = BG, fg = FG)
        self.lab_top.grid(row = 0, columnspan = 4, padx = 5, pady = 5, sticky = tk.EW)

        #Listboxes --------- 4 Columns ------------------------------------------------------------------
        #Column 1 ---------
        self.left_labelF = tk.LabelFrame(self, text = 'ACCOUNT LIST', bg = BG, fg = FG)     
        self.left_labelF.grid(row = 1, rowspan = 3, column = 0, padx = 5, pady = 5, sticky = tk.NS)
        #Column 2 ---------
        self.right_labelF = tk.LabelFrame(self, text = 'CONTACTS', bg = BG, fg = FG)
        self.right_labelF.grid(row = 1, rowspan = 3, column = 1, sticky = tk.NS)
        #Column 3 ---------
        self.right21_labelF = tk.LabelFrame(self, text = 'To Follow - 1', bg = BG, fg = FG)
        self.right21_labelF.grid(row = 1, column = 2, padx = 5, pady = 5)
        self.right22_labelF = tk.LabelFrame(self, text = 'To Follow - 2', bg = BG, fg = FG)
        self.right22_labelF.grid(row = 2, column = 2, padx = 5, pady = 5)
        self.right23_labelF = tk.LabelFrame(self, text = 'To Follow - 3', bg = BG, fg = FG)
        self.right23_labelF.grid(row = 3, column = 2, padx = 5, pady = 5)
        #Column 4 ---------
        self.right3_labelF = tk.LabelFrame(self, text = 'Selected Contact', bg = BG, fg = FG)
        self.right3_labelF.grid(row = 1, rowspan = 3, column = 3, padx = 5, pady = 5, sticky = tk.NS)

        
        #Column 1 - Widgets
        #Listbox of contacts-----------------------------------------------------------------------
        self.lbox = tk.Listbox(self.left_labelF, bg = BG, fg = FG, width = 30, height = 19,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.lbox.grid(row = 0, rowspan = 2, column = 0, padx = 5, pady = 5)

        self.b = tk.Button(self.left_labelF, text = 'OPEN PROFILE PAGE', bg = BG, fg = FG,
                           command = lambda: None)
        self.b.grid(row = 2, padx = 5, pady = 5, sticky = tk.EW)

        self.b_new = tk.Button(self.left_labelF, text = 'ADD NEW', bg = BG, fg = FG,
                           command = lambda: None)
        self.b_new.grid(row = 3, padx = 5, pady = 5, sticky = tk.EW)

        self.b_cont_new = tk.Button(self.right_labelF, text = 'ADD NEW', bg = BG, fg = FG,
                           command = lambda: None)
        self.b_cont_new.grid(row = 2, padx = 5, pady = 5, sticky = tk.EW)

        #Column 2 - Widgets
        #------------------------------------------------------------------------------------------
        self.rlbox = tk.Listbox(self.right_labelF, bg = BG, fg = FG, width = 30, height = 20,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.rlbox.grid(row = 0, column = 0, padx = 5, pady = 5)

        #Column 3, row 2 - Widgets
        #------------------------------------------------------------------------------------------ 
        self.rlbox2 = tk.Listbox(self.right21_labelF, bg = BG, fg = FG, width = 25, height = 5,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.rlbox2.grid(row = 1, column = 0, padx = 5, pady = 5)

        #Column 3, row 2 - Widgets
        #------------------------------------------------------------------------------------------ 
        self.rlbox2 = tk.Listbox(self.right22_labelF, bg = BG, fg = FG, width = 25, height = 5,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.rlbox2.grid(row = 2, column = 0, padx = 5, pady = 5)

        #Column 3, row 3 - Widgets
        #------------------------------------------------------------------------------------------ 
        self.rlbox2 = tk.Listbox(self.right23_labelF, bg = BG, fg = FG, width = 25, height = 5,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.rlbox2.grid(row = 2, column = 0, padx = 5, pady = 5)

        #Column 4 - Widgets
        #------------------------------------------------------------------------------------------ 
        self.lbutton3 = tk.Button(self.right3_labelF, text = '<-', bg = BG, fg = FG,
                                    command = lambda: self.load_prev(self.ky))
        self.lbutton3.grid(row = 3, column = 0,  padx = 5, pady = 5, sticky = tk.EW)
        
        self.rlbox3 = tk.Listbox(self.right3_labelF, bg = BG, fg = FG, width = 55, height = 20,
                                 selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2)
        self.rlbox3.grid(row = 0, rowspan = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

        self.rbutton3 = tk.Button(self.right3_labelF, text = '->', bg = BG, fg = FG,
                                    command = lambda: self.load_next(self.ky))
        self.rbutton3.grid(row = 3, column = 1,  padx = 5, pady = 5, sticky = tk.EW)
        
        #------------------------------------------------------------------------------------------ 
        self.lab = tk.Label(self, text = 'Days since last contacted: -', bg = BG, fg = FG, font = 12)
        self.lab.grid(row = 4, column = 0, columnspan = 4, padx = 5, pady = 5, sticky = tk.EW)

        self.init_accounts(self.lbox)
        self.lbox.bind('<Button-1>', self.lbox_selected)
        self.rlbox.bind('<Double-Button-1>', self.contact_selected)


    #----------------------------------------------------
    def init_accounts(self, widge):
        """
        Func to insert the Account names as listed in the spreadhseet to insert into listbox
        """
        
        self.c = C.split('\n')
        
        for i in self.c:
            
            k = len(contacts_hold[i])
            widge.insert(tk.END, i) #'{}: {} Entries'.format(i, k))


    #----------------------------------------------------
    def lbox_selected(self, event):
        """
        Func that when event is captured i.e. button click on item. We take selected line and
        call our holding dict with contact info and display those that match the keyword
        """

        #Columns to be used for display of search results so user knows what text relates to
        cols = ('COMPANY NAME','STATE,CITY','FIRST NAME','LAST NAME.SFX',
                'LAST DATE','NOTE','POSITION', 'CONT #1','CONT #2','EMAIL','MANF PURCHASED',
                'PROCESS','OFFICE/SITE ADDRESS','WEBSITE','LINKEDIN','LOC. OPENS','CONT. HOURS')

        self.tracker = clc.OrderedDict()
        trackitr = 0
        
        pick = event.widget.get(tk.ACTIVE)
        self.lab_top.config(text = 'Account Selected: {}'.format(pick))
        self.rlbox.delete(0,tk.END)                                                         #Switched all rlbox2's to rlbox

        self.rlbox.insert(tk.END, '    ACCOUNT: {}'.format(pick.upper()))   
        self.rlbox.insert(tk.END, " ")

        loc_itr = 0                                 #Iterator variable to keep track of entry number

        self.ent_range_itr = {}
        
        for i in contacts_hold[pick]:               #Iterate through all the values in key of selected line
            itr_qty = len(contacts_hold[pick])
            loc_itr += 1

            #self.rlbox.tag_configure('{}'.format(loc_itr), fg = 'dark goldenrod')
            self.rlbox.insert(tk.END, '*** ENTRY: {} of {} **** - - -(click here) - - - - - - - - - - -'.format(loc_itr, len(contacts_hold[pick])))
            self.ent_range_itr['{}'.format(loc_itr)] = [self.rlbox.get(tk.END)]
            for s,r in enumerate(i[3:-1]):
                
                if len(r) <= 1:                     #Skip lines with no content
                    pass
                
                else:
                    self.rlbox.insert(tk.END, '{}:'.format(cols[s+2]))        #, r.upper()))
                    self.ent_range_itr['{}'.format(loc_itr)].append(self.rlbox.get(tk.END))
                    self.rlbox.insert(tk.END, r.upper())
                    self.ent_range_itr['{}'.format(loc_itr)].append(self.rlbox.get(tk.END))
                    self.rlbox.itemconfig(tk.END, fg = 'dark goldenrod') #, fg = 'black')
                    
            self.rlbox.insert(tk.END, '-----------------------------------------------------')      #Spreader entry (readability)
            self.rlbox.insert(tk.END, ' ')  #Creating a blank to help ease readability by spreading out entries

        temp = self.rlbox.get(0,tk.END)
        
        for i,j in enumerate(temp):
            self.tracker[i] = j
            
        #print(self.tracker.items())


    #-----------------------------------------------
    def contact_selected(self, event):
        """
        Func - to test loading data related to selected conatact and or account
        """
        
        indx = event.widget.get(tk.ACTIVE)
        self.rlbox2.delete(0, tk.END)
        self.rlbox2.insert(tk.END, indx)

        temp = self.rlbox.get(tk.ACTIVE)        #Gets the active text for the clicked line

        self.ky = None                          #Establishing the global key variable to passed to other functions
        
        if temp == ' ':
            print('\nNothing Selected!\n')
                       
        else:                
            for k,v in self.ent_range_itr.items():                          #Iterate thru the dictionaries items
                print(k)
                if temp in v[1:-2:2]:                                       #Only look at key values which are every other in list
                    print('Keyword Selected\nPlease select orange item')
                    return
                
                else:
                    for g in v:
                        if g == temp:
                            self.ky = k                            #Unwanted action returns all matching keys (i.e. if multiple 'bills' all keys -
                            self.print_selected()                   # - thathave values with bill in it returned
                        else:   
                            pass
                        

    #------------------------------------------------
    def print_selected(self):
        """
        Func to take key that was associated with value and print out entire selection NOT just the active line,
        but all lines associated with what was clicked
        """
        
        try:
            holdr = self.ent_range_itr[self.ky]
            self.pop_up_details(*holdr)
            fline = holdr[0]
##            print(fline)
##            
##            kys = holdr[1:-2:2]
##            vals = holdr[2:-1:2]
##            for h in range(len(kys)):
##                print(kys[h])
##                print('------> {}'.format(vals[h]))
##
##            print('\n\n\n')
##            print(self.ent_range_itr[self.ky])
            
        except Exception as e:
            print(e)
        
##        try:
##            temp = indx.split(':')
##            print(temp[-1].lstrip())
##            self.pull_profile_page(temp[-1].lstrip())
##            
##        except Exception as e:
##            print(e)
                

    #-----------------------------------------------
    def pop_up_details(self, *args):
        """
        Func to
        
        IN:
            - selec: which selection was made on listbox
        RETURN:
            - a toplevel widget to display whatever
        """

        self.infowin = tk.Toplevel(bg = BG)
        self.lbutton = tk.Button(self.infowin, text = '<-', bg = BG, fg = FG,
                                    command = lambda: self.load_prev(self.ky))
        self.lbutton.grid(row = 1, column = 0, columnspan = 3,  padx = 5, pady = 5, sticky = tk.EW)
        
        self.infotxt = tk.Listbox(self.infowin, bg = BG, fg = FG, selectbackground = 'dark goldenrod', selectforeground = 'black',
                                 selectborderwidth = 2, height = 10, width = 80)
        self.infotxt.grid(row = 0, column = 1, columnspan = 4, padx = 5, pady = 5)

        self.infotxt.bind('<Double-Button-1>', self.copyselectedline())

        self.rbutton = tk.Button(self.infowin, text = '->', bg = BG, fg = FG,
                                    command = lambda: self.load_next(self.ky))
        self.rbutton.grid(row = 1, column = 3, columnspan = 3,  padx = 5, pady = 5, sticky = tk.EW)

        self.load_initial(args)
##        for i in args:
##            self.infotxt.insert(tk.END, '{}\n'.format(i))

        self.infowin.protocol('WM_DELETE_WINDOW', self.infowin.destroy)
        self.infowin.mainloop()
        
    #-
    def copyselectedline(self):
        
        self.infowin.clipboard_clear()
        self.infowin.clipboard_append(self.infotxt.get(tk.ACTIVE))
        return


    #-----------------------------------------------
    def load_initial(self, args):
        """
        Load listbox with initial selected key and values
        """

        temp = [j for j in [i for i in args]]   

        kys = temp[1:-2:2]
        vals = temp[2:-1:2]
        self.infotxt.insert(tk.END, '\n{}\n\n'.format(temp[0]))

        for i in range(len(kys)):
            self.infotxt.insert(tk.END, '{}\n'.format(kys[i]))
            self.infotxt.insert(tk.END, '     {}\n'.format(vals[i]))
            self.infotxt.itemconfig('end', fg = 'dark goldenrod')
        return



    #-----------------------------------------------
    def load_prev(self, k):
        """
        Take the current key and associated values and reduce by one and return k-1 and its values
        """
        
        self.infotxt.delete(0, tk.END)
        self.s = int(k)
        self.s -= 1
        self.ky = self.s
        
        if self.s < 1:
            self.infotxt.insert(tk.END, '\n     No more Entries,\n    Press --> Key')
            
        else:
            temp = self.ent_range_itr['{}'.format(self.s)]
            kys = temp[1:-2:2]
            vals = temp[2:-1:2]
            self.infotxt.insert(tk.END, '\n{}\n\n'.format(temp[0]))
            
            for i in range(len(kys)):
                self.infotxt.insert(tk.END, '{}\n'.format(kys[i]))
                self.infotxt.insert(tk.END, '     {}\n'.format(vals[i]))
                self.infotxt.itemconfig('end', fg = 'dark goldenrod')
            return
            
    #-----------------------------------------------
    def load_next(self, k):
        """
        Take the current key and associated values and increase by one and return k+1 and its values
        """
        
        self.infotxt.delete(0, tk.END)
        self.s = int(k)
        self.s += 1
        self.ky = self.s
        
        if self.s > len(self.ent_range_itr.keys()):
            self.infotxt.insert(tk.END, '\n     No more Entries,\n    Press <-- Key')
            
        else:
            temp = self.ent_range_itr['{}'.format(self.s)]
            kys = temp[1:-2:2]
            vals = temp[2:-1:2]
            self.infotxt.insert(tk.END, '\n{}\n\n'.format(temp[0]))
            
            for i in range(len(kys)):
                self.infotxt.insert(tk.END, '{}\n'.format(kys[i]))
                self.infotxt.insert(tk.END, '     {}\n'.format(vals[i]))
                self.infotxt.itemconfig('end', fg = 'dark goldenrod')
                
            return
        
        
    #-----------------------------------------------
    def pull_profile_page(self, searchterm):
        """
        Func to grab profile page for which account was highighted at time of selection.
        Try method used in-case user has non selected
        """
        
        pass


#Below is failed code to iterate through the lines and see if clicked item matches
#There are too many similar terms that would make searches return unfavorable results not matching
        
##        try:
##            s = self.lbox.get(tk.ACTIVE)            
##        except:
##            pass
##
##        itr = 0
##        while itr <= 5:            
##            for i in contacts_hold.values():
##                for s in (j for j in i):
##                    for k in s[:]:
##                        print(k)
##                    itr += 1

        


#--------------------------------------------------
"""Initializing the call to Google API for our spreadsheet,
then we create the GUI to manipulate data"""

if __name__ == '__main__':
    get_spreadsheet_data()
    root = tk.Tk()
    ContactsHub(root)
    root.mainloop()

        

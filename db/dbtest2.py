import tkinter as tk
import sqlite3 as sql3
import random as rand
import calendar as cal
import collections as clc
import json
import datetime as dt
import collections as clc

opts = """Ign:1 https://storage.googleapis.com/cros-packages/85 buster InRelease
Get:2 https://storage.googleapis.com/cros-packages/85 buster Release [3,119 B]
Get:3 https://storage.googleapis.com/cros-packages/85 buster Release.gpg [819 B]
Get:4 https://deb.debian.org/debian buster InRelease [121 kB]
Get:5 https://deb.debian.org/debian-security buster/updates InRelease [65.4 kB]
Get:6 https://storage.googleapis.com/cros-packages/85 buster/main amd64 Packages [16.1 kB]
Get:7 https://deb.debian.org/debian buster/main amd64 Packages [7,906 kB]
Get:8 https://deb.debian.org/debian buster/main Translation-en [5,968 kB]
Get:9 https://deb.debian.org/debian-security buster/updates/main amd64 Packages [234 kB]
Get:10 https://deb.debian.org/debian-security buster/updates/main Translation-en [126 kB]
Fetched 14.4 MB in 8s (1,775 kB/s)                                                                                                                                         
Reading package lists... Done
Building dependency tree       
Reading state information... Done
36 packages can be upgraded. Run 'apt list --upgradable' to see them.
N: Repository 'https://deb.debian.org/debian buster InRelease' changed its 'Version' value from '10.4' to '10.6'""".splitlines()

#---------------------------------------
class main:
    
    #--------------------------------------
    def __init__(self, parent):
        """ 
        calls all the functions in order necc. to build out GUI
        """
        
        self.parent = parent
        self.parent.title('Main DB')
        
        self.entriestracker = clc.OrderedDict()
        self.create_widgets()
        self.load_db()
        self.pull_db_info()
        self.populate_list()
        
        
    #WIDGET SECTION -------------------------------------------
    def create_widgets(self):
        """ 
        create the following wdgets ---- 
        - label
        - listbox   
        - scrollbar
        - filter entry
        - filter button
        - default button
        """
        
        self.create_label("Pick Date")
        self.create_lbox(40, 15)
        
        self.filtentry = tk.Entry(self.parent)
        self.filtentry.grid(sticky = tk.EW)
        self.fbutt = tk.Button(self.parent, text = 'Filter', command = lambda: None)
        self.fbutt.grid(sticky = tk.EW)
        self.defbutt = tk.Button(self.parent, text = 'Reset', command = lambda: None)
        self.defbutt.grid(sticky = tk.EW)
        
    #--------------------------------------
    def create_label(self, txt):
        """ 
        
        """
        
        self.lab = tk.Label(self.parent, text = txt)
        self.lab.grid()
        return
    
    #--------------------------------------
    def create_lbox(self, w, h):
        """ 
        
        """
        
        self.lbox = tk.Listbox(self.parent, width = w, height = h)
        self.lbox.grid()
        self.lbox.bind('<Button-1>', self.tooltipobj)#self.alterlabel)
        self.lbox.bind('<Double-Button-1>', self.newtoplevel)
        #lbox_ttp = CreateToolTip(self.lbox, "Testing")
        #self.lbox.bind("<Enter>", self.ttip_enter)
        #self.lbox.bind("<Leave>", self.ttip_close)
    
    
    def tooltipobj(self, event):
        txt = 'test'
        ktrack = tk.StringVar()
        k = CreateToolTip(self.lbox, txt)
        ktrack.trace('w', self.delkobj)
        
        
    def delkobj(self, *args):
        del(k)
        return
        
    #DATABASE SECTION -----------------------------------------
    def load_db(self):
        """
        columns -----
        - date
        - contact
        - note
        - rev?
        """
        
        self.con = sql3.connect(':memory:')
        return
    
    #--------------------------------------
    def fetch_db_ents(self, ents):
        """ 
        
        """
        
        for i in ents.fetchall():
            print(i)
    
    #--------------------------------------
    def select_db(self):
        """ 
        
        """
        
        pass
    
    #--------------------------------------
    def insert_db(self):
        """ 
        insert and update will work together.
        - first we must make a copy of the current note in db. 
        - then append to the end of the note
        - re-submit or update the value
        - ***Only when editing will we not need a copy
        """
        
        pass
    
    #--------------------------------------
    def update_db(self):
        """ 
        
        """
        
        pass
    
    #--------------------------------------
    def pull_db_info(self):
        """ 
        call to calendar function for given year to return datetime objects
        """
        self.dataents = self.pullcalldates()
        return
        
    #--------------------------------------
    def populate_list(self):
        """ 
        
        """
        for k,v in self.dataents.items():
            yr  = str(v).split('-')[0]
            if yr == '2020':
                randval = rand.choice(opts)
                self.lbox.insert(tk.END, f"{v} : Entries = None ")
                self.entriestracker[str(v)] = 0
            else:
                pass
    
    #--------------------------------------
    def pullcalldates(self):
        """ 
        grabs all the datetime dates from calendar module to be used as ref for 
        database writing of notes.
        """
        datelist = cal.Calendar()
        dlist = datelist.yeardatescalendar(2020)
        itr = 0
        self.d = {}
        for i in dlist[:]:
            for j in i:
                for k in j:
                    for u in k:
                        itr += 1
                        self.d[itr] = u
        return self.d
    
    #--------------------------------------
    def serializedata(self, entdate, dictobj):
        """ 
        entdate = the date which will have contents updated
        dictobj = dict object that will be passed to json.dumps to have a string object
        and loaded to the db file. 
        When we need to retrieve the string object will be sent thru json.loads to produce
        a DICTIONARY OBJECT AGAIN
        
        json example:
        k = {'2020-10-12':'Test Note 1', 'accnt 1':'note1', 'accnt 2':'note2'}
        y = json.dumps(k)  -- string object
        x = json.loads(y)  -- dict object
        """
        
        dict_length = len(dictobj.values())
        jsonobj = json.dumps(dictobj)
        self.con.execute("""UPDATE table SET notes = ?, qtyents = ? WHERE date = ?""",(jsonobj, dict_length,entdate))
        self.con.commit()
    
    
    #EVENT BINDING FUNCTIONS ----------------------------------------------------
    #--------------------------------------
    def alterlabel(self,event):
        """ 
        """
        
        curselect = event.widget.get(tk.ACTIVE).split(':')
        self.lab.config(text = f"Current Date: {curselect[0]}")
        return

    #--------------------------------------
    def newtoplevel(self, event):
        """
        """
        
        self.dbtop = tk.Toplevel()
        curselect = event.widget.get(tk.ACTIVE).split(':')
        self.toplab = tk.Label(self.dbtop, text = curselect[0])
        self.toplab.grid(row = 0, column = 0, columnspan = 2)
        self.txtbox = tk.Text(self.dbtop)
        self.txtbox.grid(row = 1, column = 0, columnspan = 2)
        self.repbutt = tk.Button(self.dbtop, text = 'Replace Entry', command = lambda: self.newentryparser(curselect[0]))
        self.repbutt.grid(row = 2, column = 0, sticky = tk.EW)
        self.addbutt = tk.Button(self.dbtop, text = 'Add Entry', command = lambda: self.addentry(curselect[0]))
        self.addbutt.grid(row = 2, column = 1, sticky = tk.EW)
        self.sepbutt = tk.Button(self.dbtop, text = 'Add Seperator', command = lambda: self.addseperator())
        self.sepbutt.grid(row = 3, column = 0, columnspan = 2, sticky = tk.EW)
        self.dbtop.mainloop()

    #--------------------------------------
    def addentry(self, d):
        """
        """
        pulledtext = self.txtbox.get(1.0, tk.END)
        self.dbtop.destroy()
        self.entriestracker[str(d)] = pulledtext
        self.refreshmainlist()

        
    #--------------------------------------
    def addseperator(self):
        """
        This is assuming going forward teh seperator between entries which will be split is ------
        The entire entry treated as a string and each entry is distinguishable by that dash -----
        """
        
        tod = dt.datetime.today()           #Add a timestamp to the entry
        seper = f"\n{tod}:\n-----"
        self.txtbox.insert(tk.END, seper)
        return


    #--------------------------------------
    def newentryparser(self, d):
        """
        pull the entire field of the text box as a string and parse it by a defined splitter (-----)
        after put each of the entries in a dict so that we can use json method to pass to db
        """
        
        jsdict = {}
        enttxt = self.txtbox.get(1.0, tk.END).split('-----')
        for n,i in enumerate(enttxt):
            jsdict[n] = i.strip('\n')
        
        self.entriestracker[str(d)] = len(jsdict.values())       #Keeping track of entry totals for each date to display on the main listbox
        for k,v in self.entriestracker.items():
            print(k,v)
            
        print(f'Total Entries : {len(jsdict.values())}')
        print(jsdict.items())
        go = json.dumps(jsdict)
        pull = json.loads(go)
        print(go)
        print(pull)

    #--------------------------------------
    def refreshmainlist(self):
        """
        """
        self.lbox.delete(0,tk.END)
        for k,v in sorted(self.entriestracker.items()):
            if v != 0:
                self.lbox.insert(tk.END, f"{k} : {v}")
                self.lbox.itemconfig(tk.END, fg = 'red')
            else:
                self.lbox.insert(tk.END, f"{k} : {v}")
        return
    
    #TOOL TIP FUNCTIONALITY
    #------------------------------------------------------
    def ttip_enter(self, event=None):
        x = y = 0
        x, y, cx, cy = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 20
        
        # creates a toplevel window
        self.tw = tk.Toplevel(event.widget)
        
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left', foreground = 'white',
                       background='navy blue', relief='solid', borderwidth=1,
                       font=("times", "12", "normal"))
        label.pack(ipadx=1)
        
    #------------------------------------------------------
    def ttip_close(self, event=None):
        if self.tw:
            self.tw.destroy()







class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.near = self.widget.nearest(self.widget.winfo_pointery())
        self.text = self.widget.get(tk.ACTIVE)   #f'@{self.widget.winfo_pointerx()},{self.widget.winfo_pointery()}')#,(self.widget.winfo_pointerx(), self.widget.winfo_pointery()))
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        
    #------------------------------------------------------
    def enter(self, event=None):
        """
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
        abs_coord_y = root.winfo_pointery() - root.winfo_rooty()
        """
        x = y = 0
        x, y, cx, cy = self.widget.bbox(tk.ACTIVE)
        x += (self.widget.winfo_pointerx())  # - self.widget.winfo_rootx()) #+ 25
        y += (self.widget.winfo_pointery())  # - self.widget.winfo_rooty()) #+ 20
        
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        self.label = tk.Label(self.tw, text=self.widget.get(tk.ACTIVE), justify='left', foreground = 'black',
                       relief='solid', borderwidth=1,
                       font=("times", "12", "normal"))
        self.label.pack(ipadx=1)
        #In the 1st class you can add in line 38:
        self.label.after(1000, self.altercolor)
        #self.label.after(2000, self.close)
        #to disappear the label after 1 sec
    
    #------------------------------------------------------
    def close(self, event=None):
        try:
            if self.tw:
                self.tw.destroy()
        except AttributeError as e:
            print(e)
    
    def changedialog(self, txt):
        self.label.config(text = txt)
    
    def altercolor(self, event = None):
        self.label.config(background = 'red')
        self.label.after(2000, self.close)
        #self.label.after(2000, self.changedialog('Hurry Up'))

#MAIN----------------------------
#--------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.mainloop()

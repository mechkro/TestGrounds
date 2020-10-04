import tkinter as tk
import sqlite3 as sql3
import random as rand
import calendar as cal
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

class main:
    
    #--------------------------------------
    def __init__(self, parent):
        """ 
        
        """
        
        self.parent = parent
        self.parent.title('Main DB')
        
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
        self.filtentry.grid()
        self.fbutt = tk.Button(self.parent, text = 'Filter', command = lambda: None)
        self.fbutt.grid()
        self.defbutt = tk.Button(self.parent, text = 'Reset', command = lambda: None)
        self.defbutt.grid()
        
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
        
        """
        self.dataents = self.pullcalldates()
        
    #--------------------------------------
    def populate_list(self):
        """ 
        
        """
        
        for i in range(365):
            randval = rand.choice(opts)
            self.lbox.insert(tk.END, f"{i} - {randval}")
    
    #--------------------------------------
    def pullcalldates(self):
        """ 
        
        """
        datelist = cal.Calendar()
        dlist = datelist.yeardatescalendar()
        itr = 0
        self.d = {}
        for i in y[:]:
            for j in i:
                for k in j:
                    for u in k:
                        itr += 1
                        self.d[itr] = u
        return self.d
        

#MAIN----------------------------
#--------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    main(root)
    root.mainloop()
        
    
        

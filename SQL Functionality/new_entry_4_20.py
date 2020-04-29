import tkinter as tk
import sqlite3
import datetime as dt
import calendar as cal
from tkcalendar import Calendar, DateEntry


BG = 'white'
FG = 'midnight blue'
DGR = 'dark goldenrod'


class Main(object):
    
    #----------------------------------------
    def __init__(self, parent):
        """ 
        
        """
        
        self.parent = parent
        self.parent.config(bg = BG)
        self.parent.title('Testing Grounds')
        
        self.frm = tk.Frame(self.parent, bg = BG)
        self.frm.grid(sticky = tk.NSEW)

        self.ents_count = tk.Label(self.frm, text = 'No Entries Loaded', font = 'verdana 12 bold', bg = BG, fg = DGR)
        self.ents_count.grid(row = 0, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        #Scroolbar and Text Widget -------------------------------------------------------
        self.sbar = tk.Scrollbar(self.frm, orient = tk.VERTICAL, bg = BG)
        self.sbar.grid(row = 1, column = 1, sticky = tk.NS)
        self.txt = tk.Text(self.frm, yscrollcommand = self.sbar.set, bg = BG, fg = FG)
        self.txt.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.NS)
        self.sbar.config(command = self.txt.yview)
        
        #Button and Label --------------------------------------------
        self.butt_initiate = tk.Button(self.frm, text = 'Initiate DB', font = 'verdana 14 bold', bg = BG, fg = FG, command = lambda: self.init_db_func())
        self.butt_initiate.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)

        self.filterlab = tk.Label(self.frm, text = 'Filter by?', bg = BG, fg = FG, font = 'verdana 12 bold')
        self.filterlab.grid(row = 3, columnspan = 2, padx = 5, pady = 5)

        #Spinbox and StringVar -------------------------------------------
        self.sboxvar = tk.StringVar()
        
        self.sbox = tk.Spinbox(self.frm, values = ['Month', 'Day', 'Company'], bg = BG, fg = FG,
                               textvariable = self.sboxvar, font = 'verdana 12 bold')
        self.sbox.grid(row = 4, columnspan = 2, padx = 5, pady = 10)
        
        self.sboxvar.trace('w', self.print_spinbox)
        
    
    #-------------------------------------------
    def print_spinbox(self, *args):
        """ 
        TEMPERARY***
        Future - Will be used to notify the application a change has been made to the spinbox variable
        """
        
        print(self.sbox.get())
        
        
    #-----------------------------------------    
    def init_db_func(self):
        """ 
        
        """
        
        self.establish_db_connection()
        self.create_db_table()
        self.execute_date_mapping()
        self.init_all_notes()
        #self.insert_map_into_db()
        self.enter_into_date_new()
        
        
        
    #-----------------------------------------
    def establish_db_connection(self):
        """ 
        For now is having database run and source from memory instead of future .db
        """       
        
        floc = r'C:\Users\kinse\Desktop\DXP_app\Databases\year2020.db'
        self.condb = sqlite3.connect(floc)
    
        self.butt_initiate.config(text = 'Add new Note', command = lambda: self.enter_into_date_new())
    
    #------------------------------------------
    def create_db_table(self):
        """ 
        Create table for the database to referemce. 
        Vars: id, date, note, tstamp
        
        tstamp - timestamp of the last event for any given entry or change
        """
        
        self.condb.execute("""CREATE TABLE IF NOT EXISTS caldates (id INTEGER PRIMARY KEY,
                                                                                            date TEXT,
                                                                                            note TEXT,
                                                                                            tstamp TEXT);""")
        self.condb.commit()
        
    #-----------------------------------------
    def execute_date_mapping(self):
        """
        Func will gather all the possible dates for a given year and match them to a dictionary with
        keys being integers corresponding to primary key of database
        
        Ex. 
        dates = ('01-01-2020', '01-02-2020', .... '12-31-2020')
        dates_map = { 0: dates[0], 1:dates[1]....... n:dates[n]}
        """
        
        c = cal.Calendar()
        dates = c.yeardatescalendar(2020, width = 1)
        self.dates_map = {} 
        iter_dates = 0
        
        for a in dates:
            for b in a:
                for c in b:
                    for d in c:
                        y = dt.datetime.strftime(d, '%Y, %m, %d')
                        if y.split(',')[0] != '2020':
                            pass
                        else:
                            self.dates_map[y] = iter_dates
                            iter_dates += 1
        


    #------------------------------------------------------
    def insert_map_into_db(self):
        """ 
        
        """
        
        cur = self.condb.cursor()
        
        for k, v in self.dates_map.items():
            t = dt.datetime.now()
            cur.execute("""INSERT INTO caldates (id, date, tstamp) VALUES (?, ?, ?)""",(v,k, t))
        self.condb.commit()
        cur.close()
        print('succesful insert and close of db')



    #---------------------------------------------
    def enter_into_date_new(self):
        """
        Function serves to gather date input from user and insert into the approapriate
        DB id based on the date
        """
           
        self.tlevel = tk.Toplevel(bg = BG)
        
        self.cal_labelframe =tk.LabelFrame(self.tlevel, text = 'Calendar', bg = BG, fg = FG, font = 'Verdana 12 bold')
        self.cal_labelframe.grid(row = 0, padx = 10, pady = 10, sticky = tk.NSEW)
        
        tdy = dt.datetime.today()
        tdy_str = tdy.strftime('%Y %m %D').split()
        y = tdy_str[0]
        m = tdy_str[1]
        d = (tdy_str[-1].split("/"))[1]
        
        today = dt.date.today()
        mindate = dt.date(year=(int(y)-1), month=int(m), day=int(d))
        maxdate = today + dt.timedelta(days=365)
        
        self.cal = Calendar(self.cal_labelframe, font="Arial 14", selectmode='day', locale='en_US',
                            background = BG, foreground = FG, headersbackground = BG, headersforeground = DGR,
                            bordercolor = DGR,normalbackground = BG, normalforeground = FG, 
                            weekendbackground = BG, weekendforeground = FG,
                            selectbackground = DGR, selectforeground = 'black',
                            othermonthforeground = 'dim gray', othermonthbackground = BG, 
                            othermonthweforeground = 'dim gray', othermonthwebackground = BG, 
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            tooltipbackground = BG, tooltipforeground = DGR,
                            cursor="hand1", year=int(y), month=int(m), day=int(d))
        
        self.cal.grid(row = 0, column =0, columnspan = 2, padx = 10, pady = 10., sticky = tk.NSEW)
        self.cal.bind('<<CalendarMonthChanged>>', self.on_change_month)
        self.cal.bind('<<CalendarSelected>>', self.on_change_day)


        self.tlevel2 =tk.LabelFrame(self.tlevel, text = 'Widgets', bg = BG, fg = FG, font = 'Verdana 12 bold')
        self.tlevel2.grid(row = 1, padx = 10, pady = 10, sticky = tk.NSEW)        

        #LAbel Widgets --------------------------------------
        self.l1 = tk.Label(self.tlevel2, text = 'What year?', bg = BG, fg = FG)
        self.l1.grid(row = 0, column = 0, padx = 3, pady = 3)
        
        self.l2 = tk.Label(self.tlevel2, text = 'What Month?', bg = BG, fg = FG)
        self.l2.grid(row = 1, column = 0, padx = 3, pady = 3)
        
        self.l3 = tk.Label(self.tlevel2, text = 'What Day?', bg = BG, fg = FG)
        self.l3.grid(row = 2, column = 0, padx = 3, pady = 3)       

        #Entry Widgets ------------------------------
        self.e1 = tk.Entry(self.tlevel2, bg = BG, fg = FG, font = ('verdana 12 bold'), justify = tk.CENTER)
        self.e1.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = tk.EW)
        
        self.e2 = tk.Entry(self.tlevel2, bg = BG, fg = FG, font = ('verdana 12 bold'), justify = tk.CENTER)
        self.e2.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = tk.EW)
        
        self.e3 = tk.Entry(self.tlevel2, bg = BG, fg = FG, font = ('verdana 12 bold'), justify = tk.CENTER)
        self.e3.grid(row = 2, column = 1, padx = 3, pady = 3, sticky = tk.EW)

        #Bindings ---------------------------------------
        self.e1.bind('<Enter>', self.alter_clr_e1)
        self.e1.bind('<Leave>', self.default_clr_e1)
         

        self.e2.bind('<Enter>', self.alter_clr_e2)
        self.e2.bind('<Leave>', self.default_clr_e2)

        self.e3.bind('<Enter>', self.alter_clr_e3)
        self.e3.bind('<Leave>', self.default_clr_e3)
        
        #Button Widget -----------------------------------
        self.b1 = tk.Button(self.tlevel2, text = 'Confirm' ,bg = BG, fg = FG, command = lambda: self.check_add_note())
        self.b1.grid(row = 3, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        self.tlevel.mainloop()



    #EVENTS --------------------------------------------------------------
    def on_change_month(self, event):
        """ 
        When the month is changed from Calander widget 
        """
        pass
    
    
    def on_change_day(self, event):
        """ 
        When the month is changed from Calander widget 
        """
        e = event.widget.selection_get()
        e_split = str(e).split('-')
        #e_ss = e_split.split('-')
        e_year = e_split[0]
        e_mnth = e_split[1]
        e_day = e_split[-1]
        print(e)
        
        for i in (self.e1, self.e2, self.e3):
            i.delete(0, tk.END)
            
        self.e1.insert(0, str(e_year))
        self.e1.update
        
        self.e2.insert(0, str(e_mnth))
        self.e2.update
        
        self.e3.insert(0, str(e_day))
        self.e3.update        
                       
    
    #Color changing-----------------------------------
    """Assist in helpiing user identify widget cursor is over """
    def alter_clr_e1(self, event):
        """ """
        self.l1.config(fg = DGR)
        
    #--------------------------------------------
    def default_clr_e1(self, event):
        """ """
        self.l1.config(fg = FG)
        
    #-------------------------------------------------------
    def alter_clr_e2(self, event):
        """ """
        self.l2.config(fg = DGR)
        
    #-----------------------------------------------
    def default_clr_e2(self, event):
        """ """
        self.l2.config(fg = FG)
    
    #-------------------------------------------
    def alter_clr_e3(self, event):
        """ """
        self.l3.config(fg = DGR)

    #----------------------------------------------
    def default_clr_e3(self, event):
        """ """
        self.l3.config(fg = FG)
        
    #---------------------------------------------
    def check_add_note(self):
        """
        
        """
        
        x,y,z = self.e1.get(), self.e2.get(), self.e3.get()
        
        if int(y) in range(0,10):
            y = '{}'.format(y)
        else:
            pass

        if int(z) in range(0,10):
            z = '{}'.format(z)
        else:
            pass        
        
        formatted_date = "{}, {}, {}".format(x,y,z)
       
        for itms in self.tlevel.winfo_children():
            itms.destroy()
            
        self.note_lab = tk.Label(self.tlevel, text = 'Add Note', bg = BG, fg = FG)
        self.note_lab.grid(row = 0, padx = 3, pady = 3)
        
        self.noteadd = tk.Text(self.tlevel, bg = BG, fg = FG)
        self.noteadd.grid(row = 1, padx = 5, pady = 5)
        
        self.noteadd.tag_config('EntryTitle', foreground = 'white', background = 'navy blue')
        self.noteadd.insert(1.0, 'Entry - {} ------:\n\n'.format(formatted_date), 'EntryTitle')
        
        self.butt_add = tk.Button(self.tlevel, text = 'Add Note', command = lambda: self.add_new_note(formatted_date), bg = BG, fg = FG)
        self.butt_add.grid(row = 2, padx = 5, pady = 5)



    #---------------------------------------------
    def add_new_note(self, ftxt):
        """
        
        """
        
        addtxt = self.noteadd.get(1.0, tk.END)
        cur = self.condb.cursor()
        cur.execute("""UPDATE caldates SET note=? WHERE id=?""", (addtxt, self.dates_map[ftxt]))
        self.condb.commit()
        cur.close()
        self.tlevel.destroy()
        self.print_to_main()


    #--------------------------------------------
    def print_to_main(self):
        """ 
        
        """
        
        self.txt.delete(1.0, tk.END)      #Reset the text widget contents - so that new old notes are not re-pasted  
        cur = self.condb.cursor()
        cur.execute("""SELECT * FROM caldates WHERE note != 'None'""")
        ents = cur.fetchall()
        numb_ents = len(ents)
        self.ents_count.config(text = 'Total Entries: {}'.format(numb_ents))
        for j in ents:
            notetoadd = """##########\nID: {}\nDate: {}\nNote: {}\nLast Change: {}\n##########\n\n""".format(j[0],j[1],j[2],j[3])
            self.txt.insert(tk.END,notetoadd)
        
        return
               
    
    
    #-----------------------------------------------
    def init_all_notes(self):
        """
        Currently serving as a testing output function.
        FUTURE - alter to print whatever entry was entered
        """
        
        cur = self.condb.cursor()
        cur.execute("""SELECT * FROM caldates""")
        ents = cur.fetchall()
        for j in ents:
            notetoadd = """##########\nID: {}\nDate: {}\nNote: {}\nLast Change: {}\n##########\n\n""".format(j[0],j[1],j[2],j[3])
            self.txt.insert(1.0, notetoadd)
        
            
            
            
            
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
    

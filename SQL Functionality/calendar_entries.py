import tkinter as tk
import sqlite3
import datetime as dt
import calendar as cal


class Main(object):
    
    #----------------------------------------
    def __init__(self, parent):
        """ 
        
        """
        
        self.parent = parent
        
        self.frm = tk.Frame(self.parent)
        self.frm.grid(sticky = tk.NSEW)

        self.ents_count = tk.Label(self.frm, text = 'No Entries Loaded', font = 'verdana 12 bold')
        self.ents_count.grid(row = 0, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        self.sbar = tk.Scrollbar(self.frm, orient = tk.VERTICAL)
        self.sbar.grid(row = 1, column = 1, sticky = tk.NS)
        self.txt = tk.Text(self.frm, yscrollcommand = self.sbar.set)
        self.txt.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.NS)
        self.sbar.config(command = self.txt.yview)
        
        self.butt_initiate = tk.Button(self.frm, text = 'Initiate DB', font = 'verdana 14 bold', command = lambda: self.init_db_func())
        self.butt_initiate.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)

        self.filterlab = tk.Label(self.frm, text = 'Filter by?')
        self.filterlab.grid(row = 3, columnspan = 2, padx = 5, pady = 5)

        self.sboxvar = tk.StringVar()
        self.sbox = tk.Spinbox(self.frm, values = ['Month', 'Day', 'Company'])
        self.sbox.grid(row = 4, columnspan = 2, padx = 5, pady = 5)
        self.sboxvar.trace('w', None)

        self.editlab = tk.Label(self.frm, text = 'Edit Entry ID:')
        self.editlab.grid(row = 5, columnspan = 2, padx = 3, pady = 3)
        
        self.editent = tk.Entry(self.frm)
        self.editent.grid(row = 6, columnspan = 2, padx = 3, pady = 3)

        self.butt_edit = tk.Button(self.frm, text = 'Edit', command = lambda: self.edit_entry())
        self.butt_edit.grid(row = 7, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        
    #-----------------------------------------    
    def init_db_func(self):
        """ 
        
        """
        
        self.establish_db_connection()
        self.create_db_table()
        self.execute_date_mapping()
        self.insert_map_into_db()
        self.enter_into_date_new()
        
        
        
    #-----------------------------------------
    def establish_db_connection(self):
        """ 
        For now is having database run and source from memory instead of future .db
        """       
        
        floc = ':memory:'
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
           
        self.tlevel = tk.Toplevel()

        #LAbel Widgets --------------------------------------
        self.l1 = tk.Label(self.tlevel, text = 'What year?')
        self.l1.grid(row = 0, column = 0, padx = 3, pady = 3)
        
        self.l2 = tk.Label(self.tlevel, text = 'What Month?')
        self.l2.grid(row = 1, column = 0, padx = 3, pady = 3)
        
        self.l3 = tk.Label(self.tlevel, text = 'What Day?')
        self.l3.grid(row = 2, column = 0, padx = 3, pady = 3)       

        #Entry Widgets ------------------------------
        self.e1 = tk.Entry(self.tlevel)
        self.e1.grid(row = 0, column = 1, padx = 3, pady = 3)
        
        self.e2 = tk.Entry(self.tlevel)
        self.e2.grid(row = 1, column = 1, padx = 3, pady = 3)
        
        self.e3 = tk.Entry(self.tlevel)
        self.e3.grid(row = 2, column = 1, padx = 3, pady = 3)

        #Bindings ---------------------------------------
        self.e1.bind('<Enter>', self.alter_clr_e1)
        self.e1.bind('<Leave>', self.default_clr_e1)

        self.e2.bind('<Enter>', self.alter_clr_e2)
        self.e2.bind('<Leave>', self.default_clr_e2)

        self.e3.bind('<Enter>', self.alter_clr_e3)
        self.e3.bind('<Leave>', self.default_clr_e3)
        
        #Button Widget -----------------------------------
        self.b1 = tk.Button(self.tlevel, text = 'Submit', command = lambda: self.check_add_note())
        self.b1.grid(row = 3, columnspan = 2, padx = 5, pady = 5)
        
        self.tlevel.mainloop()

    def alter_clr_e1(self, event):
        """ """
        self.l1.config(fg = 'dark goldenrod')

    def default_clr_e1(self, event):
        """ """
        self.l1.config(fg = 'black')

    def alter_clr_e2(self, event):
        """ """
        self.l2.config(fg = 'dark goldenrod')

    def default_clr_e2(self, event):
        """ """
        self.l2.config(fg = 'black')

    def alter_clr_e3(self, event):
        """ """
        self.l3.config(fg = 'dark goldenrod')

    def default_clr_e3(self, event):
        """ """
        self.l3.config(fg = 'black')
    #---------------------------------------------
    def check_add_note(self):
        """
        
        """
        
        x,y,z = self.e1.get(), self.e2.get(), self.e3.get()
        
        if int(y) in range(0,10):
            y = '0{}'.format(y)
        else:
            pass

        if int(z) in range(0,10):
            z = '0{}'.format(z)
        else:
            pass        
        
        formatted_date = "{}, {}, {}".format(x,y,z)
       
        for itms in self.tlevel.winfo_children():
            itms.destroy()
            
        self.note_lab = tk.Label(self.tlevel, text = 'Add Note')
        self.note_lab.grid(row = 0, padx = 3, pady = 3)
        
        self.noteadd = tk.Text(self.tlevel)
        self.noteadd.grid(row = 1, padx = 5, pady = 5)
        
        self.butt_add = tk.Button(self.tlevel, text = 'Add Note', command = lambda: self.add_new_note(formatted_date))
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
    def print_all_notes(self):
        """
        Currently serving as a testing output function.
        FUTURE - alter to print whatever entry was entered
        """
        
        cur = self.condb.cursor()
        cur.execute("""SELECT * FROM caldates""")
        ents = cur.fetchall()
        for j in ents:
            print(j)


    #-----------------------------------------------
    def edit_entry(self):
        """
        Takes user inputed entry of the ID number to coresponding date
        and allows user to edit it.
        """
        entid = self.editent.get()
        cur = self.condb.cursor()
        cur.execute("""SELECT * FROM caldates WHERE id = ?""", (entid,))

        self.editlevel = tk.Toplevel()
        self.txtedit = tk.Text(self.editlevel)
        self.txtedit.grid()
        for j in cur.fetchone():
            self.txtedit.insert(tk.END, '{}\n'.format(j))
        self.editlevel.mainloop()
            
            
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
    

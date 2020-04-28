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
        
        self.sbar = tk.Scrollbar(self.frm, orient = tk.VERTICAL)
        self.sbar.grid(row = 0, column = 1, sticky = tk.NS)
        self.txt = tk.Text(self.frm, yscrollcommand = self.sbar.set)
        self.txt.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.NSEW)
        self.sbar.config(command = self.txt.yview)
        
        self.butt_initiate = tk.Button(self.frm, text = 'Initiate DB', font = 'verdana 14 bold', command = lambda: self.init_db_func())
        self.butt_initiate.grid(row = 1, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        
        
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
        
        self.l1 = tk.Label(self.tlevel, text = 'What year?')
        self.l1.grid(row = 0, column = 0, padx = 3, pady = 3)
        
        self.l2 = tk.Label(self.tlevel, text = 'What Month?')
        self.l2.grid(row = 1, column = 0, padx = 3, pady = 3)
        
        self.l3 = tk.Label(self.tlevel, text = 'What Day?')
        self.l3.grid(row = 2, column = 0, padx = 3, pady = 3)       
       
        self.e1 = tk.Entry(self.tlevel)
        self.e1.grid(row = 0, column = 1, padx = 3, pady = 3)
        
        self.e2 = tk.Entry(self.tlevel)
        self.e2.grid(row = 1, column = 1, padx = 3, pady = 3)
        
        self.e3 = tk.Entry(self.tlevel)
        self.e3.grid(row = 2, column = 1, padx = 3, pady = 3)        
        
        self.b1 = tk.Button(self.tlevel, text = 'Submit', command = lambda: self.check_add_note())
        self.b1.grid(row = 3, columnspan = 2, padx = 5, pady = 5)
        
        self.tlevel.mainloop()
        
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
            
            
            
            
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
    

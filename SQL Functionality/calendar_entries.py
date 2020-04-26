import tkinter as tk
import sqlite3
import datetime as dt
import calendar as cal


class Main:
    
    #----------------------------------------
    def __init__(self, parent):
        """ """
        self.parent = parent
        self.establish_db_connection()
        self.create_db_table()
        self.execute_date_mapping()
        self.insert_map_into_db()
        self.print_all_db()
        self.enter_into_date_new()
        
        
        
    #-----------------------------------------
    def establish_db_connection(self):
        """ """
        floc = ':memory:'
        self.condb = sqlite3.connect(floc)
    
    
    #------------------------------------------
    def create_db_table(self):
        """ """
        self.condb.execute("""CREATE TABLE IF NOT EXISTS caldates (id INTEGER PRIMARY KEY,
                                                                                            date TEXT,
                                                                                            note TEXT);""")
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
                            self.dates_map[iter_dates] = y
                            iter_dates += 1
        
        #for k,v in self.dates_map.items():
        #    print(k, v)


    #------------------------------------------------------
    def insert_map_into_db(self):
        """ """
        
        cur = self.condb.cursor()
        for k, v in self.dates_map.items():
            cur.execute("""INSERT INTO caldates (id, date) VALUES (?, ?)""",(k,v))
        self.condb.commit()
        cur.close()
        print('succesful insert and close of db')


    #----------------------------------------------
    def print_all_db(self):
        """ """
        
        cur = self.condb.cursor()
        cur.execute("""SELECT * FROM caldates""")
        ents = cur.fetchall()
        print('The following dates are associated with these keys:\n\n')
        for al in ents:
            als = al[1].split(',')
            print('Id #: {}\nDate Associated:\n  Year:{}\n  Month:{}\n  Day:{}\n\n'.format(al[0], als[0], als[1], als[-1]))
        return


    def enter_into_date_new(self):
        """ """
        year_in = input("What year? : ")
        month_in = input("What Month? : ")
        day_in = input("What Day? : ")
        x = "{}, {}, {}".format(year_in, month_in, day_in)
        note_in = input("Note: ")

        fromdatesmap = [k for k,v in self.dates_map.items() if v == x]
        self.condb.execute("""INSERT INTO caldates (id, date, note) VALUES (?,?,?)""",(fromdatesmap[0], self.dates_map[fromdatesmap[0]], note_in))
        self.condb.commit()

        print('succesful implement')
        return
    
        
            
            
            

Main('test')
    
    

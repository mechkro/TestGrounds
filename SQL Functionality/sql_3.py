import sqlite3 as sql
import random
import datetime
import collections as clc
import tkinter as tk

#SAUCE - https://www.python-course.eu/sql_python.php
"""
ex 1:
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

# delete 
#cursor.execute('''DROP TABLE employee;''')

sql_command = '''
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);'''

cursor.execute(sql_command)

sql_command = '''INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");'''
cursor.execute(sql_command)


sql_command = '''INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");'''
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()


Ex 2:
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
               ("Frank", "Schiller", "m", "1955-08-17"),
               ("Jane", "Wall", "f", "1989-03-14") ]
               
for p in staff_data:
    format_str = '''INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");'''

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate = p[3])
    cursor.execute(sql_command)
"""



customer = ['AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
            'Arizona_Mining_Company', 'Arizona_Pacific_Wood', 'Asarco_Mission', 'Avondale', 'BE_Aerospace', 'Biosphere', 'Black_&_Veatch', 'Botanicare', 'Brown_and_Caldwell',
            'Bull_Moose', 'Bullhead_City', 'CCA', 'Camp_Dresser_McGhee', 'Carefree', 'Casa_Grande', 'Casa_Grande_Area', 'Cave_Creek', 'Chandler', 'Chino_Valley_',
            'City_of_Casa_Grande_WWTP', 'City_of_Henderson', 'City_of_Las_Vegas', 'Clark_County_Water_Reclamation_District', 'Clarkdale_Metals', 'Coolidge_Land_Acquition_Wes_Emulsions',
            'Cottonwood', 'Daisy_Sour_Cream', 'Davis_Monthan_AFB', 'Drake_Materials_Paulden', 'Ehrmanns_Dairy', 'Envirogen', 'Environmental_Biomass', 'Epcor_Bullhead_City',
            'Euclid_Chemical', 'FMI_Ajo', 'FMI_Bagdad', 'FMI_Bisbee', 'FMI_Sieritta', 'Fann_Environmental', 'Florence', 'Fluid_Solutions', 'Fountain_Hills', 'Franklin_Foods_Cream_Cheese',
            'Frito_Lay', 'Ft_Huachuca', 'Ft_Mohave', 'GCW', 'Glendale', 'Goodyear', 'Greeley_and_Hansen', 'Green_Valley_Pecans', 'Griffith_Energy_New_Star_Energy', 'Henderson_Electric',
            'Hexcel', 'Honeywell', 'Hydro_Geo_Chem', 'IBM', 'IDG', 'JDS_Engineering', 'Jones_Lang_LaSalle', 'Kinder_Morgan', 'Kingman', 'Kingman_all_Accounts', 'LPC_Contstruction',
            'Las_Vegas_Valley_Water_District', 'Laughlin', 'Lhoist_North_America', 'MGC', 'Mesa_NOT_Riverview', 'Mingus_Associates_Construction', 'Mohave_Valley', 'Morrison_Maierle',
            'Needles', 'Neltec', 'Nexus_Energy_calpine', 'Nord_Copper', 'Nucor', 'Oceanspray', 'Olin_Chlor', 'Paragon', 'Peoria', 'Phoenix_', 'Pima_County_WW', 'Poggemeyer_Engineers',
            'Praxair_Electronics', 'Prescott', 'Pro_Petroleum', 'Queen_Creek', 'Rain_Bird', 'Raytheon_Hagemeyer', 'Renewable_Algal_Energy', 'Sasol_Inc', 'Scottsdale', 'Severn_Trent_Environmental_Services',
            'Sierra_Vista_Regional_Health_Center', 'Slater_Hannifan_Group', 'Sletten', 'Southern_Nevada_Water_Authority', 'Sun_Mechanical', 'Sundt_', 'Surprise', 'Swissport_Fueling_',
            'TEP_Irvington', 'Timet_HOLD_OFF', 'Tolin_Mechanical', 'Tolleson', 'Topock', 'Trans_Canada_Power_Plant_Coolidge', 'United_Metals', 'Wilson_Engineers']

firstnames = ['Tony', 'John', 'Jim', 'Ken', 'Mary', 'Ashley', 'Gavin', 'Rich', 'Wesley', 'Sean', 'Shelly', 'Candi']
lastnames = ['smith', 'rogers', 'kinsey', 'jones', 'focker', 'white', 'johnson', 'harris', 'burnes', 'harrington', 'li', 'wang']
notes = ['Called and left VM', 'NTOd the quote', 'Waiting on calling him back', 'Quoted', 'Follow up needed', "meeting scheduled",
         "Plan lunch and learn", "Urgent!!!!", "Call and get clarification", "WON"]


def connect_db():
    """ """
    
    connection = sql.connect(':memory:')
    return connection    


class SQLBot:
    
    
    #----------------------------------------------------------
    def __init__(self, parent, table, *args):
        """ """
        self.parent = parent

        self.l = tk.Label(self.parent, text = 'Enter new ID\n assignment')
        self.l.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.ent = tk.Entry(self.parent)
        self.ent.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        self.lbox = tk.Listbox(self.parent, width = 45, height = 10)
        self.lbox.grid(row = 1, columnspan = 2, padx = 5, pady = 5)

        self.b = tk.Button(self.parent, text = 'start',command = lambda: self.start_db(table))
        self.b.grid(row = 2, columnspan =2, padx = 5, pady = 10)

        self.lsort = tk.Label(self.parent, text = 'Sort by? :')
        self.lsort.grid(row = 3, column = 0, padx = 5, pady = 5)

        self.val = tk.StringVar()
        self.sbox = tk.Spinbox(self.parent, values = ('ID', 'Date', 'Company'), state = 'disabled',
                               textvariable = self.val)
        self.sbox.grid(row = 3, column = 1, padx = 5, pady = 5)
        #self.val.set(self.sbox.get(tk.ACTIVE))
        self.val.trace('w', None)
    
    def start_db(self, t):
        """ """
        
        self.table = t
        self.c = connect_db()
        self.create_table()
        self.add_to_table()
        x = self.print_table()
        self.print_select(x)

        self.ask_if_id_taken()
     
        
    #----------------------------------------------------------
    def create_table(self):
        """
        ToDo - Tag Classifications - tablename (status CHAR(1)) - ex: Can be 'U' for Urgent

        """
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, date TEXT, customer TEXT, note TEXT)""")
        self.c.commit()
        self.c.execute("""CREATE TABLE IF NOT EXISTS datetrig (id INTEGER, note TEXT, days INTEGER)""")
        self.c.commit()
        return
    
    
    #----------------------------------------------------------
    def add_to_table(self):
        """ """
        
        for n, i in enumerate(range(100)):
            r_customer = random.choice(customer)
            fname = random.choice(firstnames)
            lname = random.choice(lastnames)
            r_note = random.choice(notes)
            combo = '{},{} - {}'.format(fname, lname, r_note)
            p = [1,2,3,4,5,6,7,8,20,25,15]
            dt = datetime.date.today()-datetime.timedelta(weeks=random.choice(p))
            self.c.execute("""INSERT INTO test VALUES (NULL,?,?,?)""",(str(dt), r_customer, combo))
            self.c.commit()
        return
    
    
    #----------------------------------------------------------
    def print_table(self):
        """ """
        
        temp = None
        ents = self.c.execute("""SELECT * FROM test""")
        for n,i in enumerate(sorted(ents.fetchall())):
            if n == 0:
                temp = i[2]
            else:
                pass
            self.lbox.insert(tk.END, i)
            if n %2 == 0:
                self.lbox.itemconfig(tk.END, bg = 'black', fg = 'white')
            else:
                pass
            
            print(i)
        self.lbox.update()
        self.sbox.config(state = 'normal')
        return temp
    
    
    #----------------------------------------------------------
    def print_select(self, searchterm):
        """ """
        
        itr = 0
        ents = self.c.execute("""SELECT * FROM test WHERE customer = ?""",(searchterm,))
        for i in ents:
            itr += 1
            print(i)
        print('There were {} total entries that matched "{}"'.format(itr, searchterm))
        print('Which is {} % of the total polled'.format((itr/1000.0)*100.0))
        return

    def re_route(self):
        self.ask_if_id_taken()

    #---------------------------------------------------------
    def ask_if_id_taken(self):
        """

        """
        
        userin = input('What Id do you want to assign?\n')
        chk = self.c.execute("""SELECT * FROM test WHERE id = ?""",(userin,))
        k = chk.fetchone()
        
        if k != None:
            print('Not available, ID taken by:')
            print(k[3])
            print('Please try again.')
            self.re_route()
        else:
            print('Available!')
            uin = input('Would you like to proceed? (Y/N)\n')
            if uin.upper() == 'Y':
                self.add_new(userin)
            else:
                pass


    def add_new(self, newid):
        """ """
        p = [1,2,3,4,5,6,7,8,20,25,15]
        dt = datetime.date.today()-datetime.timedelta(days=random.choice(p))
        self.c.execute("""INSERT INTO test VALUES (?,?,?,?)""",(newid, str(dt), random.choice(customer), newid))
        self.c.commit()
        print('New ID succesfully input!')

        c = self.c.cursor()
        c.execute("""SELECT * FROM test WHERE id = ?""",(newid,))
        print(c.fetchone())

        d = self.c.cursor()
        d.execute("""SELECT * FROM test WHERE id % 2 = 0""")
        for i in d.fetchall():
            self.print_days(i)
        self.print_db_trig()

    def print_days(self,s):
        d = datetime.datetime.today()
        p = datetime.datetime.strptime(s[1], '%Y-%m-%d')
        diff = (d - p).days
        print('Days Since: {}'.format(diff))
        if diff >= 14:
            self.triggered(s,diff)
        else:
            pass
        #self.print_db_trig()


    def triggered(self, itm, d):
        print('\nEntry ID {} Triggered\nWhos name is: {}'.format(itm[0], itm[2]))
        self.c.execute("""INSERT INTO datetrig VALUES (?,?,?)""",(itm[0], itm[2], d))
        self.c.commit()
        

    def print_db_trig(self):
        c = self.c.cursor()
        c.execute("SELECT * FROM datetrig")
        sorter = clc.OrderedDict()
        for i in c.fetchall():
            print(i)
            sorter[i[0]] = int(i[-1])

        d_sorted_by_value = clc.OrderedDict(sorted(sorter.items(), key=lambda x: x[1]))
        for k,v in d_sorted_by_value.items():
            print('ID: {}'.format(k))
            print('Days: {}\n'.format(v))


if __name__ == '__main__':
    root = tk.Tk()
    SQLBot(root, 'test')
    root.mainloop()

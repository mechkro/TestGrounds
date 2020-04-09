import sqlite3 as sql
import random
import datetime
import tkinter as tk
from tkinter import filedialog as filed
from collections import OrderedDict as od
from Adjusting_Rank import Main


#----------------------------------------------------------
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


BG =  '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'


#----------------------------------------------------------
def connect_db():
    """ """
    
    connection = sql.connect(':memory:')
    return connection    


class SQLBot:
    
    #----------------------------------------------------------
    def __init__(self, table, parent, *args):
        """ """
        self.table = table
        self.parent = parent
        self.tracker_coords = None        #Keep track of the coordinates for selection so when new one happens we can change back to default
        
        self.registar = od()
        
        self.create_frame()
        self.create_text()
        self.create_button()
        
        #self.c = connect_db()
        #self.create_table()
        #self.add_to_table()
        #x = self.print_table()
        #self.print_select(x)
    
    
    #----------------------------------------------------------
    def create_frame(self):
        """ """
        self.f = tk.Frame(self.parent, bg = BG)
        self.f.grid(row = 0, column = 0)
        return
    
    
    #----------------------------------------------------------
    def create_text(self):
        """ """
        self.txt = tk.Text(self.f, bg = BG, fg = FG, highlightbackground = DGR, font = 'Verdana 10 normal',
                           selectbackground = DGR, selectforeground = 'navy blue', selectborderwidth = 2)
        self.txt.grid(row = 0, padx = 5, pady = 5)
        self.txt.bind('<ButtonPress>', self.change_to_default)
        self.txt.bind('<ButtonRelease>', self.print_selected)
        return
    
    
    #----------------------------------------------------------    
    def create_button(self):
        """ """
        self.b = tk.Button(self.f, text = 'start', command = lambda: self.invoke_sql(),
                           bg = BG, fg = FG, font = ('Verdana', 14, 'bold'))
        self.b.grid(row = 1, padx = 5, pady = 5)
        
        self.b2 = tk.Button(self.f, text = 'main', command = lambda: self.invoke_main(),
                            bg = BG, fg = FG, font = ('Verdana', 14, 'bold'))
        self.b2.grid(row = 2, padx = 5, pady = 5)
        return
    
    
    def change_to_default(self, event):
        """ 
        Func to take previous selected text in text widget and change it back to default setting
        If first time being called it is skipped to prevent error
        """
        
        #Try and except are implemented to prevent error triggers 
        #when users clicks button and releases when no items have been selected        
        try:
            if self.tracker_coords == None:
                pass
            
            else:
                self.txt.tag_configure('highlightline', font='Verdana 10 normal', relief='raised')
                self.txt.tag_remove('highlightline', self.tracker_coords['first'], self.tracker_coords['last'])
        except Exception as e:
            pass

    
    
    def print_selected(self, event):
        """ 
        ***TO DO - change func name --- no longer print func ***
        """
        
        self.tracker_coords = {}
        
        #Try and except are implemented to prevent error triggers 
        #when users clicks button and releases when no items have been selected
        try:
            self.tracker_coords['first'] = event.widget.index(tk.SEL_FIRST)
            self.tracker_coords['last'] = event.widget.index(tk.SEL_LAST)
            
            self.txt.tag_configure('highlightline', font='Verdana 10 normal', relief='raised')
            self.txt.tag_remove('highlightline', self.tracker_coords['first'], self.tracker_coords['last'])        
            
            temp = event.widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.txt.tag_add('highlightline', tk.SEL_FIRST, tk.SEL_LAST)
            self.txt.tag_configure('highlightline', font='helvetica 20 bold', relief='raised')
            self.copy_selected(temp)
        except Exception as e:
            pass
     
    #----------------------------------------------------------
    def copy_selected(self, txt):
        """Take the selected text and copy to clipboard """
        self.parent.clipboard_append(txt)
        return
    
    #----------------------------------------------------------
    def invoke_sql(self):
        """ """
        self.c = connect_db()
        self.create_table()
        self.add_to_table()
        x = self.print_table()
        self.print_select(x)
    
    
    #----------------------------------------------------------
    def invoke_main(self):
        """ """
        m = tk.Tk()
        Main(m)
        m.mainloop()
        return
        
    #----------------------------------------------------------
    def create_table(self):
        """ """
        
        self.c.execute("""CREATE TABLE IF NOT EXISTS test (id text, date text, customer text, note text)""")
        self.c.commit()
        return
    
    
    #----------------------------------------------------------
    def add_to_table(self):
        """ """
        
        for n, i in enumerate(range(10)):
            r_customer = random.choice(customer)
            fname = random.choice(firstnames)
            lname = random.choice(lastnames)
            r_note = random.choice(notes)
            combo = '{},{} - {}'.format(fname, lname, r_note)
            dt = datetime.date.today()
            self.c.execute("""INSERT INTO test VALUES (?,?,?,?)""",(str(n), str(dt), r_customer, combo))
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

            self.txt.insert(tk.END, 'ID: {}\nDate: {}\nCustomer: {}\nNote: {}\n\n'.format(i[0], i[1], i[2], i[3]))
            self.register_entry(n,i)
            print(i)
            
        self.print_registar()
        return temp
    
    #----------------------------------------------------------
    def print_select(self, searchterm):
        """ """
        
        itr = 0
        ents = self.c.execute("""SELECT * FROM test WHERE customer = ?""",(searchterm,))
        for i in ents:
            self.txt.insert(tk.END, i)
            itr += 1
            print(i)
        print('There were {} total entries that matched "{}"'.format(itr, searchterm))
        print('Which is {} % of the total polled'.format((itr/1000.0)*100.0))
        return
    
    #----------------------------------------------------------
    def register_entry(self, line, ent):
        """ 
        
        """        
        
        self.registar[line] = ent
        return
    
    
    #----------------------------------------------------------
    def print_registar(self):
        """ 
        
        """
        
        for k, v in self.registar.items():
            print(k)
            print(v)
        return
    

#----------------------------------------------------------    
if __name__ == '__main__':
    root = tk.Tk()
    SQLBot('test', root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq3
import datetime as dt
import collections as clc



######################################################
"""
Listbox:
  
   - add the number of to do's or call log entries next to the company name

Lisbox/Combobox:

   - When listbox select is triggered load the other Combobox with the associated contacts




"""
######################################################






BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
fbig = 'terminal 12 bold'
fsmall = 'terminal 10 normal'

contacts = """'AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
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
'TEP_Irvington', 'Timet_HOLD_OFF', 'Tolin_Mechanical', 'Tolleson', 'Topock', 'Trans_Canada_Power_Plant_Coolidge', 'United_Metals', 'Wilson_Engineers'"""

cont_container = clc.OrderedDict()
parsr = []

for i in contacts.split(','):
    parsr.append(i)


parsr_parsed = list(set(parsr))
for ents in parsr_parsed:
    cont_container[ents] = []
    cont_container[ents].append(ents)

#for i in contacts:
#    x = i.split()
#    cont_container[x[0]].append(x[1::])
        
for k,v in cont_container.items():
    print(v)



customer = sorted(parsr_parsed)

"""
['AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
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
"""

vendors = ['Atlas Equipment', 'Baker Hughes', 'Baldor ABB', 'BJM  - Flow Solutions', 'Blacoh', 'Bray Valves', 'Cornell',
           'Crane Pump and Systems', 'DXP - Controls', 'DXP - Vacuum Pumps', 'Eagle Burgmann', 'Ebara', 'Emerson', 'Flex-a-seal',
           'Flowserve', 'Franklin Controls', 'Gammajet', 'Gormann Rupp', 'Grundfos', 'Hayward Gordon', 'Iwaki America',
           'JDA Global', 'John Crane', 'KSB ', 'Liquiflo', 'LMI', 'Milton Roy', 'MP Pumps', 'Nidec Motors', 'Paco (Grundfos)',
           'Patterson', 'Pioneer Equipment Inc.', 'PSG Dover', 'Pumpworks', 'Seepex', 'Sharpe Mixers', 'Simflo', 'Sundyne/Sunflo', 
           'TechnipFMC', 'Teco Motors', 'TECO-Westinghouse', 'Tornatech', 'Travaini', 'Vertiflo', 'Vulcan Pumps', 'Xylem - Auburn ',
           'Xylem - Fresno', 'Xylem - Lake Mary', 'Xylem - Morton Grove', 'Xylem - Southhaven', 'Xylem GWT/TTO', 'Xylem TTO', 'WEG Motors']



con = sq3.connect(":memory:")#r"C:\Users\kinse\Desktop\DXP_app\Databases\call_log_test.db")
con.execute("""CREATE TABLE IF NOT EXISTS notes
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               cust_name TEXT,
               note_add TEXT,
               time TEXT);""")

con.commit()



############################################################################
#---------------------------------------------------------------------------
class CustomerNotes(tk.Frame):
    
    
    def __init__(self,parent, *args):
        """ 
        
        """
        
        tk.Frame.__init__(self,
                          parent)
        self.grid()
        
        self.labelinfo = tk.Label(self,
                                  text = f"Week of: {str(dt.datetime.today()).split(' ')[0]}",
                                  bg = BG,
                                  fg = FG,
                                  font = fbig)
        self.labelinfo.grid(row = 0,
                            columnspan = 2,
                            padx = 5,
                            pady = 5,
                            sticky = tk.EW)
        
        
        self.nbook = ttk.Notebook(self)
        self.frame1 = tk.Frame(self.nbook,
                               bg = BG,
                               relief = tk.SUNKEN)     #width = 400, height = 400, relief = tk.SUNKEN)
        self.frame2 = tk.Frame(self.nbook,
                               bg = BG,
                               relief = tk.SUNKEN)     #width = 400, height = 400, relief = tk.SUNKEN)        
        self.frame1.grid(sticky = tk.NSEW)
        self.frame2.grid(sticky = tk.NSEW)
        
        
        self.nbook.add(self.frame1,
                       text = 'ACCOUNTS')
        self.nbook.add(self.frame2,
                       text = 'VENDORS')        
        self.nbook.grid(row = 1,
                        rowspan = 3,
                        column = 0,
                        padx = 5,
                        pady = 5,
                        sticky = tk.NS)
        
        
        #----------------------------------
        self.lbox = tk.Listbox(self.frame1,
                               bg = BG,
                               fg = FG,
                               font = fsmall,
                               height = 15)
        self.lbox.grid(row = 0,
                       column = 0,
                       padx = 5,
                       pady = 5,
                       sticky = tk.NS)
    
        self.lbox.bind('<<ListboxSelect>>',
                       self.load_active)
        
        self.lbox2 = tk.Listbox(self.frame2,
                                bg = BG,
                                fg = FG,
                                font = fsmall,
                                height = 15)
        self.lbox2.grid(row = 0,
                        column = 0,
                        padx = 5,
                        pady = 5, 
                        sticky = tk.NS)
    
        
        #-------------------------------
        self.entryframe = tk.Frame(self)
        self.entryframe.grid(row = 1,
                             column = 1,
                             sticky = tk.EW)
        
        self.text1 = tk.Text(self.entryframe,
                             height = 5,
                             width = 60)
        self.text1.grid(row = 1,
                        column = 0,
                        padx = 5, 
                        pady = 5,
                        sticky = tk.EW)
        
        self.text2 = tk.Text(self,
                             height = 10, 
                             width = 60,
                             state = 'normal')
        self.text2.grid(row = 2,
                        rowspan = 2,
                        column = 1,
                        padx = 5,
                        pady = 5,
                        sticky = tk.NSEW)
        
        self.bnew = tk.Button(self.entryframe, text = 'submit', command = lambda: self.entry_submit())
        self.bnew.grid(row = 2, column = 0, sticky = tk.EW)        
        
        self.cbox = ttk.Combobox(self.entryframe,
                                 values = customer)
                                 #postcommand = self.combo_update)
        self.cbox.grid(row = 3, sticky = tk.EW)
        
        self.cbox.bind("<<ComboboxSelected>>", self.print_combo_select)
        self.add_customers()
        self.add_vendors()
    
    
    
    ############################################################################
    #---------------------------------------------------------------------------
    def combo_update(self, event):
        """ 
        
        """
        self.load_combobox(self.lbox.get(self.lbox.curselection()))
    
    
    
    ############################################################################
    #---------------------------------------------------------------------------
    def print_combo_select(self, event):
        """ 
        
        """
        print(event.widget.current(), event.widget.get())
        
        
    
    ############################################################################
    #---------------------------------------------------------------------------
    def load_active(self, event):
        """ 
        
        """
        
        try:
            selection = self.lbox.get(self.lbox.curselection())        #Grab the current highlighted listbox object
            self.clear_text_1()
            self.text1.insert(1.0, f"{selection}:\n")
            
            x = con.execute("SELECT * FROM notes WHERE cust_name = ?", (selection,))
            f = x.fetchall()
            
            self.clear_text_2()
            
            if f:
                for i in f:
                    self.text2.insert(tk.END, f"{i}\n")
                    
            else:
                self.text2.insert(tk.END, f'{selection}: No Entries')
                
            x.close()
            
            self.load_combobox(selection)
            
        except Exception as e:
            #print(e)
            pass
        
        self.cbox.update()
        return
        

        
    
    ############################################################################
    #---------------------------------------------------------------------------
    def load_combobox(self, ent):
        """ 
        
        """
        #print([i for i in [j for j in cont_container[ent] if j != '']])
        selects = [str(i) for i in cont_container[ent]]
        self.cbox.config(values = [j for j in selects if len(j) > 1])
                         #[i for i in cont_container[ent] if i.encode('utf-8') != ''])

        return 
    

    
    ############################################################################
    #---------------------------------------------------------------------------    
    def add_customers(self):
        """ 
        
        """
        
        for i in customer:
            self.lbox.insert(tk.END, i)
        
        return
    
    
    
    ############################################################################
    #---------------------------------------------------------------------------    
    def add_vendors(self):
        """ 
        
        """
        
        for i in vendors:
            self.lbox2.insert(tk.END, i)
        
        return    
    
    
    ############################################################################
    #---------------------------------------------------------------------------    
    def entry_submit(self):
        """ 
        
        """
        
        company = self.lbox.get(self.lbox.curselection())       #Grab current active object in listbox
        note = self.text1.get(1.0, tk.END)                      #Pull all the text
        time = dt.datetime.now()                                #Grab the date and time at moment of trigger
        
        self.add_database(company, note, time)                  #Send to func to be placed in DB
        
        self.clear_text_1()
        self.clear_text_2()
        
        q = con.execute("""SELECT * FROM notes WHERE cust_name = ?""",(company,))
        for i in q.fetchall():
            self.text2.insert(tk.END, f"{i}\n")
        
        q.close()
        
        return
    
    
    
    
    
    ############################################################################
    #---------------------------------------------------------------------------
    def add_database(self, c, n, t):
        """ 
        (id ,cust_name , note_add TEXT, time TEXT)
        """
        
        cur = con.cursor()
        cur.execute("""INSERT INTO notes
                       (id, cust_name, note_add, time) 
                       VALUES (null,?, ?, ?);""",(c,n,t))
        con.commit()
        cur.close()
        
        self.test_entry(c)
        
    
    
    
    ############################################################################
    #---------------------------------------------------------------------------    
    def test_entry(self, c):
        """ 
        
        """
        
        q = con.cursor()
        ents = q.execute("""SELECT * FROM notes WHERE cust_name = ?""",(c,))
        if ents.fetchall():
            for i in ents.fetchall():
                self.text2.insert(tk.END, f"\nCompany: {i[1]}\nNote: {i[2]} @ {i[3]}\n---------------------------------------\n")
        
        else:
            print("""Error  - TEST ENTRY""")
        q.close()
        
    
    
    

    ############################################################################
    #---------------------------------------------------------------------------   
    def clear_text_1(self):
        """ 
        
        """
        
        self.text1.delete(1.0, tk.END)
        return
    
    
    ############################################################################
    #---------------------------------------------------------------------------   
    def clear_text_2(self):
        """ 
        
        """
        
        self.text2.delete(1.0, tk.END)
        return    






############################################################################
#---------------------------------------------------------------------------
if __name__=='__main__':
    """
    
    """
    root = tk.Tk()
    root.title('Note-Taker')
    CustomerNotes(root)
    root.mainloop()

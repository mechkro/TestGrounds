import tkinter as tk
from tkinter import ttk
import sqlite3 as sql


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

############################################################################################
#VENDORS=========================
#PUMPS-----------
vendors_pumps = """AC Fire Pump, a Xylem Brand
American Marsh
ARO
Atlas Equipment
BJM
Crane (Barnes, Deming, Weinman)
Ebara
Envirogear
Finish Thompson
FMC
Gorman Rupp
Goulds Water Technology, a Xylem Brand
Grundfos (Paco, Peerless)
Hayward Gordon
HP-Plus
Hydra-Cell
KSB
Iwaki
JDA Corporation - NOMAD
Liquiflo
LMI
Milton Roy
Patterson
Pentair (Aurora, Fairbanks, Myers)
PumpWorks Industrial
PumpWorks 610
SEEPEX
Sundyne/Sunflo/Kontro/HMD
Vertiflo
Vulcan Pumps
Warren Rupp (SandPiper)
""".splitlines()


#MECHANICAL SEALS/ PACKING----------
vendors_seals = """Flexaseal
John Crane
Lemco
Momentum""".splitlines()


#POWER TRANSFER/ COUPLINGS-----------
vendors_powertransfer = """Dodge
Falk
Rexnord
TB Woods""".splitlines()

#AGITATORS/ TANK CLEANING-----------
vendors_agitators_tankclean = """
Alfa Laval/Gamajet
Hayward Gordon
KSB
Scott Turbon
Sharpe""".splitlines()

#GEAR BOXES----------
vendors_gearbox = """Amarillo
Dodge
IDC
Nord
Rexnord""".splitlines()

#HEAT EXCHANGERS-----------
vendors_heatx = """APV
Standard Exchange
Tranter""".splitlines()

#VACUUM PUMPS/ BLOWERS-----------
vendors_vacpumpblow = """
Airtech
Dekker
National Vacuum
Travaini Pumps
Tuthill""".splitlines()


#FILTRATION & SEPARATION-----------
vendors_filtersep = """Eaton Filtration
Lakos
Rosedale
United""".splitlines()


#MISC. AND ACCESORIES-----------
vendors_miscaccess = """Belco Fiberglass Tanks/Ductwork
Strongwell Fiberglass Grating
Dupont Vespel Bearings
Babbitt Bearing Repair
Controls
Instrumentation
Motors
VFDs""".splitlines()


vendors_directory = {'PUMPS': vendors_pumps,
                            'MECHANICAL_SEALS_PACKING':vendors_seals,
                            'POWER_TRANSFER_COUPLINGS':vendors_powertransfer,
                            'GEAR_BOXES':vendors_agitators_tankclean,
                            'GEAR_BOXES':vendors_gearbox, 
                            'HEAT_EXCHANGERS':vendors_heatx,
                            'VACUUM_PUMPS_BLOWERS':vendors_vacpumpblow,
                            'FILTRATION_SEPARATION':vendors_filtersep, 
                            'MISC_AND_ACCESORIES':vendors_miscaccess}

#---------------------------------------------------
class ComboBox_app(tk.Frame):
    
    
    #----------------------------------------------------------
    def __init__(self, *args):
        tk.Frame.__init__(self,*args)
        self.grid()
       
        self.setup_sql()
        self.label = tk.Label(self, text = 'Customers').grid(column=0, row=0, padx = 5, pady = 5)
        self.cbox = ttk.Combobox(self, 
                                    values = customer)
        
        self.cbox.grid(column=0, row=1, padx = 5, pady = 5)
        self.cbox.bind("<<ComboboxSelected>>", self.callbackFunc)    
        
        self.var = tk.StringVar()
        self.label2 = tk.Label(self, text = 'Choose Product Category').grid(column=0, row=2, padx = 5, pady = 5)
        self.cbox2 = ttk.Combobox(self, values = [i for i in vendors_directory.keys()], textvariable = self.var)
        self.cbox2.grid(column=0, row=3, padx = 5, pady = 5)
        self.var.trace("w", self.get_category)
        
        self.lbox = tk.Listbox(self, width = 20, height = 10)
        self.lbox.grid(row = 4, column = 0, padx = 10, pady = 10)
        #self.txt = tk.Text(self, width = 20, height = 10)
        #self.txt.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.mainloop()
    
    #----------------------------------------------------------   
    def setup_sql(self):
        """ """
        self.c = sql.connect(':memory:')
        self.cur = self.c.cursor()
        
        for k,v in vendors_directory.items():
            self.create_tables()
            self.load_database(k,v)
        self.pull_data()
        return        
        
    #----------------------------------------------------------        
    def create_tables(self):
        """ """
        self.c.execute("""CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY, cat TEXT, supp TEXT);""")
        self.c.commit()
        return
            
    #----------------------------------------------------------         
    def load_database(self, k,v):
        """ """
        for i in v:
            self.cur.execute("""INSERT INTO suppliers (cat, supp) VALUES (?,?);""",(k,i))
            self.c.commit()
        return
    
    #----------------------------------------------------------   
    def pull_data(self):
        """ """
        for k,v in vendors_directory.items():
            self.cur.execute("""SELECT * FROM suppliers""")
            for thing in self.cur.fetchall():
                print(thing)
        return
            
    #----------------------------------------------------------    
    def callbackFunc(self, event):
        """ """
        feedback = ("New Element Selected: {}".format(event.widget.get())).split(':')
        print(feedback)
        print(' '.join(feedback[:]))
        
    #----------------------------------------------------------   
    def get_category(self, *args):
        """ """
        contents = vendors_directory[self.cbox2.get()]
        self.lbox.delete(0, tk.END)
        
        for i in contents:
            self.lbox.insert(tk.END, i)
    
        
        
if __name__ == '__main__':
    ComboBox_app()  

    

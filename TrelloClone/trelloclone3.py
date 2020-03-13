import tkinter as tk
import random


#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
#-----------------------------------------------------------------------------------



acc_list = """ABBOTT_NUTRITION
ABRAMS_AIRBORNE_MANUFACTURING_INC
AIR_LIQUIDE
AIR_PRODUCTS_AND_CHEMICALS
AMEC_ENGINEERING
AMES_CONSTRUCTION
APACHE_NITROGEN
APPLIED_LNG
ARCADIS
ARCHER_WESTERN
ARGUS_CONSULTING
ARIZONA_MINING_COMPANY
ARIZONA_PACIFIC_WOOD
AZ_COOP
BLACK_and_VEATCH
BOULDER_CITY
BROWN_and_CALDWELL
BULL_MOOSE_TUBE_CO
CALPINE
CAMP_DRESSER_MCGHEE
CAROLLO
CASA_GRANDE
CCA
CCWRD
CHINO_VALLEY
CITY_OF_AVONDALE
CITY_OF_BULLHEAD
CITY_OF_CASA_GRANDE_WWTP
CITY_OF_CHANDLER
CITY_OF_CHANDLER_PACOS_WTP
CITY_OF_FLAGSTAFF
CITY_OF_HENDERSON
CITY_OF_LAS_VEGAS
CITY_OF_MESA
CITY_OF_NORTH_LV
CITY_OF_PHOENIX
CLARK_COUNTY_DEPT_AVIATION
CLARK_COUNTY_WATER_RECLAMATION_DISTRICT
CLEARWATER_PAPER
DAISY_SOUR_CREAM
DAVIS_MONTHAN_AFB
DESERT_STAR_ENERGY_CENTER
DRAKE_MATERIALS
EHRMANNS_DAIRY
ENVIROGEN
ENVIROMENTAL_BIOMASS
EPCOR_BULLHED_CITY
EUCLID_CHEMICAL_ELOY
EVOQUA_CHANDLER
EVOQUA_MESA
EVOQUA_PARKER
FAIRIBAULT_FOODS
FANN_ENVIRONMENTAL_LLC
FELIX_CONSTRUCTION
FLSMIDTH
FLUID_SOLUTIONS
FMI_AJO
FMI_BISBEE
FMI_CORP
FMI_BAGDAD
FMI_SIERRITA
FRANKLIN_FOODS_CREAM_CHEESE
FRITO_LAY
FT_HUACHUCA
FT_MOJAVE
GARVER_USA
GCW_ENGINEERING
GREELEY_and_HANSEN
GREEN_VALLEY_PECANS
GRIFFITH_ENERGY_NEW_STAR_ENERGY
HAZEN_and_SAWYER
HDR
HENDERSON_ELECTRIC
HEXCEL
HONEYWELL_JONES_LANG_LASELLE
HUNTER_CONTRACTING
HYDRO_GEO_CHEM
IBM
IDG_
JACOBS_
KIEWIT_CONSTRUCTION
KIMLEY_HORN
KINDER_MORGAN_
KINDER_MORGAN_
KINDER_MORGAN_
ALL_KINGMAN
LAUGHLIN_WATER_RECLAIM
LAYTON_CONSTRUCTION
LHOIST_NORTH_AMERICA
LPC_CONSTRUCTION
LPC_CONTSTRUCTION
LVVWD
MCCARTHY_BUILDING_COMPANIES
MGC_CONTRACTORS_INC
MINGUS_CONSTRUCTORS
MORRISON_MAIERLE
NELTEC
NEVADA_COGEN
NEVADA_RESELLERS
NEVADA_SOLAR_ONE
NEXUS_ENERGY
NORD_COPPER
NUCOR
NV_ENERGY
OCEANSPRAY
OLIN_CHLOR
PARAGON_SERVICES_LLC
PCL_CONTRUCTION
PIMA_COUNTY_WW
POGGEMEYER_ENGINEERS
PRAXAIR_ELECTRONICS
PRO_PETROLEUM
RAIN_BIRD
RAYTHEON
RENEWABLE_ALGAL_ENERGY
ROMTEC_UTILITIES
SASOL_INC
SEVERN_TRENT_ENVIRONMENTAL_SERVICES
SIERRA_VISTA_REGIONAL_HEALTH_CENTER
SLATER_HANNIFAN_GROUP
SLETTEN_COMPANIES
SOUTHERN_NEVADA_WATER_AUTHORITY
SRP_DESERT_BASIN
STANTEC_CONSULTING
SUN_MECHANICAL
SUNDT_CONSTRUCTION
SWISSPORT_FUELING_
TEP
TEP_IRVINGTON
TIMET
TOLIN_MECHANICAL
TOWN_OF_CASA_GRANDE_
TOWN_OF_KINGMAN
TOWN_OF_QUEEN_CREEK
TOWN_OF_WICKENBURG
TRANS_CANADA_POWER_PLANT
WALSH_GROUP_ARCHERWESTERN
WESTERN_EMULSIONS
WILSON_ENGINEERING
WATERWORKS_ENGINEERS
"""







#-----------------------------------------------------------------------------------
###########################################

class Initiate(object):
    
    
    #-----------------------------------------------------------------------------------
    def __init__(self, master):
        """ 
        
        """
        
        self.master = master
        self.master.title('Trello Clone')
        self.master.config(bg = BG)
        
        #Create the dictionariess to hold our widgets
        self.framehold = {}
        self.labelhold = {}
        self.labelframehold = {}
        self.texthold = {}
        self.listboxhold = {}
        self.butthold = {}
        
        col_titles = [('Not Started','red'), ('In Progress', 'yellow'), ('Completed','green')]
        col_desc = ['Total Entries: ', 'Total Entries: ', 'Total Entries: ']
        itr = 0
    
    
        self.framehold[itr] = self.make_frame().grid(row = 0, column = 1,  padx = 5, pady = 5)   #Total of 9 frames made
        self.labelframehold[itr] = tk.LabelFrame(self.framehold[itr], text = 'Nav. Window', bg = BG, fg = FG).grid(padx = 5, pady = 5, sticky = tk.NS)#row = 0, column = 1, padx = 5, pady = 5, sticky = tk.NS)
        self.t = tk.Text(self.labelframehold[itr], bg = BG, fg = FG, width = 20, height = 25).grid(row = 0, rowspan = 5, column = 0, padx = 5, pady = 5)
        
        #self.labelframehold[itr] = tk.LabelFrame(self.framehold[itr], text = 'Nav. Window', bg = BG, fg = FG).grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.NS)
        
        for i in range(5):
                itr += 1
                
                self.butthold[itr-1] = tk.Button(self.labelframehold[0], text = '{}'.format(i), bg = BG, fg = FG, command = lambda: None).grid(row = i, column = 1, padx = 5, pady = 5, sticky = tk.NS)
                self.framehold[itr-1] = self.make_frame().grid(row = i, column = 2, padx = 5, pady = 5)   #Total of 9 frames made
                self.texthold[itr-1] = self.make_text(self.framehold[itr-1], *[i,2])
        

        
        ##------------------------------------------------ Column 1 - Buttons
        #self.butt_fwd_col1 = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        #self.butt_fwd_col1.grid(row = 3, column = 0, pady = 2, sticky = tk.EW)
        
        #self.butt_fwd_col1.bind('<Button-1>', self.button_binding_1)
        
        #self.butt_fwd_col1_2 = tk.Button(self.master, text = 'Change FG', bg = BG, fg = FG, command = lambda: self.highlight_selected(self.listboxhold[0], self.listboxhold[0].curselection()), font = ('Vardana',14,'bold'))
        #self.butt_fwd_col1_2.grid(row = 4, column = 0, pady = 2, sticky = tk.EW)
          
        
        ##------------------------------------------------ Column 2 - Buttons
        #self.butt_fwd_col2_left = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        #self.butt_fwd_col2_left.grid(row = 3, column = 1, pady = 2, sticky = tk.EW)
        
        #self.butt_fwd_col2_left.bind('<Button-1>', self.button_binding_2_left)
        
        #self.butt_fwd_col2_right = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        #self.butt_fwd_col2_right.grid(row = 4, column = 1, pady = 2, sticky = tk.EW)
        
        #self.butt_fwd_col2_right.bind('<Button-1>', self.button_binding_2_right)        
        
        
        ##------------------------------------------------ Column 3 - Buttons
        #self.butt_fwd_col3 = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        #self.butt_fwd_col3.grid(row = 3, column = 2, pady = 2, sticky = tk.EW)
        
        #self.butt_fwd_col3.bind('<Button-1>', self.button_binding_3)
        
        #self.butt_fwd_col3_2 = tk.Button(self.master, text = 'Change FG', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',14,'bold'))
        #self.butt_fwd_col3_2.grid(row = 4, column = 2, pady = 2, sticky = tk.EW)        
        
        #self.buttonhold = {1:self.butt_fwd_col1,
                                      #2:self.butt_fwd_col2_left,
                                      #3:self.butt_fwd_col2_right,
                                      #4:self.button_binding_3}
        
        
        #self.detailslf = tk.LabelFrame(self.master, text = 'Current Entry: None', bg = BG, fg = FG, font = ('Vardana',13,'bold'))
        #self.detailslf.grid(row = 5, column = 0, columnspan = 3, padx = 5, pady = 5, sticky = tk.EW)
        
        #self.details_pane = tk.Text(self.detailslf, bg = BG, fg = FG, height = 5, width = 100)
        #self.details_pane.grid(padx = 10, pady = 5, sticky = tk.NSEW)
        
        
        #a_list = acc_list.split('\n')   #split up the ltriple quote into list
        
        #for itms in a_list:               #Iterate through the list to insert into listbox  
            #self.testing_entries(self.listboxhold[0], itms)
        
        #self.update_totals_labels()

    
    
     #-----------------------------------------------------------------------------------
    def update_totals_labels(self):
        """ """
        for i, widge in enumerate(self.labelhold.values()):
            qty = self.listboxhold[i].size()
            widge.config(text = 'Total Entries: {}'.format(qty))
        
        return
                            
    
    #-----------------------------------------------------------------------------------
    def testing_entries(self, widge, ent):
        """ 
        
        """    
        return widge.insert(tk.END, ent)
    
    
    
    #-----------------------------------------------------------------------------------
    def highlight_selected(self, widge, indx_list):
        """ """
        for itms in indx_list:
            widge.itemconfig(itms, fg = DGR)
        return
    
    
    
    #-----------------------------------------------------------------------------------
    def make_frame(self,*args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return tk.Frame(self.master, bg = BG)
    
    
    #-----------------------------------------------------------------------------------
    def make_labelframe(self, parent, txt, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
            
        lf = tk.LabelFrame(parent, text = txt, bg = BG, fg = FG, font = ('Vardana',18,'bold'))
        lf.grid(row = args[0], column = args[1], padx = 5, pady = 5, sticky = tk.EW)
        return lf
    
    
    #-----------------------------------------------------------------------------------
    def make_listbox(self, parent, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        lb = tk.Listbox(parent, bg = BG, fg = FG, font = ('Vardana',8,'normal'), width = 45, height = 18, selectmode = tk.EXTENDED)
        lb.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        
        #Adding click button 1 binding to display details in details pane
        lb.bind('<Double-Button-1>', self. display_details)
        return lb   
    
    
    
    def display_details(self, event):
        """ 
        """
        
        try:
            idx= event.widget.curselection()
            txt = event.widget.get(idx)
            self.details_pane.delete(1.0, tk.END)
            self.details_pane.insert(tk.END, txt)
            self.detailslf.config(text = 'Current:     ---  {}  ---    '.format(txt))
            
        except Exception as e:
            print(e)
            
        return
        
        
        
    #-----------------------------------------------------------------------------------
    def make_text(self, parent, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        t = tk.Text(parent, bg = BG, fg = FG, font = ('impact',8,'normal'), width = 35, height = 5)
        t.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        return t
    
    #-----------------------------------------------------------------------------------
    def make_label(self, parent,  txt, *args):
        """ 
        After frame is made - we create a label instance for parent frame and then return.
        During creation we call to binding function to add enter and leave functionality
        """
        
        
        l = tk.Label(parent, text = txt, bg = BG, fg = FG, font = ('Vardana',10,'normal'))
        l.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        self.add_binding(l)     #Add Binding to functionality before returning the label to dictionary
        
        return l   
    
    
    #-----------------------------------------------------------------------------------
    def add_binding(self, widge):
        """ 
        
        """
        
        widge.bind('<Enter>', self.change_txt_color)
        widge.bind('<Leave>', self.change_txt_def_color)
        return
        
    
    #-----------------------------------------------------------------------------------
    def change_txt_color(self, event):
        """ 
        
        """
        
        event.widget.config(fg = DGR, font = ('Vardana',10,'normal'))
        return 
        
        
    #-----------------------------------------------------------------------------------
    def change_txt_def_color(self, event):
        """ 
        
        """
        
        event.widget.config(fg = FG, font = ('Vardana',10,'normal'))
        return         
        
        
    #-----------------------------------------------------------------------------------
    def button_binding_1(self, event):
        """ 
        Listbox's have had Extended selectionmode enabled. User can select many entries using shift  or cntrl keyboard buttons.
        Func will then take each item in the selected array and then one by one add them to new Listbox is next column
        """
        
        try:
            att = self.listboxhold[0].curselection()
            print(len(att))
            for i in att:
                curent = self.listboxhold[0].get(i)
                self.listboxhold[1].insert(tk.END, curent) 
                self.listboxhold[0].delete(i)
        
        except:
            print('failed')
            
        self.update_totals_labels()
     
       
    #-----------------------------------------------------------------------------------       
    def button_binding_2_left(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[1].get(tk.ACTIVE)
            self.listboxhold[1].delete(tk.ACTIVE)
            self.listboxhold[0].insert(tk.END, select)        
            
        except:
            print('failed')
    
        self.update_totals_labels()
    
    #-----------------------------------------------------------------------------------       
    def button_binding_2_right(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[1].get(tk.ACTIVE)
            self.listboxhold[1].delete(tk.ACTIVE)
            self.listboxhold[2].insert(tk.END, select)        
            
        except:
            print('failed')
            
        self.update_totals_labels()
    
    
    #-----------------------------------------------------------------------------------
    def button_binding_3(self, event):
        """ 
        
        """
        
        try:
            select = self.listboxhold[2].get(tk.ACTIVE)
            self.listboxhold[2].delete(tk.ACTIVE)
            self.listboxhold[1].insert(tk.END, select)      
            
        except:
            print('failed')
        
        self.update_totals_labels()
      


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    """ """
    
    root = tk.Tk()
    Initiate(root)
    root.mainloop()

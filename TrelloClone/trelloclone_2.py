import tkinter as tk
import random
import functools as func
import sqlite3 as sql3




#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
#-----------------------------------------------------------------------------------





proj_outline = """

Consist of 3 columns of widgets.
In each will be a listbox to store the entries. Every entry starts in the first column and
is user-triggered moved to the middle and then the next.

Reason being - This is for a to do tracker. 3 columns are named:

- Not Started - These are to dos that have just been recently logged
- In Progress - We have started the to do
- Completed - To do entry has been completed.

For cleanliness - each entry will on comprise of a view line in the form.
- Customer/Account - Days since put intp db

Only when the item is clicked will it bring up the details view where users can view and
edit if required.

tables:
- viewline VALUES (id INTEGER PRIMARY KEY, cusacc TEXT, date TEXT)
- entstore VALUES (id INTEGER PRIMARY KEY, notes TEXT)

ID's need to be one of a kind, so we do not mix the notes up


"""



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
WATERWORKS_ENGINEERS"""





sqlfileloc = r'none'




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

        self.menu = tk.Menu(self.master)
        self.menu.add_command(label = 'Move: In Progress', command = self.move_to_inprogress)
        self.menu.add_command(label = 'Move: Completed', command = self.move_to_completed)
        self.menu.add_command(label = 'Cancel', command = lambda: None)
        self.master.bind('<3>', lambda e: self.menu.post(e.x_root, e.y_root))
        
        #Create the dictionariess to hold our widgets
        self.framehold = {}
        self.labelhold = {}
        self.labelframehold = {}
        self.texthold = {}
        self.listboxhold = {}
        self.menuhold = {}
        
        col_titles = [('Not Started', FG), ('In Progress', FG), ('Completed', FG)]  #'red', 'yellow', 'green'
        col_desc = ['Total Entries: ', 'Total Entries: ', 'Total Entries: ']
        itr = 0
    
        
        for i in range(3):
            for j in range(3):
                
                self.framehold[itr] = self.make_frame()
                self.framehold[itr].grid(row = i, column = j, padx = 3, pady = 3)   #Total of 9 frames made
                self.framehold[itr].bind('<Enter>', self.change_clr_enter)
                self.framehold[itr].bind('<Leave>', self.change_clr_leave)
        
                if itr <= 2:
                    self.labelframehold[j] = self.make_labelframe(self.framehold[itr], '{}'.format(col_titles[itr][0]), col_titles[itr][1], *[i, j])
                    self.labelhold[itr] = self.make_label(self.labelframehold[itr], '{}'.format(col_desc[itr]), *[ i, 0])
                    
                if 2 < itr <= 5:
                    self.listboxhold[itr -3] = self.make_listbox(self.framehold[itr], *[i,0])
                    self.listboxhold[itr - 3].bind('<ButtonRelease>', self.change_lab_selected)
##                    self.menuhold[itr-3] = tk.Menu(self.listboxhold[itr -3])
##                    self.menuhold[itr-3].add_command(label = 'OK')
##                    self.listboxhold[itr - 3].bind('<3>', lambda e: self.menuhold[itr-3].post(e.x, e.y))
                
                itr += 1

        #The following labels are for displaying the amount of selected items in a list
        #The listbox are binded by button release event to call func to alter these
                
        self.lab_selected_col_1 = tk.Label(self.labelframehold[0], text = 'Selected Entries: {}'.format('-'), bg = BG,
                                           fg = FG)
        self.lab_selected_col_1.grid(row = 2, padx = 3, pady = 3)

        self.lab_selected_col_2 = tk.Label(self.labelframehold[1], text = 'Selected Entries: {}'.format('-'), bg = BG,
                                           fg = FG)
        self.lab_selected_col_2.grid(row = 2, padx = 3, pady = 3)
        
        self.lab_selected_col_3 = tk.Label(self.labelframehold[2], text = 'Selected Entries: {}'.format('-'), bg = BG,
                                           fg = FG)
        self.lab_selected_col_3.grid(row = 2, padx = 3, pady = 3)

        
        #------------------------------------------------ Column 1 - Buttons
        self.butt_fwd_col1 = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',8,'bold'))
        self.butt_fwd_col1.grid(row = 3, column = 0, pady = 2, sticky = tk.EW)
        
        self.butt_fwd_col1.bind('<Button-1>', self.button_binding_1)
        
        self.butt_fwd_col1_2 = tk.Button(self.master, text = 'Add NEW', bg = BG, fg = FG, command = lambda: self.maker_new_todo, font = ('Vardana',8,'bold'))
        self.butt_fwd_col1_2.grid(row = 4, column = 0, pady = 2, sticky = tk.EW)
          
        
        #------------------------------------------------ Column 2 - Buttons
        self.butt_fwd_col2_left = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: self.highlight_selected(self.listboxhold[1],
                                            self.listboxhold[1].curselection()), font = ('Vardana',10,'bold'))
        self.butt_fwd_col2_left.grid(row = 3, column = 1, pady = 2, sticky = tk.EW)
        
        self.butt_fwd_col2_left.bind('<Button-1>', self.button_binding_2_left)
        
        self.butt_fwd_col2_right = tk.Button(self.master, text = '>', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col2_right.grid(row = 4, column = 1, pady = 2, sticky = tk.EW)
        
        self.butt_fwd_col2_right.bind('<Button-1>', self.button_binding_2_right)        
        
        
        #------------------------------------------------ Column 3 - Buttons
        self.butt_fwd_col3 = tk.Button(self.master, text = '<', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col3.grid(row = 3, column = 2, pady = 2, sticky = tk.EW)
        
        self.butt_fwd_col3.bind('<Button-1>', self.button_binding_3)
        
        self.butt_fwd_col3_2 = tk.Button(self.master, text = 'Change FG', bg = BG, fg = FG, command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col3_2.grid(row = 4, column = 2, pady = 2, sticky = tk.EW)        
        
        self.buttonhold = {1:self.butt_fwd_col1,
                                      2:self.butt_fwd_col2_left,
                                      3:self.butt_fwd_col2_right,
                                      4:self.button_binding_3}
        
        
        self.detailslf = tk.LabelFrame(self.master, text = 'Current Entry: None', bg = BG, fg = FG, font = ('Vardana',10,'bold'))
        self.detailslf.grid(row = 5, column = 0, columnspan = 3, padx = 3, pady = 3, sticky = tk.EW)
        
        self.details_pane = tk.Text(self.detailslf, bg = BG, fg = FG, height = 6, width = 150,
                                    selectbackground = DGR, selectforeground = 'black', state = tk.DISABLED)
        self.details_pane.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)#tk.NSEW)
        
        
        a_list = acc_list.split('\n')   #split up the ltriple quote into list
        
        for itms in a_list:               #Iterate through the list to insert into listbox  
            self.testing_entries(self.listboxhold[0], itms)
        
        self.update_totals_labels()


##    #-------------------------------
##    def popupmenu(self, x, y):
##        self.master.bind('<3>', lambda: self.menu.post(x, y))


    #-----------------------------------------------------------------------------------
    def move_to_inprogress(self):
        """ """
        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[0].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[0].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[0].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[1].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[1].delete(0, tk.END)               #Delete all entries of new listbox destination
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            if not thngs:
                pass
            else:
                self.listboxhold[1].insert(tk.END, thngs)
                
        self.listboxhold[0].selection_clear(0, tk.END)
        self.listboxhold[0].selection_set(0)
        self.update_totals_labels()
        
##        grab = self.listboxhold[0].curselection()
##        for i in grab:
##            txt = self.listboxhold[0].get(i)
##            print(txt)

    #-----------------------------------------------------------------------------------
    def move_to_completed(self):
        """ """
        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[0].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[0].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[0].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[1].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[1].delete(0, tk.END)               #Delete all entries of new listbox destination
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            if not thngs:
                pass
            else:
                self.listboxhold[1].insert(tk.END, thngs)
                
        self.listboxhold[0].selection_clear(0, tk.END)
        self.listboxhold[0].selection_set(0)
        self.update_totals_labels()
        
##        grab = self.listboxhold[0].curselection()
##        print(grab)


    #-----------------------------------------------------------------------------------
    def maker_new_todo(self):
        """ """
        pass


    #-----------------------------------------------------------------------------------
    def change_lab_selected(self, event):
        """ """
        if event.widget == self.listboxhold[0]:
            numbsel = len(event.widget.curselection())
            self.lab_selected_col_1.config(text = 'Selected Entries: {}'.format(numbsel))
        if event.widget == self.listboxhold[1]:
            numbsel = len(event.widget.curselection())
            self.lab_selected_col_2.config(text = 'Selected Entries: {}'.format(numbsel))
        if event.widget == self.listboxhold[2]:
            numbsel = len(event.widget.curselection())
            self.lab_selected_col_3.config(text = 'Selected Entries: {}'.format(numbsel))


    #-----------------------------------------------------------------------------------
    def change_clr_enter(self, event):
        """ """
        for k,v in self.framehold.items():
            if event.widget in v.children:
                event.widget.config(bg = 'blue')
            else:
                pass
        

    #-----------------------------------------------------------------------------------
    def change_clr_leave(self, event):
        """ """
        pass
        
    
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
    def make_labelframe(self, parent, txt, clr, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
            
        lf = tk.LabelFrame(parent, text = txt.upper(), bg = BG, fg = clr, font = ('Vardana',14,'bold'))
        lf.grid(row = args[0], column = args[1], padx = 5, pady = 5, sticky = tk.EW)
        return lf
    
    
    #-----------------------------------------------------------------------------------
    def make_listbox(self, parent, *args):
        """ 
        
        """
        #try:
            #f = tk.Frame(self.master, bg = BG)
            #f.grid(row = args[0], column = args[1], padx = 5, pady = 5)
        lb = tk.Listbox(parent, bg = BG, fg = FG, font = ('Vardana',8,'normal'), selectmode = tk.EXTENDED, width = 45) #,width = 45, height = 18, selectmode = tk.EXTENDED)
        lb.grid(row = args[0], column = args[1], padx = 3, pady = 3)
        
        #Adding click button 1 binding to display details in details pane
        lb.bind('<Double-Button-1>', self. display_details)
        return lb   
    
    
    #-----------------------------------------------------------------------------------    
    def display_details(self, event):
        """ 
        """
        
        try:
            idx= event.widget.curselection()
            txt = event.widget.get(idx)
            self.details_pane.delete(1.0, tk.END)
            self.details_pane.insert(tk.END, '----------- {} --------------------\n'.format(txt))
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
        t = tk.Text(parent, bg = BG, fg = FG, font = ('impact',8,'normal'))#, width = 37, height = 7)
        t.grid(row = args[0], column = args[1], padx = 3, pady = 3)
        return t

    
    #-----------------------------------------------------------------------------------
    def make_label(self, parent,  txt, *args):
        """ 
        After frame is made - we create a label instance for parent frame and then return.
        During creation we call to binding function to add enter and leave functionality
        """
        
        
        l = tk.Label(parent, text = txt, bg = BG, fg = FG, font = ('Vardana',10,'normal'))
        l.grid(row = args[0], column = args[1], padx = 3, pady = 3)
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
        
    
    ############# Bindings of teh buttons and transfering of ACTIVE items #################
    #-----------------------------------------------------------------------------------
    def button_binding_1(self, event):
        """ 
        Listbox's have had Extended selectionmode enabled. User can select many entries using shift  or cntrl keyboard buttons.
        Func will then take each item in the selected array and then one by one add them to new Listbox is next column

        EDIT - added extra functionality for sorting list with new items for alphabetical considerations. Takes the selected items
        and current listbox that is being moved to items and sorts before re-applying entries
        """

        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[0].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[0].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[0].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[1].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[1].delete(0, tk.END)               #Delete all entries of new listbox destination
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            if not thngs:
                pass
            else:
                self.listboxhold[1].insert(tk.END, thngs)
                
        self.listboxhold[0].selection_clear(0, tk.END)
        self.listboxhold[0].selection_set(0)
        self.update_totals_labels()                         #Call to adjust the totals labels
     
       
    #-----------------------------------------------------------------------------------       
    def button_binding_2_left(self, event):
        """ 
        
        """

        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[1].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[1].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[1].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[0].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[0].delete(0, tk.END)               #Delete all entries of new listbox destination
        
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            if not thngs:
                pass
            else:
                self.listboxhold[0].insert(tk.END, thngs)
        self.listboxhold[1].selection_clear(0, tk.END)
        self.listboxhold[1].selection_set(0)
        self.update_totals_labels()
    
    #-----------------------------------------------------------------------------------       
    def button_binding_2_right(self, event):
        """ 
        
        """
        
        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[1].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[1].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[1].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[2].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[2].delete(0, tk.END)               #Delete all entries of new listbox destination
        
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            if not thngs:
                pass
            else:
                self.listboxhold[2].insert(tk.END, thngs)
        self.listboxhold[1].selection_clear(0, tk.END)
        self.listboxhold[1].selection_set(0)
        self.update_totals_labels()
    
    
    #-----------------------------------------------------------------------------------
    def button_binding_3(self, event):
        """ """

        temp_sort = []   #Will append the selected items and current entries of new column
        
        try:
            
            att = self.listboxhold[2].curselection()        #Grab selected items from listbox
            print(len(att))
            
            for i in att:
                cur_ent = self.listboxhold[2].get(i)
                #self.listboxhold[1].insert(tk.END, cur_ent)
                temp_sort.append(cur_ent)
                self.listboxhold[2].delete(i)
        
        except:
            print('failed')

        for i in self.listboxhold[1].get(0, tk.END):        #Before deleting all entries in new listbox append them to list
            temp_sort.append(i)

        self.listboxhold[1].delete(0, tk.END)               #Delete all entries of new listbox destination
        
        for thngs in sorted(temp_sort):                     #Sort the list then re-insert into new listbox
            self.listboxhold[1].insert(tk.END, thngs)

        self.listboxhold[2].selection_clear(0, tk.END)
        self.listboxhold[2].selection_set(0)
        self.update_totals_labels()
      


#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    """ """
    
    root = tk.Tk()
    Initiate(root)
    root.mainloop()
        

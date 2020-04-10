import tkinter as tk
import random as rand
import datetime as dt
import calendar as cal  
import collections as clc
import random as rand
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import sqlite3 as sql3


BG =  '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'

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

#---------------------------------------------------------------------------------------------
class Main:
    
    #---------------------------------------------------------------------------------------------
    def __init__(self, master):
        self.master = master
        self.master.config(bg = BG)
        self.master.title('Calendar View')
        
        self.frame_L = tk.Frame(self.master, bg = BG)
        self.frame_L.grid(row = 0, column = 0 , padx = 5, pady = 5)
        
        #self.lableft = tk.Label(self.frame_L, text = 'Please select\ndate -->', bg = BG, fg = FG)
        #self.lableft.grid()
        
        #ADD SCROLLBOX - This will house the type of entry we want to add
        #Ex - CUSTOMER, EVENT, TO DO, REMINDER, TRAVEL
        #Once chosen the listbox will refresh with the loaded items
        
        
        self.var = tk.StringVar()
        self.choice_sbox = tk.Spinbox(self.frame_L, values = ('Call Log', 'To Do', 'Accounts'), textvariable = self.var, 
                                      bg = BG, fg = FG)
        self.choice_sbox.grid(row = 0, padx = 5, pady = 5, sticky = tk.EW)
        self.var.set(self.choice_sbox.get())
        
        self.var.trace('w', self.load_choice_data)
        
        self.contents_lframe = tk.LabelFrame(self.frame_L, text = 'Contents', bg = BG, fg = FG, 
                                             font = 'Verdana 12 bold')
        self.contents_lframe.grid(row = 1, padx = 5, pady = 5, sticky = tk.NS)
        
        self.accounts = tk.Listbox(self.contents_lframe, bg = BG, fg = FG, height = 15, 
                                   selectbackground = DGR, selectforeground = 'black')
        self.accounts.grid(row = 0, padx = 5, pady = 5, sticky = tk.NS)
               
        #---------------------------------------------------------- CALENDER WIDGETS
        for i in customer:
            self.accounts.insert(tk.END, i)
        
        self.frame_R = tk.Frame(self.master, bg = BG)
        self.frame_R.grid(row = 0, column = 1 , padx = 25, pady = 25)
        
        self.frame_legend = tk.Frame(self.master, bg = BG)
        self.frame_legend.grid(row = 0, column = 2, padx = 5, pady = 5)
        
        tdy = dt.datetime.today()
        tdy_str = tdy.strftime('%Y %m %D').split()
        y = tdy_str[0]
        m = tdy_str[1]
        d = (tdy_str[-1].split("/"))[1]
    
        today = dt.date.today()
        mindate = dt.date(year=(int(y)-1), month=int(m), day=int(d))
        maxdate = today + dt.timedelta(days=365)
        #print(mindate, maxdate)
        
        self.cal_labelframe =tk.LabelFrame(self.frame_R, text = 'Calendar', bg = BG, fg = FG, font = 'Verdana 12 bold')
        self.cal_labelframe.grid(row = 0, padx = 10, pady = 10, sticky = tk.NSEW)
                                           
                                           
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
        
        self.cal.grid(row = 0, padx = 25, pady = 25., sticky = tk.NSEW)
        self.cal.bind('<<CalendarMonthChanged>>', self.on_change_month)
        
    
        self.addb = tk.Button(self.frame_R, text="Add Date Entry", command = self.add_date_entry, bg = BG, fg = FG)
        self.addb.grid(row = 1, padx = 5, pady = 5, sticky = tk.EW)
        
        self.viewb = tk.Button(self.frame_R, text="View Date Entries", command = self.print_sel, bg = BG, fg = FG)
        self.viewb.grid(row = 2, padx = 5, pady = 5, sticky = tk.EW)
        
        #-----------------------------------------------------------------LEGEND WIDGETS
        self.labframe = tk.LabelFrame(self.frame_legend, text = 'Calendar Legend', bg = BG, fg = FG, font = 'Verdana 12 bold')
        self.labframe.grid(row = 0, padx = 5, pady = 5)
                                      
        self.leg_red = tk.Label(self.labframe, text = 'Please select\ndate -->', bg = BG, fg = FG)
        self.leg_red.grid(row=0, column = 0, padx = 5, pady = 5)
        
        self.leg_purple = tk.Label(self.labframe, text = 'Please select\ndate -->', bg = BG, fg = FG)
        self.leg_purple.grid(row=1, column = 0, padx = 5, pady = 5)
        
        self.leg_green= tk.Label(self.labframe, text = 'Please select\ndate -->', bg = BG, fg = FG)
        self.leg_green.grid(row=2, column = 0, padx = 5, pady = 5)

        self.dentry = DateEntry(self.frame_legend, locale='en_US', date_pattern='MM/dd/yyyy')
        self.dentry.grid(row = 2, padx = 5, pady = 5)
        
        
        
    #---------------------------------------------------------------
    def on_change_month(event):
        # remove previously displayed events
        cal.calevent_remove('all')
        year, month = cal.get_displayed_month_year()
        # display the current month events 
        # ...
        print(year, month)    
    
    
    #----------------------------------------------------------------------------------------------
    def load_choice_data(self, *args):
        """ """
        self.accounts.delete(0, tk.END)
        selected = self.choice_sbox.get()
        if selected == 'Accounts':
            for i in customer:
                self.accounts.insert(tk.END, i)
        if selected == 'Call Log':
            self.accounts.insert(tk.END, selected)
        if selected == 'To Do':
            self.accounts.insert(tk.END, selected)
        return
    
    #----------------------------------------------------------------------------------------------
    def print_sel(self):
        """ """
        
        print(self.cal.selection_get())
        self.cal.see(dt.date(year=2016, month=2, day=5)) 
        
        
    #----------------------------------------------------------------------------------------------
    def add_date_entry(self):
        """" """
        
        self.topl = tk.Toplevel(bg = BG)        
        
        self.tl_entry_frame = tk.Frame(self.topl, bg = BG)
        self.tl_entry_frame.grid()
        
        date_text = self.cal.selection_get()
        acc = self.accounts.get(tk.ACTIVE)
        self.topl.title('Date Entry: {}'.format(date_text))
        
        acc_lab = tk.Label(self.topl, text = acc, font = 'Verdana 16 bold', bg = BG, fg = FG)
        acc_lab.grid(row = 0, padx = 5, pady = 10)
        
        top_lab = tk.Label(self.topl, text = "Entry for Date:\n{}".format(date_text), font = 'Verdana 12 bold', bg = BG, fg = FG)
        top_lab.grid(row = 1, padx = 5, pady = 10)
        
        topl_text = tk.Text(self.topl, bg = BG, fg = FG, width = 40, height = 10)
        topl_text.grid(row = 2, padx = 5, pady = 5)
        
        #self.cal.see(dt.date(year=2016, month=2, day=5)) 
        self.topl.mainloop()




class MyCalendar(Calendar):

    def _next_month(self):
        Calendar._next_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_month(self):
        Calendar._prev_month(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _next_year(self):
        Calendar._next_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def _prev_year(self):
        Calendar._prev_year(self)
        self.event_generate('<<CalendarMonthChanged>>')

    def get_displayed_month_year(self):
        return self._date.month, self._date.year








#---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()
    
    
    
    
    
    
    
#SCRATCH CODE ----- TK Calendar

    #top = tk.Toplevel(root)

    #cal = Calendar(top, selectmode='none')
    #date = cal.datetime.today() + cal.timedelta(days=2)
    #cal.calevent_create(date, 'Hello World', 'message')
    #cal.calevent_create(date, 'Reminder 2', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    #cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    #cal.tag_config('reminder', background='red', foreground='yellow')

    #cal.pack(fill="both", expand=True)
    #ttk.Label(top, text="Hover over the events.").pack()


#def example1():
    #def print_sel():
        #print(cal.selection_get())
        #cal.see(datetime.date(year=2016, month=2, day=5))

    #top = tk.Toplevel(root)

    #import datetime
    #today = datetime.date.today()

    #mindate = datetime.date(year=2018, month=1, day=21)
    #maxdate = today + datetime.timedelta(days=5)
    #print(mindate, maxdate)

    #cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   #mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   #cursor="hand1", year=2018, month=2, day=5)
    #cal.pack(fill="both", expand=True)
    #ttk.Button(top, text="ok", command=print_sel).pack()


#def example3():
    #top = tk.Toplevel(root)

    #ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    #cal = DateEntry(top, width=12, background='darkblue',
                    #foreground='white', borderwidth=2, year=2010)
    #cal.pack(padx=10, pady=10)


#root = tk.Tk()
#ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
#ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
#ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

#root.mainloop()

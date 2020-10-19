import calendar as cal
import collections as clc
import datetime as dt
import sqlite3 as sql3
import random as rand
import tkinter as tk
import tkcalendar as tcal


#----------------------------------------------------------------
#Development notes
devnotes = """

Filter by trigger days difference i.e. 7 days, 14 days, 1 month
    - Pull all the db items having dates within trigger range


"""
#----------------------------------------------------------------


x = cal.Calendar()
d = x.yeardatescalendar(2020)
contain = clc.OrderedDict()

itr = 1
for a in range(4):
    for k in d[a]:
        for j in k:
            for r in j:
                contain[itr] = r
                itr += 1

tod = dt.date.today()
#for k,v in contain.items():
#    print(k,v)
#    diff = abs((v-tod).days)
#    print(f"Days from today: {diff}")


#----------------------------------------------
class initiate_dates:

    #----------------------------------------------------
    def __init__(self, master):
        """ """
        self.master = master
        self.lbox = tk.Listbox(self.master, width = 55, height = 15)
        self.lbox.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.lab = tk.Label(self.master, text = 'Current trigger: 14 days').grid(row = 1, column = 0, sticky = tk.EW)
        self.dbinit()
        self.today = self.todaysdate()      #First pull todays date at this moment (This will dictate which entries in database are in need of edited days since inception as well as triggers)
        #self.additeration()                 #Each entry still not complete needs to have an additonal day added to the tally since it was input into db
        #self.checktriggeres()               #Check all differential days and trigger those that have met the threshhold
        #self.checkevents()                  #Check for events needing to be brought to users attention (calendar events, reminders, follow ups...etc)
        self.temptesting()
        self.addcalendar()

    #----------------------------------------------------
    def dbinit(self):
        """ """
        self.con = sql3.connect(":memory:")


    #----------------------------------------------------
    def todaysdate(self):
        """ """
        return dt.date.today()              #Return a datetime object for todays date. This can be used to check against the other db entries date that is stored.


    #----------------------------------------------------
    def daydifferntial(self, date1, date2):
        """ """
        if type(date1) == str:                      #Confirm both the passed dates are datetime objects such that they can be used in calcualtions
            dt1 = dt.strptime(date1, "%Y-%m-%d")
        else:
            dt1 = date1

        if type(date2) == str:                      #Confirm both the passed dates are datetime objects such that they can be used in calcualtions
            dt2 = dt.strptime(date2, "%Y-%m-%d")
        else:
            dt2 = date2

        diff = (dt1 - dt2).days             #Subtract date 1 from date 2 and call the days method to return days as INT
        return diff


    #---------------------------------------------------
    def gathertriggered(self, tod, tab, difftrig):
        """ """
        qtytrig = (tod + difftrig).days             #This will need to be a date that has been x amnt of days since input according to today
        trig_list = self.con.excute("""SELECT * FROM ? WHERE date = ?""",(tab, qtytrig))
        
        
        
    #---------------------------------------------------
    def temptesting(self):
        """ """
        randday = rand.choice(range(1,len(contain.items())))
        self.rday = contain[randday]
        self.trigcontain = clc.OrderedDict()
        self.master.title("Trigger Date: " + str(self.rday))
        trigger = 14
        
        for n,(k,v) in enumerate(contain.items()):
            #dtobj = dt.datetime.strptime(v, "%Y-%m-%d")
            diff = abs((v-self.rday).days)
            if diff <= trigger:
                print(v)
                self.lbox.insert(tk.END, f"Following date has been triggered: {v}")
                self.trigcontain[n] = v
            else:
                pass


    #---------------------------------------------------
    def addcalendar(self):
        """ """
        today = dt.date.today()
        mindate = dt.date(year=2019, month=12, day=1)
        maxdate = today + dt.timedelta(days=30)
        self.c = tcal.Calendar(self.master, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red', selectforeground = 'grey2', selectbackground = 'dark green',
                   cursor="hand1")#, year=2018, month=2, day=5)
        self.c.grid(row = 0, rowspan = 2, column = 1)
        
        self.c.tag_config('trigger', foreground = 'dark goldenrod', background = 'black')           #Config the tag 'trigger' for the triggered dates to be added to        
        for k,v in self.trigcontain.items():                                                        #Add tags to each of the triggered dates so they are color themed on tkcalendar
            self.c.calevent_create(v, f"{v}", "trigger")
        
        self.c.see(self.rday)
        self.c.selection_set(self.rday)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    initiate_dates(root)
    root.mainloop()

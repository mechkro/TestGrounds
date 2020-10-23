import calendar as cal
import collections as clc
import datetime as dt
import sqlite3 as sql3
import random as rand
import tkinter as tk
from tkinter import ttk
import tkcalendar as tcal
#from TextFarm_emails import msgfunc


#----------------------------------------------------------------
#Development notes
devnotes = """

Filter by trigger days difference i.e. 7 days, 14 days, 1 month
    - Pull all the db items having dates within trigger range


"""
#----------------------------------------------------------------


#Looking to introduce myself
salesintro = """
Hi [prospect name],

I checked out your website, and it looks like you might be trying
to [accomplish X specific goal]. Without making any assumptions 
about your business goals, I believe [Y] might play a pivotal
role in your success.

If you’re unfamiliar with [company], our solution helps businesses 
in [prospect company's] space with three main goals:

[Goal #1]
[Goal #2]
[Goal #3]
Are you free in the next few days for a call to discuss 
[prospect company's] strategy for [business area]?

Regards,
Tony K
"""

custsitevisit = """
Hi [prospect name],

I'm sending this note to introduce myself as your resource here at 
[company]. I work with small businesses in [prospect company's] space, 
and noticed that your colleagues had stopped by our website in the past.

This inspired me to spend a few minutes on your site to gain a better 
understanding of how you are [handling strategy for busines area]. 
In doing so, I noticed a few areas of opportunity and felt compelled 
to reach out to you directly.

[Company] is working with similar companies in your industry, such as X, 
helping them [accomplish Y], while providing them with the tools to [manage Z].
When do you have 15 minutes to connect today?
Please also feel free to book time directly onto my 
calendar here: [Meetings link].

Thanks,
[Your name]
"""

salesstranger = """
Hi [prospect name]

I'll keep this short and sweet to make the 26 seconds it takes to read 
this worth your time (yes, I timed it.)

As a [job title] at [company], I get to speak with people like 
you about [achieving X]. [Prospect company] is on my radar because 
we've helped a lot of companies in [X space] with [business area].

Could we schedule a 15 to 20-minute call to discuss your strategy for 
Y -- what excites you, which challenges you see, and how you envision your 
plan changing down the road? Even if you decide not to continue the conversation 
after our call, you'll leave with some advice for [business area] 
that will make an immediate impact.

Best,
[Your name]
"""

rightaftercall = """
[Name],

Saw that you were checking out [product], and wanted to give you 
a quick shout after checking out the [prospect company] site. 
The last thing I want to do is waste your time or mine, but I 
thought it would be helpful to quickly speak and learn a bit more 
about what you hope to get from [product, and share some best practices.

Most of our successful users will have a quick set up like this 
to get things started in the right direction.

Is there a good time for you today or the next few days? You can 
book some time directly on my calendar here: [Meetings link].

Best,
[Your name]

P.S. Thought you might like this as well while getting started:

[Helpful link #1]
[Helpful link #2]
"""

eventtrigger = """
Hi [prospect name],

Your [LinkedIn description, company’s recognition in the Inc. 500, 
connection with XYZ colleague] inspired me to reach out. Other 
staffing firms like A, B, and C leverage [product] to [accomplish X and Y].

Within six months of working with [company], client [saw X results]. 
I’d be happy to share a few ideas about how [prospect company] 
could accomplish the same.

If you’re open to it, when would be a convenient time to chat? 
Say, [XYZ time]?

[Your name]
"""


emailpool = [salesintro, custsitevisit, salesstranger,
            rightaftercall, eventtrigger]

x = cal.Calendar()
d = x.yeardatescalendar(2020)
contain = clc.OrderedDict()
containcount = clc.OrderedDict()

itr = 1
for a in range(4):
    for k in d[a]:
        for j in k:
            for r in j:
                contain[itr] = r
                containcount[r] = 0
                itr += 1

tod = dt.date.today()
for i,j in containcount.items():
    print(i,j)


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
        self.sboxmaker()
        self.nbookmaker()
        self.createpopmenu()


    #----------------------------------------------------
    def createpopmenu(self):
        """ 
        create a menu instance to allow user to popup menuoptions when configured event button press 
        is initiated.
        """
        
        self.menu = tk.Menu(self.master)
        for i in ('Copy', 'Edit', 'Remove', 'Tag', 'Select', 'Cancel'):
            self.menu.add_command(label=i, command = lambda: self.menucommand(i))
        self.master.bind('<2>', lambda e: self.menu.post(e.x_root, e.y_root))
        self.master.bind('<3>', self.clickedwidgetreturn)
    
    #----------------------------------------------------
    def menucommand(self, action):
        """ 
        Func is passed one of the following strings 'Copy', 'Edit', 'Remove', 'Tag', 'Select', 'Cancel'.
        Will dictate the next action
        
        **** CURRENTLY ONLY PRINTING 'cancel' ***
        """
        print(action)    
    
    
    #----------------------------------------------------
    def clickedwidgetreturn(self, event):
        """ 
        screen.update_idletasks()
        x,y = screen.winfo_rootx(), screen.winfo_rooty()
        print(screen.winfo_containing(x+5, y+5))
        """
        #event.update_idletask()
        x,y = event.x_root, event.y_root
        widge = self.master.winfo_containing(x, y)
        print(widge)
        
    #----------------------------------------------------
    def dbinit(self):
        """ """
        self.con = sql3.connect(":memory:")
        #x = msgfunc()
        for i in emailpool:
            print(i)
            

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
                print(type(v))
                self.lbox.insert(tk.END, f"Following date has been triggered: {v}")
                self.trigcontain[n] = v
                containcount[v] += 1
                
            else:
                pass
        
        #x = msgfunc()
        for i in emailpool:
            self.lbox.insert(tk.END, i)
        print(containcount.values())


    #---------------------------------------------------
    def addcalendar(self):
        """ """
        today = dt.date.today()
        mindate = dt.date(year=2019, month=12, day=1)
        maxdate = today + dt.timedelta(days=30)
        self.c = tcal.Calendar(self.master, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red', selectforeground = 'white', selectbackground = 'dark green',
                   cursor="hand1")#, year=2018, month=2, day=5)
        self.c.grid(row = 0, rowspan = 2, column = 1, padx = 15, pady = 5)
        self.c.bind("<<CalendarSelected>>", self.peekentries)
        
        self.c.tag_config('trigger', foreground = 'dark goldenrod', background = 'black')           #Config the tag 'trigger' for the triggered dates to be added to        
        #for k,v in self.trigcontain.items():                                                        #Add tags to each of the triggered dates so they are color themed on tkcalendar
        #    txt = rand.choice(emailpool)
        #    self.c.calevent_create(v, f"{txt}", "trigger")
        for k,v in containcount.items():
            self.c.calevent_create(k, f"Total Entries: {v}", "trigger")
        self.c.see(self.rday)
        self.c.selection_set(self.rday)
        
        self.peeklab = tk.Label(self.master, text = " ")
        self.peeklab.grid(row = 3, column = 0, columnspan = 2, sticky = tk.EW)
    
    
    #--------------------------------------------------
    def peekentries(self, event):
        """ """
        datsel = event.widget.selection_get()
        print(datsel)
        print(type(datsel))
        for k,v in self.trigcontain.items():
            if v != datsel:
                pass
            else:
                print(k,v)
                rtxt = rand.choice(emailpool)
                #self.peeklab.config(text = f"Entries include: {rtxt}")
                self.tbox1.delete(1.0, tk.END)
                self.tbox1.insert(tk.END, rtxt)
                
    
    
    #---------------------------------------------------
    def sboxmaker(self):
        """ 
        
        """
        
        self.cbox = ttk.Combobox(self.master, values = [dt.datetime.strftime(i, "%Y-%m-%d") for i in contain.values()])
        self.cbox.grid(row = 2, column = 0, columnspan = 2, pady = 10, sticky = tk.EW)
        self.cbox.bind("<<ComboboxSelected>>", self.cboxevent)
        
        for i in range(55):
            pass


    #---------------------------------------------------
    def cboxevent(self, event):
        """ 
        triggered due to combobox selection change. 
        Intended use:
            - Flip calendar to show the selected date so it is visible in the appropriate month of the selection
            - 
        """
        
        cur = self.cbox.get()
        csplit = cur.split('-')
        self.c.see(dt.datetime.strptime(cur, "%Y-%m-%d"))
        self.c.selection_set(dt.datetime.strptime(cur, "%Y-%m-%d"))
        #dt.datetime.date


    #---------------------------------------------------
    def nbookmaker(self):
        """ 
        Notebook widget maker. Make tabs for each of the areas I track for sales i.e. - call logs, accounts, projects, reminders, ...etc
        """
        self.nbook = ttk.Notebook(self.master)
        self.t1 = ttk.Frame(self.nbook)
        self.t2 = ttk.Frame(self.nbook)
        self.t3 = ttk.Frame(self.nbook)
        self.t4 = ttk.Frame(self.nbook)
        self.t5 = ttk.Frame(self.nbook)
        self.t6 = ttk.Frame(self.nbook)
        self.nbook.add(self.t1, text ='CALL LOG')
        self.nbook.add(self.t2, text ='PROJECTS')
        self.nbook.add(self.t3, text ='TO DO')
        self.nbook.add(self.t4, text ='ACCOUNTS')
        self.nbook.add(self.t5, text ='VENDORS')
        self.nbook.add(self.t6, text ='FOLLOW UPS')
        self.nbook.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tk.NSEW)
        
        self.addbutt = tk.Button(self.master, text = 'ADD', command = lambda: None)
        self.addbutt.grid(row = 5, sticky = tk.EW)
        
        self.add_widgets_notebook()             #Make call to add widgets to each of the frames for the notebook
        self.tboxcontain = [(self.t1,self.tbox1),
                            (self.t2,self.tbox2),
                            (self.t4,self.tbox4),
                            (self.t5,self.tbox5),
                            (self.t6,self.tbox6)]
                            #(self.t3,self.tbox3),
        for i in self.tboxcontain:
            self.add_scrollbars(i[0],i[1])
        
        #BUTTON WIDGET-------------------
        self.addbutt = tk.Button(self.master, text = 'ADD', command = lambda: None)
        self.addbutt.grid(row = 5, sticky = tk.EW)
        
        self.t3frame_func()
    
    #--------------------------------------------------
    def add_widgets_notebook(self):
        """ 
        create the text widgets inside of each frame in the notebook.
        """
        
        self.tbox1 = tk.Text(self.t1, height = 6)
        self.tbox2 = tk.Text(self.t2, height = 6)
        #self.tbox3 = tk.Text(self.t3)
        self.tbox4 = tk.Text(self.t4, height = 6)
        self.tbox5 = tk.Text(self.t5, height = 6)
        self.tbox6 = tk.Text(self.t6, height = 6)
        
        self.tbox1.grid(padx = 5, pady = 5, row = 0, column = 0)
        self.tbox2.grid(padx = 5, pady = 5, row = 0, column = 0)
        #self.tbox3.grid(padx = 5, pady = 5, row = 0, column = 0)
        self.tbox4.grid(padx = 5, pady = 5, row = 0, column = 0)
        self.tbox5.grid(padx = 5, pady = 5, row = 0, column = 0)
        self.tbox6.grid(padx = 5, pady = 5, row = 0, column = 0)
        
        return


    #--------------------------------------------------
    def add_scrollbars(self, frm, tbox):
        """ 
        create the scrollbars for each of the text box in notebook
        self.scroll1 = tk.Scrollbar(self.t1, orient = tk.VERTICAL)
        self.scroll1.grid(row = 0, column = 1, sticky = tk.NS)
        self.tbox1.config(yscrollcommand = self.scroll1.set)
        self.scroll1.config(command = self.tbox1.yview)
        """
        scroll = tk.Scrollbar(frm, orient = tk.VERTICAL)
        scroll.grid(row = 0, column = 1, sticky = tk.NS)
        tbox.config(yscrollcommand = scroll.set)
        scroll.config(command = tbox.yview)
        
        return
        
    #--------------------------------------------------
    def t3frame_func(self):
        """ 
        To-do tab of the notebook
        """
        
        #FRAMES --------------------------------
        self.fleft = tk.Frame(self.t3)
        self.fmid = tk.Frame(self.t3)
        self.fright = tk.Frame(self.t3)
        
        self.fleft.grid(row = 0, column = 0)
        self.fmid.grid(row = 0, column = 1)
        self.fright.grid(row = 0, column = 2)
        
        #LISTBOXES ----------------------------
        self.lbox_left = tk.Listbox(self.fleft, height = 5)
        self.lbox_left.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.lbox_mid = tk.Listbox(self.fmid, height = 5)
        self.lbox_mid.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.lbox_right = tk.Listbox(self.fright, height  = 5)
        self.lbox_right.grid(row = 1, column = 2, padx = 5, pady = 5)
        
        #FUNCTIONALITY BUTTONS
        #------------------------------------------------ Column 1 - Buttons
        self.butt_fwd_col1 = tk.Button(self.fleft, text = '>', command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col1.grid(row = 3, column = 0, pady = 2, sticky = tk.EW)
        self.butt_fwd_col1.bind('<Button-1>', None)
        self.butt_fwd_col1_2 = tk.Button(self.fleft, text = 'Add NEW',  command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col1_2.grid(row = 4, column = 0, pady = 2, sticky = tk.EW)
          
        #------------------------------------------------ Column 2 - Buttons
        self.butt_fwd_col2_left = tk.Button(self.fmid, text = '<', command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col2_left.grid(row = 3, column = 1, pady = 2, sticky = tk.EW)
        self.butt_fwd_col2_left.bind('<Button-1>', None)
        self.butt_fwd_col2_right = tk.Button(self.fmid, text = '>', command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col2_right.grid(row = 4, column = 1, pady = 2, sticky = tk.EW)
        self.butt_fwd_col2_right.bind('<Button-1>', None)        
        
        #------------------------------------------------ Column 3 - Buttons
        self.butt_fwd_col3 = tk.Button(self.fright, text = '<', command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col3.grid(row = 3, column = 2, pady = 2, sticky = tk.EW)
        self.butt_fwd_col3.bind('<Button-1>', None)
        self.butt_fwd_col3_2 = tk.Button(self.fright, text = 'Change FG', command = lambda: None, font = ('Vardana',10,'bold'))
        self.butt_fwd_col3_2.grid(row = 4, column = 2, pady = 2, sticky = tk.EW)  
    

#------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    initiate_dates(root)
    root.mainloop()

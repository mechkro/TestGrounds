import tkinter as tk
import calendar
import datetime as dt


"""
USE Cases:

- Want to have the year broken down by months.
- There will be 12 databses for any given year (each month)
- Then each day will be able to add notes or to dos for each of the days of the month

"""

#We will use 12 month dictionaries to be able to store up to 365 different days and entries for
#each day.

jan = {}
feb = {}
mar = {}
apr = {}
may = {}
jun = {}
jul = {}
aug = {}
sep = {}
octo = {}
nov = {}
dec = {}

Month_Holdr = {
    1:jan,
    2:feb,
    3:mar,
    4:apr,
    5:may,
    6:jun,
    7:jul,
    8:aug,
    9:sep,
    10:octo,
    11:nov,
    12:dec 
                       }


#---------------------------------------------------------------------------------------
class Main:
    
    cur_month = None
    cur_year = None
    
    #---------------------------------------------------------------------------------------
    def __init__(self, master):
        self.master = master
        self.master.title('Calendar')
        
        self.f = tk.Frame(self.master)
        self.f.grid()
        
        self.lab1 = tk.Label(self.f, text = 'Year')
        self.lab1.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.lab2 = tk.Label(self.f, text = 'month')
        self.lab2.grid(row = 1, column = 0,  padx = 5, pady = 5)
        
        self.e1 = tk.Entry(self.f)
        self.e1.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        self.e2 = tk.Entry(self.f)
        self.e2.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        self.b1 = tk.Button(self.f, text = 'Go', command = lambda: self.popcalendar())
        self.b1.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.EW)
        
    
    #---------------------------------------------------------------------------------------
    def popcalendar(self):
        """ """
        
        self.tl = tk.Toplevel()
        
        self.days = {'m':{},
                            't':{},
                            'w':{},
                            'th':{},
                            'f':{},
                            'sa':{},
                            'su':{}} 
        
        Main.cur_year = self.e1.get()
        Main.cur_month = self.e2.get()
        
        self.year = int(Main.cur_year)
        self.month = int(Main.cur_month)
        
        if 0 < self.month < 13:
            weeks = 1
            itr = 0
            
            for i in calendar.monthcalendar(self.year, self.month):#int(today_str[0]), int(today_str[1])):
                for d in self.days.keys():
                    self.days[d][weeks] = i[itr]
                    itr+=1
                weeks += 1
                itr = 0      
            
            
            self.tl.title(calendar.month_name[self.month])
            
            self.prev_month = tk.Button(self.tl, text = '<--', command =  lambda: self.prev_month_render(Main.cur_month, Main.cur_year))
            self.prev_month.grid(row = 0, column = 0, padx = 5, pady = 5)
            
            self.next_month = tk.Button(self.tl, text = '-->', command = lambda: self.next_month_render(Main.cur_month, Main.cur_year))
            self.next_month.grid(row = 0, column = 6, padx = 5, pady = 5)            
            
            for n,k in enumerate(self.days.keys()):
                tk.Label(self.tl, text = '{}'.format(k.upper()), font = ('Verdana', 10, 'bold')).grid(row = 1, column = n, padx = 2, pady = 2)
                
            m = list(self.days['m'].values())
            m_layout = ((2,0), (3,0), (4,0), (5,0), (6,0),( 7,0),(8,0))
            self.place_button(self.tl, m, m_layout)
            
            t = list(self.days['t'].values())
            t_layout = ((2,1), (3,1), (4,1), (5,1), (6,1), (7,1),(8,1))
            self.place_button(self.tl, t, t_layout)
            
            w = list(self.days['w'].values())
            w_layout = ((2,2), (3,2), (4,2), (5,2), (6,2), (7,2),(8,2))
            self.place_button(self.tl, w,  w_layout)
            
            th = list(self.days['th'].values())
            th_layout = ((2,3), (3,3), (4,3), (5,3), (6,3), (7,3),(8,3))
            self.place_button(self.tl, th, th_layout)
            
            f = list(self.days['f'].values())
            f_layout = ((2,4), (3,4), (4,4), (5,4), (6,4), (7,4),(8,4))
            self.place_button(self.tl, f, f_layout)
            
            sa = list(self.days['sa'].values())
            sa_layout = ((2,5), (3,5), (4,5), (5,5), (6,5), (7,5),(8,5))
            self.place_button(self.tl, sa, sa_layout)
            
            su = list(self.days['su'].values())
            su_layout = ((2,6), (3,6), (4,6), (5,6), (6,6), (7,6),(8,6))
            self.place_button(self.tl, su, su_layout)     
        
        else:
            print('Error - month needs to be 1 - 12')
            self.tl.destroy()
            
        self.tl.mainloop()
        
        
    #---------------------------------------------------------------------------------------
    def refresh_calendar(self, p, dlst, coords):
        """ """
        for widge in self.tl.winfo_children:
            widge.destroy()
            
            

    #---------------------------------------------------------------------------------------
    def place_button(self, p, dlst, coords):
        """ """
        itr = 0
        button_count = 0        #This is used to track and give key to button that is stored in dictionary
        
        for i in coords:
            try:
                if dlst[itr] == 0:
                    t = tk.Button(p, text = ' -  ', state = tk.DISABLED,  cursor = ' hand2' )
                    t.grid(row = i[0], column = i[-1], padx = 2, pady = 2)
                    #t.bind('<Enter>', lambda: change_color(t))
                    
                else:
                    t = tk.Button(p, text = '{}'.format(dlst[itr]), cursor = 'hand2', font = ('Verdana', 10, 'bold'))
                    t.grid(row = i[0], column = i[-1], padx = 2, pady = 2)
                    
                    
                    #t.bind('<Enter>', lambda: change_color_def(t))
                    
                itr += 1
                
            except Exception as e:
                pass 
    
        return
    
    
    #---------------------------------------------------------------------------------------
    def prev_month_render(self, m, y):
        """ """
        if int(m) == 1:
            newyear = int(Main.cur_year) - 1
            Main.cur_year = newyear
            Main.cur_month = 12
        
        else:
            newmonth = int(Main.cur_month) - 1
            Main.cur_month = newmonth
            
        print(Main.cur_month)
        print(Main.cur_year)
        
    
    #---------------------------------------------------------------------------------------
    def next_month_render(self, m, y):
        """ """
        if m == 12:
            selfyear += 1
            self.month = 1
            Main.cur_year = self.year
            Main.cur_month = self.month
        else:
            pass
    
    
    
        
#---------------------------------------------------------------------------------------
if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()


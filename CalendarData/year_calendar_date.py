import tkinter as tk
import calendar as cal
import sqlite3 as sq

BG = '#0C1021'
FG = 'white'



############################################
def month_layout(yr, m):
    """ """
    refr = cal.monthcalendar(yr,m)
    dhold = {'m':[],'t':[], 'w':[], 'th':[], 'f':[], 'sa':[], 'su':[]}

    for i in refr:
        dhold['m'].append(i[0])
        dhold['t'].append(i[1])
        dhold['w'].append(i[2])
        dhold['th'].append(i[3])
        dhold['f'].append(i[4])
        dhold['sa'].append(i[5])
        dhold['su'].append(i[6])

    for k,v in dhold.items():
        print(k)
        for i in v:
            print(i)
        print('\n\n')

############################################



#----------------------------------------------------------
def create_db(fname):
    """

    """
    
    fdir = '{}.db'.format(fname)
    curr = sq.connect(':memory:')  #Normally put fdir in there with file directory
    

#----------------------------------------------------------
def create_table():
    """

    """
    
    global curr
    create_table = """CREATE TABLE IF NOT EXISTS days (
                  id integer PRIMARY KEY,
                  time TEXT,
                  note TEXT)
                  """
    curr.execute(create_table)
    curr.commit()

#----------------------------------------------------------
def insert_into_db(*args):
    """
    product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
        >>> cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
        >>> cur.execute(product_sql, ('A Guide to Writing Short Stories', 17.99))
        >>> cur.execute(product_sql, ('Data Structures and Algorithms', 11.99))
        >>> cur.execute(product_sql, ('Advanced Set Theory', 16.99))
    """
    
    ans = tuple([i for i in args])
    ans_sql = "INSERT INTO days (id)"
    

#----------------------------------------------------------
def assign_days_key(yr):
    """
    #should output >>> (('1','1/1/(yr)'), .... ('31','1/31/(yr)'),('32','2/1/(yr)'))

    We want to be able to assign each day of the year to a callable ID (primary key) in entry
    """
    
    total_days = tuple([i for i in range(1,366)])
    dist_keys = zip(map(None, None))                    #should output >>> (('1','1/1/(yr)'), .... ('31','1/31/(yr)'),('32','2/1/(yr)'))


#----------------------------------------------------------
def year_selected(yr):
    """

    """
    
    s.delete(1.0, tk.END)
    k = cal.calendar(int(yr))
    month_layout(int(yr),3)
    
    for i in k.split(','):
        s.insert(tk.END, """{}""".format(i))
    root.title('Current Year: {}'.format(yr))
    
    return


#----------------------------------------------------------
def get_selected(w):
    """

    """
    print('clicked {}'.format(w.index(tk.CURRENT)))

    
    z = w.index(tk.CURRENT)
    y = z.split('.')
    yy = y[0]

    zz = list(range(0,int(yy)))
    zzz = [i+1 for i in zz]
    print(zzz)
    
    g = float(z)
    for i in zzz:
        #add1 = int(yy) + 1
        astrg = "{}.{}".format(i,y[-1])
        print(w.get('{} + 1 lines'.format(astrg)))
        print(astrg)
        a = w.get(astrg)
        w.tag_add('highlightline', astrg)
        w.tag_configure('highlightline', background = 'yellow')#, foreground = 'yellow')
        print(a)
        
    
    #print(w.get(z))
    #print(w.get(z, tk.END))


    print(w.get(yy+'.0', yy+'.end'))
    print(w.get(z + ' lineend'))
    
    if s.tag_ranges(tk.SEL):        
        st = s.get(tk.SEL_FIRST, tk.SEL_LAST)
        print(st)
        
        try:
            stsplit = st.split()
            if len(stsplit) > 1:
                print('too many')
                print([i for i in stsplit])
            else:
                print([i for i in stsplit])
                
        except Exception as e:
            print(e)
            
    else:
        print('No text selected')
    


root = tk.Tk()
root.config(bg = BG)

yearpick = tk.Spinbox(root, values = ([i for i in range(1900,2100)]), bg = BG, fg = FG)
yearpick.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5, sticky = tk.EW)


txtscroll = tk.Scrollbar(root)
txtscroll.grid(row = 1, rowspan = 2, column = 1, sticky = tk.NS)

s = tk.Text(root, highlightbackground = 'yellow',yscrollcommand = txtscroll.set,
            bg = BG, fg = FG, relief = tk.RAISED)
s.grid(row = 1, rowspan = 2, column = 0,padx = 8, pady = 8)
txtscroll.config(command = s.yview)


getbutt = tk.Button(root, text = 'Fetch Calendar', cursor = 'hand2', bg = BG, fg = FG,
                    command = lambda: year_selected(yearpick.get()))
getbutt.grid(row = 1, column = 2, padx = 5, pady = 5)

getsel = tk.Button(root, text = 'Get Highlighted', cursor = 'hand2',
                   command = lambda: get_selected(s), bg = BG, fg = FG)    #s.index(tk.CURRENT)
getsel.grid(row = 2, column =2, padx = 5, pady = 5)


#s.bind('<<Selection>>', get_selected)
#s.bind('<TextSel>', None)
root.mainloop()

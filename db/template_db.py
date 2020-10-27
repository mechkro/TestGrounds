import random as rand
import collections as clc
import sqlite3 as sql3
import calendar as cal
import datetime as dt



sqlobj = r"C:\Users\kinse\Desktop\DXP_app\dbtemp.db"
con = sql3.connect(sqlobj)

subchoice = {"T":"Todo",
            "C":"Call Log",
            "P":"Project",
            "A":"Account",
            "I":"Internal",
            "V":"Vendor",
            "F":"Follow Up",
            "R":"Reminder",
            "E":"Emergency",
            "Q":"Quote",
            "X":"Calendar Event"}

subinternal = {"U":"Urgent",
               "L":"Low Priority",
               "H":"High Priority",
               "N":"N/A",
               "O":"Overdue",
               "F":"Follow up contest"}


template = """
CALL LOG:
----------------------------------
TO DO:
----------------------------------
ACCOUNTS: 
----------------------------------
PROJECTS:
----------------------------------
QUOTES:
==================================
###XY01-TEST COMMENT 1
###XY02-TEST COMMENT 2
###XY03-TEST COMMENT 3
###XY04-TEST COMMENT 4
"""


#NEED TO:
#X - is refers to the subjuct above

#Y - subject specific code


parsenotes = """
Split order:
    - (=) Equal sign
    - Now 2 list:
        Subjects List:
            - split (-)
        Command Entry:
            - Capture all lines startimng with #
            - Split @ (-)
            - Now 2 new list
                Code list:
                    - subject [0]
                    - subject specific code [1]
                    - same type comment order # [2:3]
                Comment:
                    - string 
"""

#-----------------------------------------
def parse_return_days():
    """ 
    
    """
    
    dates_cal = {}
    c = cal.Calendar()
    clist = c.yeardatescalendar(2020)
    
    return clist


def dbtable(x):
    """
    
    """
    d = dt.datetime.today()
    for i in x:
        cur = con.cursor()
        cur.execute("""INSERT INTO days VALUES (NOTE = ?, DATEENT = ?)""",(template,d))
        con.commit()
        cur.close()
    return
    



dcontain = parse_return_days()
dc = []
for n,i in enumerate(dcontain):
    for j in i:
        for k in j:
            for h in k:
                dc.append(h)
                print(h)
 
print(dc)               
#dbtable(dc)


#-----------------------------------------
def entryparser(triplestr):
    """
        Split order:
            - (=) Equal sign
            - Now 2 list:
                Subjects List:
                    - split (-)
                Command Entry:
                    - Capture all lines startimng with #
                    - Split @ (-)
                    - Now 2 new list
                        Code list:
                            - subject [0]
                            - subject specific code [1]
                            - same type comment order # [2:3]
                        Comment:
                            - string 
    """
    subcomm_list = triplestr.split("==================================")
    
    
    #SUBJECTS SECTION ----------------------
    itr = 0
    subj_list = subcomm_list[0].split("----------------------------------")
    
    for i in subj_list:
        itr += 1
        print(itr)
        print(i)
    
    #COMMAND ENTRY SECTION -----------------
    comm_list = subcomm_list[1]
    clist_split = comm_list.split('\n')
    contnr = {}
    
    for i in clist_split:
        
        itr += 1
        print(itr)
        print(i)
        
        if "###" in i[:]:
            
            splt = i.split("-")
            contnr[itr] = [splt[0], splt[1]]
            print(i)
            
        else:
            pass
    
    
    #-------------------------------------Nested
    def codeparse(s):
        """ """
        
        deltable = s[0:3]
        subcode = s[3]
        ssubcode = s[4]
        commitr = s[-2:-1]
        return (deltable, subcode, ssubcode, commitr)
    
    
    #-------------------------------------Nested
    def swapout_testing(lst):
        """ """
        
        a,b,c,d = lst
        swapr = rand.choice([i for i in subchoice.keys()])
        return (a,swapr,c,d)
    
    
    #-------------------------------------Nested
    def swapout_internal(lst):
        """ """
        
        a,b,c,d = lst
        swapr = rand.choice([i for i in subinternal.keys()])
        return (a,b,swapr,d)    



    codes = {}    #Containers to house the split list for codes and comments    
    comms = {}
    
    for n, (k,v) in enumerate(contnr.items()):

        codes[n] = codeparse(v[0])
        print(f"Original: {codes[n]}")
        
        tst = swapout_testing(codes[n])         #Function call to swap out value for test purposes
        tst2 = swapout_internal(tst)            #Function call to swap out value for test purposes
    
        for n,i in enumerate(tst2):
            
            if n == 0:
                pass
            
            if n == 1:
                print('\n',i)
                print(subchoice[i])
                
            if n == 2:
                print('\n',i)
                print(subinternal[i])
                
            if n == 3:
                print('\n',i)
            
        print(f"Swapped: {tst2}")
        
        comms[n] = v[1]
        print(comms[n])



    #--------------------------------------------
    def print_summary(subs, c1, c2, c3, c4):
        """ 
        
        """
        
        for n,i in subs:
            print(f"Subject {n}: \n{i}")
        
        for j in [c1,c2,c3,c4]:
            print(f"{j[0]}: {j[-1]}")
    
    
    
    
    
#START -----------------------
entryparser(template)

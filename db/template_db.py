import random as rand
import collections as clc

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
    #SUBJECTS SECTION ---
    itr = 0
    subj_list = subcomm_list[0].split("----------------------------------")
    for i in subj_list:
        itr += 1
        print(itr)
        print(i)
    
    #COMMAND ENTRY SECTION ---
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
    
    def codeparse(s):
        deltable = s[0:3]
        subcode = s[3]
        ssubcode = s[4]
        commitr = s[-2:-1]
        return (deltable, subcode, ssubcode, commitr)
        
    def swapout_testing(lst):
        a,b,c,d = lst
        #k = subchoice.keys()
        swapr = rand.choice([i for i in subchoice.keys()])
        return (a,swapr,c,d)



        
    codes = {}
    comms = {}
    for n, (k,v) in enumerate(contnr.items()):
        codes[n] = codeparse(v[0])
        print(codes[n])
        tst = swapout_testing(codes[n])
        print(tst)
        comms[n] = v[1]
        print(comms[n])
        
    
        
        
        
        
        
        
        
    
entryparser(template)

import random
import collections as clc



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



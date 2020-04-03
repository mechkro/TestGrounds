import tkinter as tk
import widgemaker as wmaker


BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'

#-------------------------------------------------------------
def print_test():
    """ """
    print('Test Worked!')


root = tk.Tk()
root.config(bg = BG)
root.title('Main Window')

f = tk.Frame(root, bg = BG)
f.grid()

l = wmaker.Widget_Maker('LABEL', f, *('test', BG, FG, ('Verdana',24,'bold'), [0,1,0,1,5,5,tk.EW]))
l2 = wmaker.Widget_Maker('LABEL', f, *('Line 1', BG, FG, ('Verdana',24,'bold'), [1,1,0,1,5,5,tk.EW]))
l3 = wmaker.Widget_Maker('LABEL', f, *('Line 2', BG, FG, ('Verdana',24,'bold'), [2,1,0,1,5,5,tk.EW]))
l4 = wmaker.Widget_Maker('LABEL', f, *('Line 3', BG, FG, ('Verdana',24,'bold'), [3,1,0,1,5,5,tk.EW]))

b = wmaker.Widget_Maker('BUTTON', f, *('Button', BG, FG, ('Verdana',24,'bold'), lambda: print_test(), [4,1,0,1,5,5, 'ew']))



root.mainloop()

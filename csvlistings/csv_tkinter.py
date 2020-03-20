import tkinter as tk



class Main(object):
    def __init__(self, master):
        self.master = master

        self.f = tk.Frame(self.master)
        self.f.grid()

        grid_layout = [(0,1),(0,2),(0,3),
                       (1,1),(1,2),(1,3),
                       (2,1),(2,2),(2,3),
                       (3,1),(3,2),(3,3),
                       (4,1),(4,2),(4,3),
                       (5,1),(5,2),(5,3),
                       (6,1),(6,2),(6,3)]

        holdr = {}
        for x,i in enumerate(grid_layout):
            holdr[x] = self.make_lbox(i[-1], i[0])

        for v in holdr.values():
            v.bind('<Enter>', self.change_clr)
            v.bind('<Leave>', self.clr_def)

        self.bot_txt = tk.Text(self.f, height = 7, bg = 'black', fg = 'white')
        self.bot_txt.grid(row = 4, column = 0, columnspan = 7, padx = 3, pady = 3, sticky = tk.EW)
        

    def make_lbox(self, r, c):
        lb = tk.Listbox(self.f, bg = 'black', fg = 'white')
        lb.grid(row = r, column = c, padx = 3, pady = 3)
        lb.insert(tk.END, 'Row = {}\nCol = {}'.format(r,c))
        return lb

##        tk.Listbox.bind('<Enter>', self.change_clr)
##        tk.Listbox.bind('<Leave>', self.clr_def)
##        return 

    def change_clr(self, event):
        event.widget.config(bg = 'dark goldenrod')
        return

    def clr_def(self, event):
        event.widget.config(bg = 'black')
        return

    
    



if __name__ == '__main__':
    root = tk.Tk()
    Main(root)
    root.mainloop()


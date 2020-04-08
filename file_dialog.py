# -*- coding: utf-8 -*-
"""
Created on Sat Oct 06 00:30:36 2018

@author: Tony
"""

#DXP Testing Ground

from Tkinter import *
import tkFileDialog as tkf
import os


BG = '#0C1021'
FG = 'white'

class Main:
    
    current = None    
    locz = None
    
    def __init__(self,frame):
        """ """
        
        self.frame = frame
        self.frame.config(bg = BG)
        
        self.blab = Label(self.frame, text = 'Enter Folder\nThen click Button', bg = BG, fg = FG)
        self.blab.pack(side = TOP, padx = 5, pady = 5)
        
        self.foldername = Entry(self.frame, bg = BG, fg = FG)
        self.foldername.pack(padx = 5, pady = 5)
        
        self.dialogbut = Button(self.frame,
                                text = 'Choose\nDirectory',
                                cursor = 'cross', bg = BG, fg = FG,
                                command = lambda: self.test_entry())
        self.dialogbut.pack(side = BOTTOM, fill = BOTH, padx = 5, pady = 5)
    
    def test_entry(self):
        """ """
        chk = self.foldername.get()
        if chk:
            self.IntDir()
        else:
            return
    
    def IntDir(self):
        """ """
        
        self.foldrselect = tkf.askdirectory()
        self.create_directory(self.foldrselect)
        Main.current = self.foldrselect
        print Main.current
        self.NewScreen1()
    
    def create_directory(self, floc):
        self.combo = '{}/{}'.format(floc,self.foldername.get())
        try:
            os.mkdir(self.combo)
        except FileExistsError:
            print('error')
        
        return
    
    def NewScreen1(self):
        """ """
        
        self.tf = Toplevel(bg = BG)
        self.tflabel = Label(self.tf, bg = BG, fg = FG,
                             text = "See Below:\nSelect which subfolders you would\nlike to create")
        self.tflabel.pack(side = TOP)
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        
        self.containr = (self.var1,self.var2,self.var3,self.var4,self.var5)
        
        self.c1 = Checkbutton(self.tf, text="Emails", variable=self.var1, bg = BG, fg = FG)
        self.c1.pack()
        self.c2 = Checkbutton(self.tf, text="PO_OA", variable=self.var2, bg = BG, fg = FG)
        self.c2.pack()
        self.c3 = Checkbutton(self.tf, text="Costing", variable=self.var3, bg = BG, fg = FG)
        self.c3.pack()
        self.c4 = Checkbutton(self.tf, text="Project Pics", variable=self.var4, bg = BG, fg = FG)
        self.c4.pack()
        self.c5 = Checkbutton(self.tf, text="Vendor Folder", variable=self.var5, bg = BG, fg = FG)
        self.c5.pack()        
        self.OkBut = Button(self.tf,
                            text = 'Next', bg = BG, fg = FG,
                            command = lambda: self.NewScreen2())      #[i for i in self.containr if i != 0]))
        self.OkBut.pack(side = BOTTOM)        
        self.tf.mainloop()
    
    def NewScreen2(self):
        """ """
        
        selections = [i.get() for i in self.containr if i == 0]
        colect = {}
        for n,i in enumerate(self.containr):
            if i.get() == 0:
                pass
            else:
                print 'You have choosen the following options:\n'
                if i == self.var1:
                    print "Emails"
                    colect[n] = 'Emails'
                elif i == self.var2:
                    print "PO_OA"
                    colect[n] = "PO_OA"
                elif i == self.var3:
                    print "Costing"
                    colect[n] =  "Costing"
                elif i == self.var4:
                    print "Project Pics"
                    colect[n] = "Project Pics"
                elif i == self.var5:
                    print "Vendor Folder"
                    colect[n] = "Vendor Folder"
                else:
                    pass
        self.make_sub_dir(colect)
        
        
                
    def make_sub_dir(self, d):
        """ """
        for k,v in d.items():
            try:
                sub = '{}/{}'.format(self.combo, v)
                os.mkdir(sub)
            except FileExistsError:
                print('Sub Folder Error')
            
        return
        
            
    def Dialogger(self):
        """ """
        
        askr = tkf.askopenfilename(parent=root, initialdir="/", title='Please select a directory')
        print askr
        return

if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()






from src.tk_menu import  *
from tkinter import *
import tkinter.constants

root = create_root(size='600x600')

class LabEnt(object):
    def __init__(self,parent,cnf={}):
        """
        label and entry combination
        :param cnf:
        1. parent
        2. label config: labtxt
        3. row
        5. column
        """

        if parent is None:
            raise Exception('must give parent widget')

        labtxt='label'
        if 'labtxt' in cnf.keys():
            labtxt = cnf['labtxt']

        irow=0
        if 'row' in cnf.keys():
            irow=cnf['row']
        icolumn=0
        if 'column' in cnf.keys():
            icolumn=cnf['column']

        lab = Label(parent, text=labtxt)
        self.ent = Entry(parent)

        lab.grid(row=int(irow),column=int(icolumn),padx=10,pady=10)
        self.ent.grid(row=int(irow),column=int(icolumn)+1,padx=10,pady=10)

    def get(self):
        return self.ent.get()


def create_widgets():

   frame = Frame(root,borderwidth=2,relief=RIDGE)
   le_sku = LabEnt(frame, cnf={'labtxt':'sku编号','row':'0','column':'0'})
   le_ord = LabEnt(frame, cnf={'labtxt': '订单编号', 'row': '0', 'column': '2'})
   le_sku2 = LabEnt(frame, cnf={'labtxt':'sku编号','row':'1','column':'0'})
   le_ord2 = LabEnt(frame, cnf={'labtxt': '订单编号', 'row': '1', 'column': '2'})
   le_sku3 = LabEnt(frame, cnf={'labtxt':'sku编号','row':'2','column':'0'})
   le_ord3 = LabEnt(frame, cnf={'labtxt': '订单编号', 'row': '2', 'column': '2'})
   frame.pack(fill=BOTH)


'test'

if __name__ == '__main__':

    m = CMenu(root)
    m.create_menu()

    Label(root, text='PRD仿真配置界面',pady=10).pack()

    create_widgets()

    root.mainloop()

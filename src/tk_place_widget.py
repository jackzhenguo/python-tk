from tkinter import *
from src.tk_multi_widgets import *


def rb_select():
    print('you selected option:' + str(var.get()))

var = IntVar()

def place_widgets():

   frame = Frame(root,borderwidth=2,relief=RIDGE)

   xbeg=1
   ybeg,ydelt = 10,50

   Label(frame,text='sku').place(x=xbeg,y=ybeg)
   sku_val = Entry(frame)
   sku_val.place(x=40+xbeg,y=ybeg)

   Label(frame,text='订单编号').place(x=280+xbeg,y=ybeg)
   ord_val = Entry(frame)
   ord_val.place(x=360+xbeg,y=ybeg)

   pw = PanedWindow(frame,relief=FLAT)
   lb = Label(pw,text = '求解方法',bg='yellow')
   pw.add(lb)

   rb1 = Radiobutton(pw, text='最优化法', variable=var, value=1, command=rb_select)
   pw.add(rb1)
   rb2 = Radiobutton(pw, text='仿真法', variable=var, value=2, command=rb_select)
   pw.add(rb2)
   pw.place(x=xbeg,y=ydelt+ybeg)

   frame.pack(fill=BOTH,expand=1)


'test'

if __name__ == '__main__':

    m = CMenu(root)
    m.create_menu()

    Label(root, text='PRD仿真配置界面',pady=10).pack()

    place_widgets()

    root.mainloop()

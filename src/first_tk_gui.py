from tkinter import *


root=Tk() #

root.title('first tk gui') #根窗口的标题

root.geometry('500x200') #根窗口的大小

#Label实例
x = Label(root,
          text='Hello',
          bg='green',
          font=('Arial',12),
          width=15,
          height=2)
#布局
x.pack()
#消息循环
x.mainloop()


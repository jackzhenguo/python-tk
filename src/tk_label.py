from tkinter import *


root=Tk() #

root.title('tk using label') #根窗口的标题

root.geometry('500x200') #根窗口的大小

#以下为label的属性
"""
 STANDARD OPTIONS

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            height, state, width
"""


'Label实例x'
x = Label(root,
          text='Hello',
          bg='green',
          font=('Arial',12),
          width=15,
          height=2)
x.pack()

'Label y'
y = Label(root,image='girl.png')
y.pack()



#消息循环
root.mainloop()
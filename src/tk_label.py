from tkinter import *
#from PIL import Image, ImageTk
import os

root=Tk() #

root.title('tk using label') #根窗口的标题

root.geometry('500x500') #根窗口的大小

'text: Label显示的文本'
'font: Label显示的字体'
'relief：控件的样式'
'padx：x方向上，Label内文字与Label边缘的距离'
'pady：y方向上，Label内文字与Label边缘的距离'
x = Label(root,
          text='a beautiful girl',
          font=('Arial',12),
          relief=RIDGE,
          padx = 5,pady=10)

x.pack(pady=20,ipady=20)


'Label y to show image'
file_dir = os.path.dirname(os.getcwd()) + '\image\girl.png'
bm = PhotoImage(file=file_dir)
y = Label(root,image=bm)
y.pack(before=x)



#消息循环
root.mainloop()
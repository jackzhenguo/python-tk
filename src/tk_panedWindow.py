'''''Tkinter教程篇PaneWindow'''
# PaneWindow(面板)为一gm,用来管理子Widget
'''''1.向PanedWindow中添加Pane'''
# 使用add方法
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
panes = PanedWindow(orient=VERTICAL)
panes.pack(fill=BOTH, expand=1)
for w in [Label, Button, Checkbutton, Radiobutton]:
    panes.add(w(panes, text='hello'))
root.mainloop()
# 每个pane中创建一个widget
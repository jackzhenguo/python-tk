from tkinter import *
import random


def create_root(size='600x600'):
    root=Tk() #
    root.title('menu') #根窗口的标题
    root.geometry(size) #根窗口的大小
    return root


class CMenu(object):

    def __init__(self,root):
        self.__root = root
        self.__menubar = Menu(self.__root)

    def __fun(self):
        print(str(random.random())+'\'m ok')

    def create_menu(self):

        xmenu = Menu(self.__menubar)
        xmenu.add_command(label='打开',command=self.__fun)
        xmenu.add_command(label='关闭',command=self.__fun)
        self.__menubar.add_cascade(label='文件',menu=xmenu)

        xmenucfg=Menu(self.__menubar)
        xmenucfg.add_command(label='sku1',command=self.__fun)
        xmenucfg.add_command(label='sku2',command=self.__fun)
        self.__menubar.add_cascade(label='配置',menu=xmenucfg)

        self.__root['menu'] = self.__menubar



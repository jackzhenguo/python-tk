from tkinter import *
from tkinter.constants import *

tk = Tk()
frame = Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label = Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)


button = Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()
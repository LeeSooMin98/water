from tkinter import *

w = Tk()
label1 = Label(w, text="label1", bg="#ff0000")
label2 = Label(w, text="label2", bg="#00ff00")
label3 = Label(w, text="label3", bg="#0000ff")
label1.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
label3.pack(side=BOTTOM)
w.geometry("600x300")
w.resizable(0, 0)
w.mainloop()
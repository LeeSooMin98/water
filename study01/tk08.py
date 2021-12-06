from tkinter import *

window = Tk()
f1 = Frame(window)
f2 = Frame(window)

label1 = Label(f1, text="넓이")
label2 = Label(f1, text="높이")
entry1 = Entry(f1)
entry2 = Entry(f1)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
f1.grid(row=0, column=0)

label3 = Label(window, text="이미지")
label3.grid(row=0, column=1)

btn1 = Button(window, text="이미지 저장")
btn1.grid(row=1, column=0)

btn2 = Button(f2, text="확대")
btn3 = Button(f2, text="축소")
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
f2.grid(row=1, column=1)

window.mainloop()
  
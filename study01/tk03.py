from tkinter import *

window = Tk()
btn = Button(window, bg = "#99004C", fg="#F361A6", text="버튼", width="80", height="2")
btn.pack()
window.mainloop()

#rgb=0~255까지 나타냄(2^8까지), 16진수 사용 0~f까지 사용(0123456789abcdef-16개 최대 0~ff까지 나타낼 수 있음
#(색상정보)을 입력하고 숫자를 입력하면 rgb컬러 입력가능
#FF0000(레드) #00FF00(GREEN) #0000FF(BLUE) #000000(BLACK) #FFFFFF(WHITE)
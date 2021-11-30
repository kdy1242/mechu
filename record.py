import tkinter
import start

class Record:
    def __init__(self, record):
        self.record = record

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        # title
        self.title = tkinter.Label(self.record, text="기    록", font=('맑은고딕', 30))
        self.title.place(x=300, y=50)

        # back 버튼
        self.backButton = tkinter.Button(self.record, width=75, height=75, borderwidth=0, command=self.BackBtn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def BackBtn(self):
        start.Mechu(self.record)

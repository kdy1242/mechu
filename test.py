import tkinter

import spicy_no
import spicy_yes
import start


class Test:
    def __init__(self, test):
        self.test = test

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        self.title = tkinter.Label(self.test, text="매운거땡기시\n나요?", font=('맑은고딕', 30))
        self.title.place(x=400, y=80)

        # yes or no
        self.menuBtn1 = tkinter.Button(self.test, width=10, height=3, text="ㅇㅇ", command=self.spicy_yes)
        self.menuBtn1.place(x=350, y=300)

        self.menuBtn1 = tkinter.Button(self.test, width=10, height=3, text="ㄴㄴ", command=self.spicy_no)
        self.menuBtn1.place(x=550, y=320)

        # back 버튼
        self.backButton = tkinter.Button(self.test, width=75, height=75, borderwidth=0, command=self.back_btn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def back_btn(self):
        start.Mechu(self.test)

    def spicy_yes(self):
        spicy_yes.SpicyYes(self.test)

    def spicy_no(self):
        spicy_no.SpicyNo(self.test)

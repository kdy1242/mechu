import tkinter

import spicy_yes
import start


class SYSoupOk:
    def __init__(self, test):
        self.test = test

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        self.title = tkinter.Label(self.test, text="짬뽕, 라면, 라멘, 김치찌개,\n 순두부찌개, 떡볶이 중에서 골라드십시오", font=30)
        self.title.place(x=200, y=120)

        # home 버튼
        self.homeButton = tkinter.Button(self.test, width=75, height=75, borderwidth=0, command=self.home_btn)
        self.homeButton.place(x=600, y=200)
        self.homeButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.homeButton.config(image=self.homeButtonImg)

        self.title = tkinter.Label(self.test, text="시작화면으로", font=30)
        self.title.place(x=600, y=190)

        # back 버튼
        self.backButton = tkinter.Button(self.test, width=75, height=75, borderwidth=0, command=self.back_btn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def back_btn(self):
        spicy_yes.SpicyYes(self.test)

    def home_btn(self):
        start.Mechu(self.test)

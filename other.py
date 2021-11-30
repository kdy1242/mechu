from tkinter import *
import tkinter

import pick


class Other:
    def __init__(self, menu):
        self.menu = menu

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        self.title = tkinter.Label(self.menu, text="기타", font=30)
        self.title.place(x=500, y=80)

        self.title = tkinter.Label(self.menu, text="뭐드실", font=30)
        self.title.place(x=600, y=80)

        # 메뉴버튼
        self.menuBtn1 = tkinter.Button(self.menu, width=10, height=3, text="스테이크")
        self.menuBtn1.place(x=400, y=230)

        self.menuBtn2 = tkinter.Button(self.menu, width=10, height=3, text="파스타")
        self.menuBtn2.place(x=600, y=230)

        self.menuBtn3 = tkinter.Button(self.menu, width=10, height=3, text="훈제오리")
        self.menuBtn3.place(x=200, y=300)

        self.menuBtn4 = tkinter.Button(self.menu, width=10, height=3, text="햄버거")
        self.menuBtn4.place(x=400, y=300)

        self.menuBtn5 = tkinter.Button(self.menu, width=10, height=3, text="쌀국수")
        self.menuBtn5.place(x=600, y=300)

        self.menuBtn6 = tkinter.Button(self.menu, width=10, height=3, text="만두")
        self.menuBtn6.place(x=200, y=370)

        self.menuBtn7 = tkinter.Button(self.menu, width=10, height=3, text="피자")
        self.menuBtn7.place(x=400, y=370)

        self.menuBtn8 = tkinter.Button(self.menu, width=10, height=3, text="카레")
        self.menuBtn8.place(x=600, y=370)

        # back 버튼
        self.backButton = tkinter.Button(self.menu, width=75, height=75, borderwidth=0, command=self.back_btn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def back_btn(self):
        pick.Pick(self.menu)

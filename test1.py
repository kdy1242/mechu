from tkinter import *
import tkinter
import start

class Test1:
    def __init__(self, test):
        self.test = test

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        # back 버튼
        self.backButton = tkinter.Button(self.test, width=75, height=75, borderwidth=0, command=self.BackBtn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def BackBtn(self):
        start.Mechu(self.test)

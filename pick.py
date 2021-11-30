from tkinter import *
import tkinter

import dessert
import other
import meat
import chicken
import chinese
import japanese
import korean
import ramen
import start


class Pick:
    def __init__(self, pick):
        self.pick = pick

        # 배경이미지
        self.bg = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.pickBg = tkinter.Label(image=self.bg)
        self.pickBg.place(x=-2, y=-2)

        self.title = tkinter.Label(self.pick, text="뭐드실", font=30)
        self.title.place(x=600, y=80)

        # 한식
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="한식", command=self.korean_move)
        self.menuBtn1.place(x=400, y=230)

        # 라면
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="라면", command=self.ramen_move)
        self.menuBtn1.place(x=600, y=230)

        # 치킨
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="치킨", command=self.chicken_move)
        self.menuBtn1.place(x=200, y=300)

        # 고기
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="고기", command=self.meat_move)
        self.menuBtn1.place(x=400, y=300)

        # 일식
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="일식", command=self.japanese_move)
        self.menuBtn1.place(x=600, y=300)

        # 중식
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="중식", command=self.chinese_move)
        self.menuBtn1.place(x=200, y=370)

        # 기타
        self.menuBtn1 = tkinter.Button(self.pick, width=10, height=3, text="기타", command=self.other_move)
        self.menuBtn1.place(x=400, y=370)

        # 분식/야식/디저트
        self.menuBtn1 = tkinter.Button(self.pick, width=15, height=3, text="분식/야식/디저트", command=self.dessert_move)
        self.menuBtn1.place(x=600, y=370)

        # back 버튼
        self.backButton = tkinter.Button(self.pick, width=75, height=75, borderwidth=0, command=self.back_btn)
        self.backButton.place(x=50, y=10)
        self.backButtonImg = tkinter.PhotoImage(file="image/back.png")
        self.backButton.config(image=self.backButtonImg)

    def back_btn(self):
        start.Mechu(self.pick)

    def korean_move(self):
        korean.Korean(self.pick)

    def chinese_move(self):
        chinese.Chinese(self.pick)

    def japanese_move(self):
        japanese.Japanese(self.pick)

    def ramen_move(self):
        ramen.Ramen(self.pick)

    def chicken_move(self):
        chicken.Chicken(self.pick)

    def meat_move(self):
        meat.Meat(self.pick)

    def other_move(self):
        other.Other(self.pick)

    def dessert_move(self):
        dessert.Dessert(self.pick)
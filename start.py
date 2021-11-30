from tkinter import *
import tkinter

import pick
import record
import test1


class Mechu:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startBack = tkinter.PhotoImage(file="image/mechu_bg.gif")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # title
        self.title = tkinter.Label(self.start, text="메 추", font=('맑은고딕', 30))
        self.title.place(x=300, y=100)

        # 테스트버튼
        self.testBtn = tkinter.Button(self.start, text="테스트", command=self.test_move, width=30, repeatdelay=20)
        self.testBtn.place(x=330, y=310)

        # 골라보기버튼
        self.menuBtn = tkinter.Button(self.start, text="골라보기", command=self.pick_move, width=30, repeatdelay=20)
        self.menuBtn.place(x=330, y=350)

        # 기록보기버튼
        self.menuBtn = tkinter.Button(self.start, text="기록보기", command=self.record_move, width=30, repeatdelay=20)
        self.menuBtn.place(x=330, y=390)

    def pick_move(self):
        pick.Pick(self.start)

    def test_move(self):
        test1.Test1(self.start)

    def record_move(self):
        record.Record(self.start)

    def play(self):
        self.start.mainloop()


if __name__ == '__main__':
    # start 화면 만들기
    start = Tk()
    start.title("메 추")
    start.geometry("800x500")
    start.resizable(width=False, height=False)

    mechu = Mechu(start)
    mechu.play()

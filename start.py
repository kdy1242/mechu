from tkinter import *
import tkinter

import main


class Mechu:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startBack = tkinter.PhotoImage(file="image/mechu_title.gif")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        self.testBtn = tkinter.Button(self.start, text="테스트", width=30,
                                          repeatdelay=20)
        self.testBtn.place(x=330, y=310)
        self.menuBtn = tkinter.Button(self.start, text="골라보기", width=30,
                                          repeatdelay=20)
        self.menuBtn.place(x=330, y=350)

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

from tkinter import *


class Mechu:
    def __init__(self):
        self.init_GUI()

    def init_GUI(self):
        self.root = Tk()
        self.root.title('메추')
        self.root.geometry(f'800x500')
        self.root.resizable(width=False, height=False)

        if __name__ == '__main__':
            self.root.mainloop()


if __name__ == '__main__':
    mechu_GUI = Mechu()

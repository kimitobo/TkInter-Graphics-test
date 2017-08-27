
import random
import time
from tkinter import *
from msvcrt import getch
tk = Tk()

canvas = Canvas(tk, width=1920, height=1080)
tk.title("Test")
canvas.pack()

def coords(axis):
    if axis == "x":
        coords = [random.randrange(1920) for i in range(5)]
    else:
        coords = [random.randrange(1080) for i in range(5)]
    return coords

def borders(numAxis, num):
    if numAxis == "x":
        if num > 1920:
            num = 1920
        elif num < 0:
            num = 0
        else:
            return num
    else:
        if num > 1080:
            num = 1080
        elif num < 0:
            num = 0
        else:
            return num
    return num

class Spazz:
    def __init__(self):
        self.lastx = coords("x")
        self.lasty = coords("y")
        self.newx = self.lastx
        self.newy = self.lasty
        self.poly_2 = canvas.create_polygon(self.lastx[0], self.lasty[0], self.lastx[1], self.lasty[1], self.lastx[2], self.lasty[2], self.lastx[3], self.lasty[3], self.lastx[4], self.lasty[4], fill="", outline="black")
        self.tick = 0
        self.mvmnt = []

    def move(self, width, tick):

        self.poly_1 = canvas.create_polygon(self.lastx[0], self.lasty[0], self.lastx[1], self.lasty[1], self.lastx[2], self.lasty[2], self.lastx[3], self.lasty[3], self.lastx[4], self.lasty[4], fill="", outline="black", width=width)
        canvas.delete(self.poly_2)

        if tick == 0:
            self.mvmnt = []

            for i in range(10):
                self.direction = random.randint(0, 1)
                self.speed = random.randint(0, 50)

                if self.direction == 0:
                    self.speed = -self.speed

                self.mvmnt.append(self.speed)

        self.newx = []
        self.newy = []
        for num, i in enumerate(self.lastx):
            self.newx.append(i + self.mvmnt[num])

        for num, i in enumerate(self.lasty):
            num += 5
            self.newy.append(i + self.mvmnt[num])

        self.lastx = [borders("x", i) for i in self.newx]
        self.lasty = [borders("y", i) for i in self.newy]

        self.poly_2 = canvas.create_polygon(self.lastx[0], self.lasty[0], self.lastx[1], self.lasty[1], self.lastx[2], self.lasty[2], self.lastx[3], self.lasty[3], self.lastx[4], self.lasty[4], fill="", outline="black", width=width)
        canvas.delete(self.poly_1)

poly = Spazz()
poly1 = Spazz()
poly2 = Spazz()
poly3 = Spazz()
poly4 = Spazz()
poly5 = Spazz()
poly6 = Spazz()
poly7 = Spazz()

def movement():
    width = 80
    tick = 0

    while True:
        #key = ord(getch())
        #if key == 80:
        #    print("Down")
        #    if width > 1:
        #        width -= 1
        #    else:
        #        width = 1

        #if key == 72:
        #    print("Up")
        #    width += 1
        if tick == 50:
            tick = 0

        tk.update()
        poly.move(random.randrange(75), tick)
        poly1.move(random.randrange(75), tick)
        poly2.move(random.randrange(75), tick)
        poly3.move(random.randrange(75), tick)
        poly4.move(random.randrange(75), tick)
        poly5.move(random.randrange(75), tick)
        poly6.move(random.randrange(75), tick)
        poly7.move(random.randrange(75), tick)

        time.sleep(0.0001)
        tick += 1

movement()



canvas.mainloop()

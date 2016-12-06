# Welcome Screen and File Creation
from VirtualBroker3_0 import VirtualBroker
from button import *
from graphics import *
class Welcome(VirtualBroker):

    def __init__(self):
        win = GraphWin("Welcome", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createDisplay()
        filename = self.inputBar()
        stocklist = open(filename, "w")
        stocklist.close()

    def __createDisplay(self):
        # Creates title box
        textbox1 = Rectangle(Point(2.5, 8), Point(7.5, 10))
        textbox1.draw(self.win)
        textbox1.setFill("white")

        # Creates text for welcome
        welcometext = Text(Point(5, 9), "Welcome! \n Please enter your name.")
        welcometext.setSize(20)
        welcometext.draw(self.win)

        # Creates Textbox
        textbox2 = Rectangle(Point(3, 1.4), Point(7, 2.6))
        textbox2.setFill("white")
        textbox2.draw(self.win)

        # Creates text for input bar
        text1 = Text(Point(5, 2), "")
        text1.draw(self.win)
        self.textB = text1

    def inputBar(self):
        self.textB.setText("")
        index = ""  #Blank Message
        while True:
            p = self.win.getKey()  #Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1]  #Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space":  # adds a space when the space bar is hit!
                index = index + " "
                continue
            if p == "period":
                index = index + "."
                self.textB.setText(" " + index)
                continue
            if p == "Shift_L" or p =="Shift_R":
                self.textB.setText(" " + index)
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)

Welcome()
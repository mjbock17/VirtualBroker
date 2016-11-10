from graphics import *
from button import Button


class Virtual_Broker:
    def __init__(self):
        win = GraphWin("Virtual Broker",700,500)
        win.setCoords(0,0,9,7)
        win.setBackground("slategray")
        self.win = win
        self.__createButtons()
        self.__createDisplay()


    def __createButtons(self):


        bsort = [(6,1,"Data Analysis"),(6,2,"Portfolio Development"),
                 (6,3,"Market/Industry Trends"),(6,4,"Stock Picking")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4.75,.75,label))
        for b in self.buttons:
            b.activate()


    def __createDisplay(self):
        bg = Rectangle(Point(.5,5.5), Point(8.5,6.5))
        bg.setFill('white')
        bg.draw(self.win)
        a = Rectangle(Point(4,4.5),Point(8,5.25))
        a.setFill('white')
        a.draw(self.win)
        text = Text(Point(4.5,6), "Welcome to Our Virtual Broker!")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(18)
        self.display = text
        text1 = Text(Point(6,4.85),"Please select a service:")
        text1.draw(self.win)
        text1.setFace("courier")
        text1.setStyle("bold")
        text1.setSize(15)
        self.display = text1
        c = Rectangle(Point(.5,1),Point(3.1,4.75))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(1.8,3),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8,1.3),"Hello, my name is Jerry!")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        self.display = text2
        


    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()


    def processButton(self, key):
        if key == 'Stock Picking':#
            self.win.close()#
            import StockpickGUI#
            stockpicking()#
        elif key == 'Portfolio Development':
            import PortfolioDevGUI
            self.display.setText(text[:-1])
        elif key == 'Linear Search':
            b = linSearch(3,globallist)
            self.display.setText(b)
        elif key == 'Binary Search':
            mergeSort(globallist)
            a = binSearch(3,globallist)
            self.display.setText(a)
        elif key == 'Selection Sort':
            selSort(globallist)
            self.display.setText(globallist)
        elif key == 'Merge Sort':
            mergeSort(globallist)
            self.display.setText(globallist)
        else:
            self.display.setText(text+key)
            


    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)


if __name__ == '__main__':
    theCalc = Virtual_Broker()
    theCalc.run()

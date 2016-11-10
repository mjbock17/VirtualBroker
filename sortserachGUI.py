from graphics import *
from Button import Button

class stockpicking:
    def __init__(self):
        win = GraphWin("Stock Picking",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win      
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Enter Stock Information")
        title.draw(self.win)
        title.setSize(30)
        title.setStyle("bold")
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

    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

class pmgmt:
    def __init__(self):
        win = GraphWin("Portfolio Management",700,500)#
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "How can I help you with your portfolio?")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")
        
class SortSearch:
    def __init__(self):
        win = GraphWin("Virtual Broker",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):

        bsort = [(7,1.5,"Data Analysis"),(7,3,"Portfolio Management"),#
                 (7,4.5,"Market/Industry Trends"),(7,6,"Stock Picking")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,1.2,label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        bg = Oval(Point(1.4,9.5), Point(8.6,7.9))
        bg.setFill('white')
        bg.draw(self.win)
        a = Line(Point(5,7),Point(8.9,7))
        a.draw(self.win)
        text = Text(Point(5,8.7), "Welcome to Our Virtual Broker!")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(18)
        self.display = text
        text1 = Text(Point(7,7.2),"Please select a service:")
        text1.draw(self.win)
        text1.setFace("courier")
        text1.setStyle("bold")
        text1.setSize(14)
        self.display = text1
        c = Rectangle(Point(.5,1),Point(3.5,7))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(2,4),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(2,1.5),"Hello, my name is Jerry!")
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
        text = self.display.getText()  
        if key == 'Stock Picking':#
            self.win.close()#
            stockpicking()#
        elif key == 'Portfolio Management':#
            self.win.close()#
            pmgmt()#

        else:
            self.display.setText(text+key)
            

    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

if __name__ == '__main__':
    theCalc = SortSearch()
    theCalc.run()

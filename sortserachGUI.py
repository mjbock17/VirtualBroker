from graphics import *
from button import Button

class stockpicking:
    def __init__(self):
        win = GraphWin("Stock Picking",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()   
    
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

from graphics import *
from button import Button
from graphics import *
from button import Button
class pmgmt:
    def __init__(self):
        win = GraphWin("Portfolio Management",700,500)#
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        #self.__createinputDisplay()
        self.__createButtons()
        self.__makeJerry()

        box1 = Rectangle(Point(1,1), Point(9,2)) ###textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox = Text(Point(5,1.5), "") ###Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox ###creates a textbox variable

    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.png")
        bg.draw(self.win) 
    
    def __createButtons(self):
        aSpecs = [(2.5,6,'100%'), (7.5,6,'50%'),
                  (2.5,4.5,'75%'), (7.5,4.5,'25%')]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
            
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __makeJerry(self):
        c = Rectangle(Point(4,2.5),Point(6,7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(5,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(5,7.8),"One must spend money to make it")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
            
    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "What Level of Risk Will You Accept?")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")

    '''def __createinputDisplay(self):
        newdisp = Rectangle(Point(3,5.5),Point(7,6.5))
        newdisp.setFill('white')
        newdisp.draw(self.win)'''

    def getButton(self):
        # Waits for a button to be clicked and returns the label of
        #    the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel() # method exit
                
    def processButton(self, key):
        # Updates the display of the calculator for press of this key
        if key == 'C':
            self.display.setText("")
        elif key == '100%':
            num = self.inputBar()
        elif key == 'Binary Search':
            ans1 = binSearch(21,mynums)
            self.display.setText(ans1)
        elif key == 'Selection Sort':
            selSort(mynums)
            self.display.setText(mynums)
        elif key == 'Merge Sort':
            mergeSort(mynums)
            self.display.setText(mynums)
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)
            
    def inputBar(self):
        self.textB.setText("hi")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textB.setText(message + " " + index)
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)
            
    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.getButton()
            self.processButton(key)
 
class VirtualBroker: #name change
    def __init__(self):
        win = GraphWin("Virtual Broker",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()

    def __bgimg(self):
        bg = Image(Point(5,5),"wood.png")
        bg.draw(self.win) 

    def __createButtons(self):

        bsort = [(7,1.5,"Data Analysis"),(7,3,"Portfolio Management"),#
                 (7,4.5,"Market/Industry Trends"),(7,6,"Stock Picking")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,1.2,label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        bg = Rectangle(Point(1.4,9.2), Point(8.6,8.2))#
        bg.setFill('white')#
        bg.setOutline("gold")#
        bg.setWidth(4)#
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
            self.win.close()##
        elif key == 'Portfolio Management':#
##            self.win.close()#
            newin = pmgmt()#
            while True:
                newin.run()

        else:
            self.display.setText(text+key)
            

    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

if __name__ == '__main__':
    theCalc1 = VirtualBroker()
    theCalc1.run()

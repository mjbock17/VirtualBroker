from graphics import *
from button import Button

class Data_Analysis:
    def __init__(self):
        #creates window for GUI
        win = GraphWin("Data Analysis",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):

        #creates the list of buttons
        bsort = [(2.5,6,"Button 1"),(7.5,6,"Button 2"),
                 (2.5,4.5,"Button 3"),(7.5,4.5,"Button 4")]
        self.buttons = []
        #creates the odd shaped buttons
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4.75,.75,label))
        #activates all buttons
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
        
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Data Analysis")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")

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
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == 'Button 1':
            ans = linSearch(21,mynums)
            self.display.setText(ans)
        elif key == 'Button 2':
            ans1 = binSearch(21,mynums)
            self.display.setText(ans1)
        elif key == 'Button 3':
            selSort(mynums)
            self.display.setText(mynums)
        elif key == 'Button 4':
            mergeSort(mynums)
            self.display.setText(mynums)
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)
 
    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.getButton()
            self.processButton(key)

class dontbuy:
    def __init__(self):
        win = GraphWin("Stock Picking(4)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()

    def __createButtons(self):
        bsort = [(4,2,"Return to home page")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,1,label))
        for b in self.buttons:
            b.activate()
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "We Advise...")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7,2.5),Point(9,7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(8,5),"myrodin.gif")
        image.draw(self.win)

        questionbox = Rectangle(Point(1,7.5),Point(6.75,6.2))
        questionbox.setFill('white')
        questionbox.draw(self.win)

        question = Text(Point(3.8,7.1),"to NOT buy this stock,")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

        question1 = Text(Point(3.8,6.5),"for these reasons:")
        question1.draw(self.win)
        question1.setSize(15)
        question1.setFace('courier')

        reason1 = Text(Point(3.8, 5.8),"-The stock is most likely overpriced")
        reason1.draw(self.win)
        reason1.setSize(13)
        reason1.setFace('courier')
        
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        if key == 'Return to home page':#
            self.win.close()#
            newin = VirtualBroker()
            while True:
                newin.run()
        
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

class retain_peGUI:
    def __init__(self):
        win = GraphWin("Stock Picking(2)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()

    def __createButtons(self):
        bsort = [(4,2.5,"PE greater than or equal to 18"),(4,5,"PE less than 18")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,2,label))
        for b in self.buttons:
            b.activate()
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7,2.5),Point(9,7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(8,5),"myrodin.gif")
        image.draw(self.win)

        questionbox = Rectangle(Point(1,7.5),Point(6.75,6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)

        question = Text(Point(3.8,7.1),"What is the PE ratio?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

        question = Text(Point(3.8,6.7),"(Price over Earnings)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')


    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        if key == "PE greater than or equal to 18":#
            self.win.close()#
            newin = dontbuy()
            while True:
                newin.run()
        elif key == 'PE less than 18':#
            self.win.close()#
            newin = divyeild()#
            while True:
                newin.run()
        
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

class grow_peGUI:
    def __init__(self):
        win = GraphWin("Stock Picking(3)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()

    def __createButtons(self):
        bsort = [(4,2.5,"PE greater than or equal to 18"),(4,5,"PE less than 18")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,2,label))
        for b in self.buttons:
            b.activate()
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7,2.5),Point(9,7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(8,5),"myrodin.gif")
        image.draw(self.win)

        questionbox = Rectangle(Point(1,7.5),Point(6.75,6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)

        question = Text(Point(3.8,7.1),"What is the PE ratio?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

        question = Text(Point(3.8,6.7),"(Price over Earnings)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')


    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        if key == 'PE greater than or equal to 18':#
            self.win.close()#
            newin = moreinfo()
            while True:
                newin.run()
        elif key == 'PE less than 18':#
            self.win.close()#
            newin = dontbuy()#
            while True:
                newin.run()

        
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

class stockpicking:
    def __init__(self):
        win = GraphWin("Stock Picking",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()

    def __createButtons(self):

        bsort = [(4,2.5,"Grow Market Share"),(4,5,"Retain Market Share")]
        self.buttons = []
        for (cx,cy,label) in bsort:
             self.buttons.append(Button(self.win,Point(cx,cy),4,2,label))
        for b in self.buttons:
            b.activate()
    
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7,2.5),Point(9,7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(8,5),"myrodin.gif")
        image.draw(self.win)

        questionbox = Rectangle(Point(1,7.5),Point(6.75,6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)

        question = Text(Point(3.8,7.2),"Do you expect the company to retain its")
        question.draw(self.win)
        question.setSize(11)
        question.setFace('courier')

        question = Text(Point(3.8,6.6),"market share or to grow its market share?")
        question.draw(self.win)
        question.setSize(11)
        question.setFace('courier')

        
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key): 
        if key == 'Retain Market Share':#
            self.win.close()#
            newin = retain_peGUI()#
            while True:
                newin.run()
        elif key == 'Grow Market Share':#
            self.win.close()#
            newin = grow_peGUI()#
            while True:
                newin.run()
        
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
            newin = stockpicking()
            while True:
                newin.run()
        elif key == 'Portfolio Management':#
            self.win.close()#
            newin = pmgmt()#
            while True:
                newin.run()
        elif key == 'Data Analysis':
            newin = Data_Analysis()
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

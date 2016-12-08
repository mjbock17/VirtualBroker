from graphics import *
from button import Button

class Welcome:
    def __init__(self):
        win = GraphWin("Welcome", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createDisplay()
        self.__createFile()
        self.win.close()

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

    def __createFile(self):
        filename = self.inputBar()
        stocklist = open(str(filename) + ".txt", "w")
        stocklist.close()

    def inputBar(self):
        self.textB.setText("")
        index = ""  # Blank Message
        while True:
            p = self.win.getKey()  # Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) - 1]  # Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space":  # adds a space when the space bar is hit!
                index += " "
                continue
            if p == "period":
                index += "."
                self.textB.setText(" " + index)
                continue
            if p == "Shift_L" or p == "Shift_R":
                self.textB.setText(" " + index)
                continue
            index += str(p)  # Adds String
            self.textB.setText(" " + index)

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
        bg = Image(Point(5,5),"wood.gif")
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

    def sceneSet(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()
    
    def processButton(self, key):
        text = self.display.getText()  #Need?
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
        elif key == 'Market/Industry Trends':
            self.win.close()
            newin = MarketIndustryTrends()
            while True:
                newin.run()
            
    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

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

    # def end(self):

#######################################################################
## Danny's Section
class stockpicking(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()  
    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4,2.5,"Grow Market Share"),(4,5,"Retain Market Share")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label)) ###Creates a back button
            else:
                self.buttons.append(Button(self.win,Point(cx, cy),4,2,label)) 
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
    def setScene(self):
        return VirtualBroker   
    def processButton(self, key): 
        if key == 'Retain Market Share':
            self.win.close()
            newin = retain_peGUI()
            while True:
                newin.run()
        elif key == 'Grow Market Share':
            self.win.close()
            newin = grow_peGUI()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
            
class retain_peGUI(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(2)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4,3.25,"PE greater than or equal to 18"),(4,5,"PE less than 18, greater than zero"),(4,1.5,"Negative/Zero PE")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,1.5,label))
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
        question = Text(Point(3.8,6.7),"(consult Yahoo Finance)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
    def setScene(self):
        return stockpicking
    def processButton(self, key):
        if key == "PE greater than or equal to 18":#
            self.win.close()#
            newin = dontbuy()
            while True:
                newin.run()
        elif key == 'PE less than 18, greater than zero':#
            self.win.close()#
            newin = divyield()#
            while True:
                newin.run()
        elif key == 'Negative/Zero PE':
            self.win.close()
            newin = dontbuy()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class grow_peGUI(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(3)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()    
    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4,3.25,"PE greater than or equal to 18"),(4,5,"PE less than 18, greater than zero"),(4,1.5,"Negative/Zero PE")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,1.5,label))
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
        question = Text(Point(3.8,6.7),"(consult Yahoo Finance)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
    def setScene(self):
        return stockpicking
    def processButton(self, key):
        if key == 'PE greater than or equal to 18':#
            self.win.close()#
            newin = analyst_opinion()
            while True:
                newin.run()
        elif key == 'PE less than 18, greater than zero':#
            self.win.close()#
            newin = dontbuy()#
            while True:
                newin.run()
        elif key == "Negative/Zero PE":
            self.win.close()
            newin = strongreason()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
class analyst_opinion(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(8)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()      
    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4,2.5,"Generally Negative"),(4,5,"Generally Positive")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,2,label))
        for b in self.buttons:
            b.activate()
    def __createstockDisplay(self):
        head = Rectangle(Point(.15,8),Point(9.85,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Financial Analyst's Opinions")
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
        questionbox = Rectangle(Point(.15,7.85),Point(6.9,6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.55,7.1),"What is the general consensus between\nfinancial analysts on this stock?\nDo they suggest a buy?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
    def setScene(self):
        return stockpicking
    def processButton(self, key):
        if key == 'Generally Positive':#
            self.win.close()#
            newin = buy()
            while True:
                newin.run()
        elif key == 'Generally Negative':#
            self.win.close()#
            newin = dontbuy()#
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class strongreason(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(5)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()      
    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4,2.5,"No"),(4,5,"Yes")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,2,label))
        for b in self.buttons:
            b.activate()
    def __createstockDisplay(self):
        head = Rectangle(Point(.3,8),Point(9.7,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Stock Has Negative Earnings")
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
        question = Text(Point(3.8,7.1),"Are you certain that this")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question = Text(Point(3.8,6.7),"company will recover and grow?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
    def setScene(self):
        return stockpicking
    def processButton(self, key):
        if key == 'Yes':#
            self.win.close()#
            newin = buy()
            while True:
                newin.run()
        elif key == 'No':#
            self.win.close()#
            newin = dontbuy()#
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class divyield(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(6)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()

    def __createButtons(self):
        bsort = [(1, 1, "Back"),(2.8,3.5,"Click to Enter")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()
    def __createstockDisplay(self):
        head = Rectangle(Point(.2,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(4.6,8.5), "Dividend Analysis")
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
        questionbox = Rectangle(Point(.2,7.5),Point(6.9,6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.65,6.8),"Please enter this company's dividend \nyield ratio(if N/A enter 0) \nthen press enter")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def __createinputDisplay(self):
        box1 = Rectangle(Point(4,3), Point(6,4)) ###textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6,1.5), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5,3.5), "") ###Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox ###creates a textbox variable


    def inputBar(self):
        self.textB.setText("")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space": #adds a space when the space bar is hit!
                index = index + " " 
                continue
            if p == "period":
                index = index + "."
                self.textB.setText(" " + index)
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)
            
    def setScene(self):
        return stockpicking
        
    def processButton(self, key):
        try:
            if key == "Back":
                self.win.close()
                newin = self.prevScene()
                while True:
                    newin.run()
            elif key == "Click to Enter":
                blink = Rectangle(Point(4.1,4.1),Point(4.2,4.2)) #notifies the user to type
                blink.setFill('red')
                blink.draw(self.win)
                information = self.inputBar()
                divyield = float(information)
                blink.undraw()
                if divyield>1.5:
                    self.win.close()
                    newin = buy()
                    while True:
                        newin.run()
                else:
                    self.win.close()
                    newin = dontbuy()
                    while True:
                        newin.run()
        except:
            error = Text(Point(4.5,2.5),"ERROR. Please enter a numeric value")
            error.draw(self.win)
                    
class dontbuy(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(4)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()    
    def __createButtons(self):
        bsort = [(2,1,"Return to home page")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            self.buttons.append(Button(self.win,Point(cx,cy),2.4,1,label))
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
        question = Text(Point(3.8,7.1),"to NOT buy this stock, for")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question1 = Text(Point(3.8,6.5),"one or more of these reasons:")
        question1.draw(self.win)
        question1.setSize(15)
        question1.setFace('courier')
        reason1 = Text(Point(3.8, 5.8),"-The stock is most likely overpriced")
        reason1.draw(self.win)
        reason1.setSize(13)
        reason1.setFace('courier')
        reason2 = Text(Point(3.5,5),"-Dividend income is insufficient")
        reason2.draw(self.win)
        reason2.setSize(13)
        reason2.setFace('courier')
        reason3 = Text(Point(3.5,4.25),"-The stock is not likely to grow")
        reason3.draw(self.win)
        reason3.setSize(13)
        reason3.setFace('courier')
        reason4 = Text(Point(3.6,3.3),"-This company is incurring a loss\nand is not expected to grow")
        reason4.draw(self.win)
        reason4.setSize(13)
        reason4.setFace('courier')
    def processButton(self, key):
        if key == 'Return to home page':#
            self.win.close()#
            newin = VirtualBroker()
            while True:
                newin.run()

class buy(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(4)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()     
    def __createButtons(self):
        bsort = [(2,1,"Return to home page"),(3.8,4.5,"Projected Earnings"),(3.8,3,"Archive This Stockpick")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            self.buttons.append(Button(self.win,Point(cx,cy),2.4,1,label))
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
        questionbox = Rectangle(Point(1,7.5),Point(6.75,6.75))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8,7.1),"To go ahead and BUY this stock")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        reason1 = Text(Point(3.8, 5.8),"Although we advise you to buy,\nearnings are never guaranteed")
        reason1.draw(self.win)
        reason1.setSize(13)
        reason1.setFace('courier')
    def processButton(self, key):
        if key == 'Projected Earnings':
            self.win.close()
            newin = projearn()
            while True:
                newin.run()
        elif key == 'Archive This Stockpick':
            self.win.close()
            newin = filecreator()
            while True:
                newin.run()
        elif key == 'Return to home page':#
            self.win.close()#
            newin = VirtualBroker()
            while True:
                newin.run()

class projearn(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(10)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()

    def __createButtons(self):
        bsort = [(1, 1, "Back"),(3.4,5.3,"Click to Enter")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()
    def __createstockDisplay(self):
        head = Rectangle(Point(1,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Projected Earnings")
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
        questionbox = Rectangle(Point(.2,7),Point(6.9,6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.6,6.5),"Please enter this company's current stock price")
        question.draw(self.win)
        question.setSize(11)
        question.setFace('courier')

    def __createinputDisplay(self):
        box1 = Rectangle(Point(4.7,4.8), Point(6.7,5.8)) ###textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6,1.5), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5.7,5.3), "") ###Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox ###creates a textbox variable


    def inputBar(self):
        self.textB.setText("")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space": #adds a space when the space bar is hit!
                index = index + " " 
                continue
            if p == "period":
                index = index + "."
                self.textB.setText(" " + index)
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)
            
    def setScene(self):
        return buy
        
    def processButton(self, key):
        try:
            if key == "Back":
                self.win.close()
                newin = self.prevScene()
                while True:
                    newin.run()
            elif key == "Click to Enter":
                blink = Rectangle(Point(2.3,5.8),Point(2.2,5.9)) #notifies the user to type
                blink.setFill('red')
                blink.draw(self.win)
                information = self.inputBar()
                price = float(information)
                blink.undraw()
                fiveper = price*1.05-price
                nfiveper = "%.2f" % fiveper
                tenper = price*1.1-price
                ntenper = "%.2f" % tenper
                fifteenper = price*1.15-price
                nfifteenper = "%.2f" % fifteenper
                twentyper = price*1.2-price
                ntwentyper = "%.2f" % twentyper
                five = Text(Point(4,4),"-Earnings of five percent: $"+nfiveper)
                five.draw(self.win)
                ten = Text(Point(4,3),"-Earnings of ten percent: $"+ntenper)
                ten.draw(self.win)
                fifteen = Text(Point(4,2),"-Earnings of fifteen percent: $"+nfifteenper)
                fifteen.draw(self.win)
                twenty = Text(Point(4,1),"-Earnings of twenty percent: $"+ntwentyper)
                twenty.draw(self.win)
        except:
            error = Text(Point(4.5,2.5),"ERROR. Please enter a numeric value")
            error.draw(self.win)

class filecreator(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(11)",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()


    def __createButtons(self):
        bsort = [(1, 1, "Back"),(2.8,3.2,"Click to Enter Name"),(2.8,4.5,"Click to Enter 'ticker'")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2.2,1,label))
        for b in self.buttons:
            b.activate()
    def __createstockDisplay(self):
        head = Rectangle(Point(.2,8),Point(9,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(4.6,8.5), "Archive This Stockpick")
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
        questionbox = Rectangle(Point(.2,7.5),Point(6.9,6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.65,6.8),"Please enter the company name\nand the stocks 'ticker'")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def __createinputDisplay(self):
        box1 = Rectangle(Point(4,4), Point(6,5)) ###textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox3 = Text(Point(5,4.5), "")
        textbox3.setSize(10)
        textbox3.draw(self.win)
        textbox4 = Text(Point(5,4.5), "") ###Creates a blank textbox
        textbox4.draw(self.win)
        self.textB = textbox4 ###creates a textbox variable

        box2 = Rectangle(Point(4,2.7), Point(6,3.7)) ###textbox
        box2.setFill("white")
        box2.draw(self.win)
        textbox2 = Text(Point(5,3.2), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5,3.2), "") ###Creates a blank textbox
        textbox.draw(self.win)
        self.textA = textbox ###creates a textbox variable


    def inputBar(self):
        self.textB.setText("")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space": #adds a space when the space bar is hit!
                index = index + " " 
                continue
            if p == "period":
                index = index + "."
                self.textB.setText(" " + index)
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)

    def inputBar1(self):
        self.textA.setText("")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textA.setText(" " + index)
                continue
            if p == "space": #adds a space when the space bar is hit!
                index = index + " " 
                continue
            if p == "period":
                index = index + "."
                self.textA.setText(" " + index)
                continue
            index = index + str(p) ###Adds String
            self.textA.setText(" " + index)
            
    def setScene(self):
        return stockpicking
        
    def processButton(self, key):
        try:
            if key == "Back":
                self.win.close()
                newin = self.prevScene()
                while True:
                    newin.run()
            elif key == "Click to Enter Name":
                blink = Rectangle(Point(5.8,3.8),Point(5.9,3.9)) #notifies the user to type
                blink.setFill('red')
                blink.draw(self.win)
                information = self.inputBar1()
                
            elif key == "Click to Enter 'ticker'":
                blink1 = Rectangle(Point(5.8,5.1),Point(5.9,5.2))
                blink1.setFill('red')
                blink1.draw(self.win)
                information1 = self.inputBar()
        except:
            error = Text(Point(4.5,2.5),"ERROR")
            error.draw(self.win)


#########################################################################################
#Henrik's Section
                
class pmgmt(VirtualBroker):
    def __init__(self):
        win = GraphWin("Portfolio Management",700,500)#
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createinputDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()
        
    def __createinputDisplay(self):
        box1 = Rectangle(Point(3,1), Point(9,2)) ###textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6,1.5), "enter a risk level between 0 and 100")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(7.5,1.5), "") ###Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox ###creates a textbox variable

    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win) 
    
    def __createButtons(self):
        aSpecs = [(1, 1, "Back"),(2.2,3.1,"enter text")]
        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Back":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
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

    def inputBar(self):
        self.textB.setText("")
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.textB.setText(" " + index)
                continue
            if p == "space": #adds a space when the space bar is hit!
                index = index + " " 
                continue
            index = index + str(p) ###Adds String
            self.textB.setText(" " + index)
            
    def setScene(self):
        return VirtualBroker
    
    def processButton(self, key):
        # Updates the display for press of this key
        try:
            if key == 'enter text':
                blink = Rectangle(Point(2.5,2.1),Point(2.6,2.2)) #notifies the user to type
                blink.setFill('red')
                blink.draw(self.win)
                information = self.inputBar()
                newinfo = int(information)
                blink.undraw()
                if 50 <= newinfo:
                    self.win.close()
                    newin = highrisk()
                    while True:
                        newin.run()
                elif newinfo < 50:
                    self.win.close()
                    newin = lowrisk()
                    while True:
                        newin.run()
            elif key == "Back":
                self.win.close()
                newin = self.prevScene()
                while True:
                    newin.run()
        except:
            error = Text(Point(6,.6),"ERROR. Please enter a numeric value")
            error.draw(self.win)
            error.setTextColor('white')
            
class highrisk(VirtualBroker):
    def __init__(self):
        win = GraphWin("High Risk",700,500)#
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Back"), (1.5,6,'Long Term'),
                  (1.5,4.5,'Short Term')]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Back":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "High Risk Portfolio")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(5.25,2.7),Point(9.725,7.25))
        a.setFill("Light Steel Blue")
        a.setOutline("gold")
        a.draw(self.win)
        graph = Image(Point(7.5,5),"sp500.gif")
        graph.draw(self.win)    

    def __makeJerry(self):
        myrec = Rectangle(Point(2.8,2.7),Point(4.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(3.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(3.1,2.5),"Try the Stock Market!")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(3.3,2.2),"I recommend a shorter horizon")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return pmgmt
    
    def processButton(self, key):
        if key == 'Long Term':
            self.win.close()
            newin = hrlt()
            while True:
                newin.run()
        if key == 'Short Term':
            self.win.close()
            newin = hrst()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
        
class lowrisk(VirtualBroker):
    def __init__(self):
        win = GraphWin("Low Risk",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Back"), (1.5,6,'Long Term'),
                  (1.5,4.5,'Short Term')]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Back":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Low Risk Portfolio")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")
        
    def __graph(self):
        a = Rectangle(Point(5.25,2.7),Point(9.725,7.25))
        a.setFill("Light Steel Blue")
        a.setOutline("gold")
        a.draw(self.win)
        graph = Image(Point(7.5,5),"10yeart.gif")
        graph.draw(self.win)
        
    def __makeJerry(self):
        myrec = Rectangle(Point(2.8,2.7),Point(4.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(3.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(3.1,2.5),"You're not a risk taker")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(3.3,2.2),"I recommend a longer horizon")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return pmgmt
    
    def processButton(self, key):
        if key == 'Long Term':
            self.win.close()
            newin = lrlt()
            while True:
                newin.run()
        if key == 'Short Term':
            self.win.close()
            newin = lrst()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class hrlt(VirtualBroker):
    def __init__(self):
        win = GraphWin("hrlt",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "High Risk Long Term")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")
        
    def __graph(self):
        a = Rectangle(Point(3.7,1),Point(9.3,7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5,4),"hrlt.gif")
        graph.draw(self.win)
        
    def __makeJerry(self):
        myrec = Rectangle(Point(0.8,2.7),Point(2.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8,2.5),"Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2,2.2),"that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker
    
    def processButton(self, key):
        if key == "Home":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class hrst(VirtualBroker):
    def __init__(self):
        win = GraphWin("hrst",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "High Risk Short Term")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")
        
    def __graph(self):
        a = Rectangle(Point(3.7,1),Point(9.3,7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5,4),"hrst.gif")
        graph.draw(self.win)
        
    def __makeJerry(self):
        myrec = Rectangle(Point(0.8,2.7),Point(2.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8,2.5),"Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2,2.2),"that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker
    
    def processButton(self, key):
        if key == "Home":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class lrlt(VirtualBroker):
    def __init__(self):
        win = GraphWin("lrlt",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Low Risk Long Term")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")
        
    def __graph(self):
        a = Rectangle(Point(3.7,1),Point(9.3,7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5,4),"lrlt.gif")
        graph.draw(self.win)
        
    def __makeJerry(self):
        myrec = Rectangle(Point(0.8,2.7),Point(2.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8,2.5),"Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2,2.2),"that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker
    
    def processButton(self, key):
        if key == "Home":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class lrst(VirtualBroker):
    def __init__(self):
        win = GraphWin("lrst",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()
        
    def __bgimg(self):
        bg = Image(Point(5,5),"gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9,1),Point(9.5,7))
        head.setFill('white')
        head.draw(self.win)
        
    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]

        self.buttons = []
        for (cx,cy,label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win,Point(cx,cy),1,1,label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),2,1,label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Low Risk Short Term")#
        title.draw(self.win)
        title.setSize(15)#
        title.setStyle("bold")
        
    def __graph(self):
        a = Rectangle(Point(3.7,1),Point(9.3,7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5,4),"lrst.gif")
        graph.draw(self.win) 
        
    def __makeJerry(self):
        myrec = Rectangle(Point(0.8,2.7),Point(2.8,7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8,5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8,2.5),"Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2,2.2),"that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker
    
    def processButton(self, key):
        if key == "Home":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
                
###################################################################################################
class MarketIndustryTrends(VirtualBroker):
    def __init__(self):
        #creates window for GUI
        win = GraphWin("Market/Industry Trends",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__makeJerry()
        self.prevScene = self.setScene()


    def __bgimg(self):
        bg = Image(Point(5,5),"wood.gif")
        bg.draw(self.win) 

    def __createButtons(self):

        #creates the list of buttons
        bsort = [(1, 1, "Back"),(3,6.25,"S&P 500"),(3,5,"Dow Jones"),
                 (3,3.75,"NASDAQ"),(3,2.5,"Russel Top 200")]
        self.buttons = []
        #creates the odd shaped buttons
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,.75,label))
        #activates all buttons
        for b in self.buttons:
            b.activate()

    def __makeJerry(self):
        c = Rectangle(Point(6.5,2),Point(8.5,7))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(7.5,4.5),"myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(7.5,1.5),"Please select a Market \n to view its index.")
        text2.setTextColor('white')
        text2.setSize(15)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Market/Industry Trends")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def setScene(self):
        return VirtualBroker

    def processButton(self, key):
        if key == 'S&P 500':
            self.win.close()
            newin = SandP500()
            while True:
                newin.run()
        elif key == 'Dow Jones':
            self.win.close()
            newin = DowJones()
            while True:
                newin.run()
        elif key == 'NASDAQ':
            self.win.close()
            newin = Nasdaq()
            while True:
                newin.run()
        elif key == 'Russel Top 200':
            self.win.close()
            newin = RusselTop200()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)

class SandP500(VirtualBroker):
    def __init__(self):
        #creates window for GUI
        win = GraphWin("SandP500",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5,5),"wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,.75,label))
        for b in self.buttons:
            b.activate()
            
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "S&P500")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5,5),"sandp500.gif")
        graph.draw(self.win)

    def setScene(self):
        return MarketIndustryTrends 

    def processButton(self, key):

        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class Nasdaq(VirtualBroker):
    def __init__(self):
        #creates window for GUI
        win = GraphWin("Nasdaq",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5,5),"wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,.75,label))
        for b in self.buttons:
            b.activate()
            
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "NASDAQ")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5,5),"nasdaq.gif")
        graph.draw(self.win)

    def setScene(self):
        return MarketIndustryTrends 

    def processButton(self, key):

        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class DowJones(VirtualBroker):
    def __init__(self):
        #creates window for GUI
        win = GraphWin("DowJones",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5,5),"wood.gif")
        bg.draw(self.win)


    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,.75,label))
        for b in self.buttons:
            b.activate()
            
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Dow Jones")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5,5),"DowJones.gif")
        graph.draw(self.win)

    def setScene(self):
        return MarketIndustryTrends 

    def processButton(self, key):

        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

class RusselTop200(VirtualBroker):
    def __init__(self):
        #creates window for GUI
        win = GraphWin("RusselTop200",700,500)
        win.setCoords(0,0,10,10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5,5),"wood.gif")
        bg.draw(self.win)


    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx,cy,label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win,Point(cx,cy),4,.75,label))
        for b in self.buttons:
            b.activate()
            
    def __createDisplay(self):
        head = Rectangle(Point(1.5,8),Point(8.5,9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5,8.5), "Russel Top 200")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5,5),"RusselTop200.gif")
        graph.draw(self.win)

    def setScene(self):
        return MarketIndustryTrends 

    def processButton(self, key):

        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()

###################################################################################################


Welcome() #  calls start

if __name__ == '__main__':
    theCalc1 = VirtualBroker()
    theCalc1.run()

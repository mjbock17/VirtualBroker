from graphics import *
from button import Button
import smtplib
import sys


class Welcome:  # First class, includes inputBar method
    def __init__(self):
        win = GraphWin("Welcome", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__makeJerry()
        self.__createDisplay()
        self.__createFile()
        self.win.close()

    def __bgimg(self):
        # sets background
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __makeJerry(self):  # imports jerry image, provides text
        c = Rectangle(Point(4.1, 2), Point(5.9, 6.6))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(5, 4.3), "myrodin.gif")
        image.draw(self.win)
        hello = Text(Point(7.8, 5.5), "Hello, my name is Jerry!")
        hello.setTextColor("white")
        hello.setStyle("bold")
        hello.setSize(16)
        hello.draw(self.win)

    def __createDisplay(self):
        # Creates title box
        textbox1 = Rectangle(Point(2.5, 7), Point(7.5, 9))
        textbox1.draw(self.win)
        textbox1.setFill("white")

        # Creates text for welcome
        welcometext = Text(Point(5, 8), "Welcome! \n Please enter your email")
        welcometext.setSize(20)
        welcometext.draw(self.win)
        self.welcometext = welcometext

        # Creates Textbox
        textbox2 = Rectangle(Point(3, .5), Point(7, 1.5))
        textbox2.setFill("white")
        textbox2.draw(self.win)

        # Creates text for input bar
        text1 = Text(Point(5, 1), "")
        text1.draw(self.win)
        self.textB = text1

    def __createFile(self):  # Creates file for storing info/stocks/portfolio
        while True:
            name = self.inputBar()
            if "@stolaf.edu" not in name and "@gmail.com" not in name:  # Checks for correct email formatting
                self.welcometext.setText('Please enter a valid email. \n I.E. @stolaf.edu or @gmail.com')
                self.welcometext.setSize(16)
            else:
                break
        global FileName  # necessary for integration across classes
        global email  # see above
        FileName = str(name) + ".txt"
        email = name
        stocklist = open(FileName, "w")
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
            if p == "period":  # adds a period
                index += "."
                self.textB.setText(" " + index)
                continue
            if p == "Shift_L" or p == "Shift_R":  # adds shift functionality
                self.textB.setText(" " + index)
                continue
            if p == "at":  # adds @ symbol
                index += "@"
                self.textB.setText(" " + index)
                continue
            index += str(p)  # Adds String
            self.textB.setText(" " + index)


class VirtualBroker:  # Hub of VB
    def __init__(self):
        win = GraphWin("Virtual Broker", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()  # Creates background images
        self.__createButtons()  # Creates buttons
        self.__createDisplay()  # Creates display

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):

        bsort = [(2, 1, "Email and Exit"), (7, 1.5, "Retirement Planning"), (7, 3, "Portfolio Management"),
                 (7, 4.5, "Market/Industry Trends"), (7, 6, "Stock Picking")]  # Creates buttons
        self.buttons = []
        for (cx, cy, label) in bsort:  # loop to process buttons
            if label == "Email and Exit":
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1.2, label))
                continue
            self.buttons.append(Button(self.win, Point(cx, cy), 4, 1.2, label))
        for b in self.buttons:
            b.activate()  # activates each button

    def __createDisplay(self):
        # Creates Textbox for heading
        bg = Rectangle(Point(1.4, 9.2), Point(8.6, 8.2))
        bg.setFill('white')
        bg.setOutline("gold")
        bg.setWidth(4)
        bg.draw(self.win)
        text = Text(Point(5, 8.7), "Welcome to Our Virtual Broker!")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(18)
        # Creates service text
        a = Line(Point(5, 7), Point(8.9, 7))
        a.draw(self.win)
        text1 = Text(Point(7, 7.2), "Please select a service:")
        text1.draw(self.win)
        text1.setFace("courier")
        text1.setStyle("bold")
        text1.setSize(14)
        # Creates box for Jerry
        c = Rectangle(Point(.5, 2), Point(3.5, 8))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Create Jerry
        image = Image(Point(2, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(2, 2.5), "Secure Your Future.")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        self.text2 = text2

    def __searchfile(self):  # obtains info from text file
        textL = self.__openfile()
        self.portfolio, self.stocks, self.retirement = self.__listextract(textL)
        if (self.portfolio or self.stocks or self.retirement) == False:  # Checks to see if self.portfolio, ect exists
            return False

    def __openfile(self):  # Opens file
        file1 = open(FileName, 'r')
        fileR = file1.read()
        text = fileR
        file1.close()
        list1 = text.split('\t')
        list1.pop()  # removes an empty value in the list
        list1.sort()
        return list1

    def __listextract(self, l1):  # extracts portfolio and stock information
        pt = False  # necessary initialization
        st = False
        rt = False
        for item in l1:
            if (pt and st and rt) == True:  # stops loop once both stocks and portfolio are found
                break
            if "Portfolio:" in item:
                pt = True
                continue
            if "Stock:" in item:
                st = True
                continue
            if "Retirement" in item:
                rt = True
                continue
        if pt == False or st == False or rt == False:  # if none are found, program ends--returns false
            return False, False, False
        portfolio = l1.pop(0)  # portfolio is first position in list
        retirement = l1.pop(0)  # Retirement is last in list
        stock = list()  # creates stock list
        for item in l1:  # adds stored stocks to list
            if "Stock" not in item:
                break
            else:
                stock.append(item)
        stockM = list()
        for item in stock:  # removes stock identifier
            edit = item[7:]
            stockM.append(edit)
        stocks = "\t".join(stockM)
        return portfolio, stocks, retirement

    def __email(self):
        self.__searchfile()
        logininfo = ['jerryvbroker@gmail.com', 'CS121AFinal']  # gmail account associated with Jerry

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # creates secure server
        server.ehlo()  # allows communication with server
        server.login(logininfo[0], logininfo[1])
        # email message
        server.sendmail(logininfo[0], email, "Here is your financial report!" + '\n\n'
                                             "Suggested Portfolio:" + self.portfolio[11:] + '\n\n'
                                             'Archived Stocks:' + self.stocks + '\n\n'
                                             'Suggested Retirement Plan: ' + self.retirement[12:] + '\n\n\n'
                                             'Good Luck!\n'
                                             'Jerry')
        server.close()

    def setScene(self):  # abstract method
        raise NotImplementedError("Subclass must implement abstract method")

    def getButton(self):  # uses loop to determine if button is clicked or not
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):  # processes button if clicked
        if key == 'Stock Picking':
            self.win.close()
            newin = stockpicking()
            while True:
                newin.run()  # necessary to run the next program
        elif key == 'Portfolio Management':
            self.win.close()
            newin = pmgmt()
            while True:
                newin.run()
        elif key == 'Market/Industry Trends':
            self.win.close()
            newin = MarketIndustryTrends()
            while True:
                newin.run()
        if key == 'Retirement Planning':
            self.win.close()
            newin = retirement()
            while True:
                newin.run()
        if key == 'Email and Exit':  # functions like try and except, ensures there is information in the text file.
            if self.__searchfile() == False:  # if so, it operates __email
                self.text2.setText("Error. Add stocks/portfolio")
                self.text2.setSize(9)
            else:
                self.__email()
                self.win.close()
                sys.exit()

    def run(self):  # runs infinite loop to keep process going. Stops all processes if window is closed!
        while True:
            if self.win.isClosed():
                break
            key = self.getButton()
            self.processButton(key)


#######################################################################
## Danny's Section
class stockpicking(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()  # stores last scene

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 2.5, "Grow Market Share"), (4, 5, "Retain Market Share")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))  # Creates a back button
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 2, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        #  Creates heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Q box
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.2), "Do you expect the company to retain its")
        question.draw(self.win)
        question.setSize(11)
        question.setFace('courier')
        question = Text(Point(3.8, 6.6), "market share or to grow its market share?")
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
        win = GraphWin("Stock Picking(2)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 3.25, "PE greater than or equal to 18"),
                 (4, 5, "PE less than 18, greater than zero"), (4, 1.5, "Negative/Zero PE")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1.5, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        #  creates heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        #  creates Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        #  creates QBOX
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.1), "What is the PE ratio?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question = Text(Point(3.8, 6.7), "(consult Yahoo Finance)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        if key == "PE greater than or equal to 18":
            self.win.close()
            newin = dontbuy()
            while True:
                newin.run()
        elif key == 'PE less than 18, greater than zero':
            self.win.close()
            newin = divyield()
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
        win = GraphWin("Stock Picking(3)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 3.25, "PE greater than or equal to 18"),
                 (4, 5, "PE less than 18, greater than zero"), (4, 1.5, "Negative/Zero PE")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1.5, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Creates Heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Stock Evaluation")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Creates Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Creates QBOX
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.1), "What is the PE ratio?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question = Text(Point(3.8, 6.7), "(consult Yahoo Finance)")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        if key == 'PE greater than or equal to 18':
            self.win.close()
            newin = analyst_opinion()
            while True:
                newin.run()
        elif key == 'PE less than 18, greater than zero':
            self.win.close()
            newin = dontbuy()
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
        win = GraphWin("Stock Picking(8)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 2.5, "Generally Negative"), (4, 5, "Generally Positive")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 2, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Create Heading
        head = Rectangle(Point(.15, 8), Point(9.85, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Financial Analyst's Opinions")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Create Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Create Qbox
        questionbox = Rectangle(Point(.15, 7.85), Point(6.9, 6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.55, 7.1),
                        "What is the general consensus between\nfinancial analysts on this stock?"
                        "\nDo they suggest a buy?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        if key == 'Generally Positive':
            self.win.close()
            newin = buy()
            while True:
                newin.run()
        elif key == 'Generally Negative':
            self.win.close()
            newin = dontbuy()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class strongreason(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(5)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 2.5, "No"), (4, 5, "Yes")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 2, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Create Heading
        head = Rectangle(Point(.3, 8), Point(9.7, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Stock Has Negative Earnings")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Create Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Create QBOX
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.25))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.1), "Are you certain that this")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question = Text(Point(3.8, 6.7), "company will recover and grow?")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        if key == 'Yes':
            self.win.close()
            newin = buy()
            while True:
                newin.run()
        elif key == 'No':
            self.win.close()
            newin = dontbuy()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class divyield(VirtualBroker, Welcome):
    def __init__(self):
        win = GraphWin("Stock Picking(6)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (2.8, 3.5, "Click to Enter")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Creates heading
        head = Rectangle(Point(.2, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(4.6, 8.5), "Dividend Analysis")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Creates Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Creates qbox
        questionbox = Rectangle(Point(.2, 7.5), Point(6.9, 6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.65, 6.8),
                        "Please enter this company's dividend \nyield ratio(if N/A enter 0) \nthen press enter")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def __createinputDisplay(self):
        box1 = Rectangle(Point(4, 3), Point(6, 4))  # textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6, 1.5), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5, 3.5), "")  # Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox  # creates a textbox variable
        self.error = Text(Point(4.5, 2.5), "ERROR. Please enter a numeric value")  # Creates incase of Error

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
        elif key == "Click to Enter":
            self.error.undraw()
            blink = Rectangle(Point(4.1, 4.1), Point(4.2, 4.2))  # notifies the user to type
            blink.setFill('red')
            blink.draw(self.win)
            information = self.inputBar()
            blink.undraw()
            try:
                divyield1 = float(information)
                if divyield1 > 1.5:  # Checks for desired ratio
                    self.win.close()
                    newin = buy()
                    while True:
                        newin.run()
                else:  # Non-float number
                    self.win.close()
                    newin = dontbuy()
                    while True:
                        newin.run()
            except:  # Necessary to get rid of win.closed error
                try:
                    self.error.draw(self.win)
                except:
                    sys.exit()


class dontbuy(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(4)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(2, 1, "Return to home page")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            self.buttons.append(Button(self.win, Point(cx, cy), 2.4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Create Heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "We Advise...")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Create Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Create Qbox
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.2))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.1), "to NOT buy this stock, for")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        question1 = Text(Point(3.8, 6.5), "one or more of these reasons:")
        question1.draw(self.win)
        question1.setSize(15)
        question1.setFace('courier')
        # Reason1
        reason1 = Text(Point(3.8, 5.8), "-The stock is most likely overpriced")
        reason1.draw(self.win)
        reason1.setSize(13)
        reason1.setFace('courier')
        # Reason 2
        reason2 = Text(Point(3.5, 5), "-Dividend income is insufficient")
        reason2.draw(self.win)
        reason2.setSize(13)
        reason2.setFace('courier')
        # Reason 3
        reason3 = Text(Point(3.5, 4.25), "-The stock is not likely to grow")
        reason3.draw(self.win)
        reason3.setSize(13)
        reason3.setFace('courier')
        # Reason 4
        reason4 = Text(Point(3.6, 3.3), "-This company is incurring a loss\nand is not expected to grow")
        reason4.draw(self.win)
        reason4.setSize(13)
        reason4.setFace('courier')

    def setScene(self):
        return VirtualBroker  # No need to go back to previous scene

    def processButton(self, key):
        if key == 'Return to home page':
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class buy(VirtualBroker):
    def __init__(self):
        win = GraphWin("Stock Picking(4)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()

    def __createButtons(self):
        bsort = [(2, 1, "Return to home page"), (3.8, 4.5, "Projected Earnings"), (3.8, 3, "Archive This Stockpick")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            self.buttons.append(Button(self.win, Point(cx, cy), 2.4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "We Advise...")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # QBox
        questionbox = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.8, 7.1), "To go ahead and BUY this stock")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')
        # Reason
        reason1 = Text(Point(3.8, 5.8), "Although we advise you to buy,\nearnings are never guaranteed")
        reason1.draw(self.win)
        reason1.setSize(13)
        reason1.setFace('courier')

    def setScene(self):
        return VirtualBroker

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
        elif key == 'Return to home page':
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class projearn(VirtualBroker, Welcome):
    def __init__(self):
        win = GraphWin("Stock Picking(10)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (3.4, 5.3, "Click to Enter")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Create Heading
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Projected Earnings")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Create Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Qbox
        questionbox = Rectangle(Point(.2, 7), Point(6.9, 6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.6, 6.5), "Please enter this company's current stock price")
        question.draw(self.win)
        question.setSize(11)
        question.setFace('courier')

    def __createinputDisplay(self):
        # inputBar Box
        box1 = Rectangle(Point(4.7, 4.8), Point(6.7, 5.8))  # textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6, 1.5), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5.7, 5.3), "")  # Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox  # creates a textbox variable
        self.error = Text(Point(4.5, 2.5), "ERROR. Please enter a numeric value")  # For try/except

    def setScene(self):
        return buy

    def processButton(self, key):
        if key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
        elif key == "Click to Enter":
            self.error.undraw()
            blink = Rectangle(Point(2.3, 5.8), Point(2.2, 5.9))  # notifies the user to type
            blink.setFill('red')
            blink.draw(self.win)
            information = self.inputBar()
            blink.undraw()
            try:  # Calculations. Ensures value is a float
                price = float(information)
                fiveper = price * 1.05 - price
                nfiveper = "%.2f" % fiveper
                tenper = price * 1.1 - price
                ntenper = "%.2f" % tenper
                fifteenper = price * 1.15 - price
                nfifteenper = "%.2f" % fifteenper
                twentyper = price * 1.2 - price
                ntwentyper = "%.2f" % twentyper
                five = Text(Point(4, 4), "-Earnings of five percent: $" + nfiveper)
                five.draw(self.win)
                ten = Text(Point(4, 3), "-Earnings of ten percent: $" + ntenper)
                ten.draw(self.win)
                fifteen = Text(Point(4, 2), "-Earnings of fifteen percent: $" + nfifteenper)
                fifteen.draw(self.win)
                twenty = Text(Point(4, 1), "-Earnings of twenty percent: $" + ntwentyper)
                twenty.draw(self.win)
            except:
                try:
                    self.error.draw(self.win)
                except:
                    sys.exit()


class filecreator(VirtualBroker, Welcome):  # appends to file
    def __init__(self):
        win = GraphWin("Stock Picking(11)", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.storedinfo = 0  # initializes value for archive button
        self.win = win
        self.__createstockDisplay()
        self.__createButtons()
        self.prevScene = self.setScene()
        self.__createinputDisplay()

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (2.8, 3.2, "Click to Enter 'ticker'"), (2.8, 4.5, "Click to Enter Name"),
                 (8, 1, 'Archive')]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2.2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        # Creates Heading
        head = Rectangle(Point(.2, 8), Point(9, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(4.6, 8.5), "Archive This Stockpick")
        title.draw(self.win)
        title.setSize(30)
        title.setFace("courier")
        title.setStyle("bold")
        c = Rectangle(Point(7, 2.5), Point(9, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        # Creates Jerry
        image = Image(Point(8, 5), "myrodin.gif")
        image.draw(self.win)
        # Creates QBOX
        questionbox = Rectangle(Point(.2, 7.5), Point(6.9, 6))
        questionbox.setFill('white')
        questionbox.draw(self.win)
        question = Text(Point(3.65, 6.8), "Please enter the company name\nand the stocks 'ticker'")
        question.draw(self.win)
        question.setSize(15)
        question.setFace('courier')

    def __createinputDisplay(self):
        box1 = Rectangle(Point(4, 4), Point(6, 5))  # textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox3 = Text(Point(5, 4.5), "")
        textbox3.setSize(10)
        textbox3.draw(self.win)
        textbox4 = Text(Point(5, 4.5), "")  # Creates a blank textbox
        textbox4.draw(self.win)
        self.textB = textbox4  # creates a textbox variable

        box2 = Rectangle(Point(4, 2.7), Point(6, 3.7))  # textbox
        box2.setFill("white")
        box2.draw(self.win)
        textbox2 = Text(Point(5, 3.2), "")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(5, 3.2), "")  # Creates a blank textbox
        textbox.draw(self.win)
        self.textA = textbox  # creates a textbox variable

        self.error = Text(Point(4.5, 2.5), "ERROR")  # Error for Try/except

    def __storeName(self, name):  # Method necessary to avoid global variable
        self.Name = name

    def __storeTicker(self, ticker):  # method necessary to avoid global variable
        self.Ticker = ticker

    def inputBar1(self):  # See previous inputBar documentation. Necessary for second textbox
        self.textA.setText("")
        index = ""  # Blank Message
        while True:
            p = self.win.getKey()
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) - 1]
                self.textA.setText(" " + index)
                continue
            if p == "space":
                index += " "
                continue
            if p == "period":
                index += "."
                self.textA.setText(" " + index)
                continue
            if p == "Shift_L" or p == "Shift_R":
                self.textA.setText(" " + index)
                continue
            index += str(p)
            self.textA.setText(" " + index)

    def setScene(self):
        return stockpicking

    def processButton(self, key):
        #  checks for info stored. No repeat Archive Button.
        if key == "Back" and self.storedinfo == 0:  # Archive not pressed
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()
        elif key == "Back" and self.storedinfo == 1:  # Archive pressed
            self.win.close()
            newin = VirtualBroker()
            while True:
                newin.run()
        elif key == "Click to Enter 'ticker'":  # Calls ticker name
            self.error.undraw()
            blink = Rectangle(Point(5.8, 3.8), Point(5.9, 3.9))  # notifies the user to type
            blink.setFill('red')
            blink.draw(self.win)
            ticker = self.inputBar1()
            blink.undraw()
            self.__storeTicker(ticker)
        elif key == "Click to Enter Name":
            self.error.undraw()
            blink1 = Rectangle(Point(5.8, 5.1), Point(5.9, 5.2))
            blink1.setFill('red')
            blink1.draw(self.win)
            name = self.inputBar()
            blink1.undraw()
            self.__storeName(name)
        elif key == "Archive" and self.storedinfo == 0:
            self.error.undraw()
            try:
                self.fileadd(self.Name, self.Ticker)  # Ensures values are in textbox
                self.storedinfo = +1
            except:
                try:
                    self.error.draw(self.win)
                except:
                    sys.exit()

    def fileadd(self, name, ticker):  # appends to file
        fileappend = open(FileName, 'a')  # calls global variable FileName
        fileappend.write("Stock: " + str(name) + " " + str(ticker) + '\t')
        fileappend.close()
        stored = Text(Point(5, 2), "Your file has been stored. \n Please click 'Back' to return to the main menu")
        stored.setSize(10)
        stored.draw(self.win)


#########################################################################################
# Henrik's Section

class pmgmt(VirtualBroker, Welcome):
    def __init__(self):
        win = GraphWin("Portfolio Management", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()  # objects in the constructor are called and activated before the user clicks
        self.__createstockDisplay()
        self.__createinputDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()  # sets up variable for back button

    def __createinputDisplay(self):
        box1 = Rectangle(Point(3, 1), Point(9, 2))  # textbox
        box1.setFill("white")
        box1.draw(self.win)
        textbox2 = Text(Point(4.6, 1.5), "enter a risk level between 0 and 100")
        textbox2.setSize(10)
        textbox2.draw(self.win)
        textbox = Text(Point(7.5, 1.5), "")  # Creates a blank textbox
        textbox.draw(self.win)
        self.textB = textbox  # creates a textbox variable

        self.error = Text(Point(6, .6), "ERROR. Please enter a numeric value")  # activates if non str

    def __bgimg(self):  # sets the gradient background
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Back"), (2.2, 3.1, "enter text")]
        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Back":  # creates back button
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()  # activate the buttons

    def __makeJerry(self):  # creates jerry image and text
        c = Rectangle(Point(4, 2.5), Point(6, 7.5))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(5, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(5, 7.8), "One must spend money to make it")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)

    def __createstockDisplay(self):  # creates display at the top of the window
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "What Level of Risk Will You Accept?")  #
        title.draw(self.win)
        title.setSize(15)  #
        title.setStyle("bold")

    def setScene(self):  # determines the screeen the backbutton will affect
        return VirtualBroker

    def processButton(self, key):
        # Updates the display for press of this key
        if key == 'enter text':
            self.error.undraw()
            blink = Rectangle(Point(2.5, 2.1), Point(2.6, 2.2))  # notifies the user to type
            blink.setFill('red')
            blink.draw(self.win)
            information = self.inputBar()  # saves the info for the if conditional
            blink.undraw()
            try:
                newinfo = int(information)
                if 50 <= newinfo:
                    self.win.close()
                    newin = highrisk()  # opens the next window
                    while True:
                        newin.run()
                elif newinfo < 50:
                    self.win.close()
                    newin = lowrisk()
                    while True:
                        newin.run()
            except:
                try:
                    self.error.draw(self.win)
                except:
                    sys.exit()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()  # looks for the variable that the back button should go to
            while True:
                newin.run()


class highrisk(VirtualBroker):
    def __init__(self):
        win = GraphWin("High Risk", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):  # creates small display far right side of screen
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Back"), (1.5, 6, 'Long Term'),
                  (1.5, 4.5, 'Short Term')]

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "High Risk Portfolio")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):  # imports the graphic for the window
        a = Rectangle(Point(5.25, 2.7), Point(9.725, 7.25))
        a.setFill("Light Steel Blue")
        a.setOutline("gold")
        a.draw(self.win)
        graph = Image(Point(7.5, 5), "sp500.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(2.8, 2.7), Point(4.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(3.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(3.1, 2.5), "Try the Stock Market!")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(3.3, 2.2), "I recommend a shorter horizon")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return pmgmt  # the back button will now return pmgmt

    def processButton(self, key):
        if key == 'Long Term':
            fileappend = open(FileName, 'a')  # opens the user save file and appends the portfolio stats
            fileappend.write("Portfolio: Stocks: 70%, Bonds: 25%, Cash: 5%, expected return 6 years 20% +/- 10%\t")
            fileappend.close()
            self.win.close()
            newin = hrlt()
            while True:
                newin.run()
        if key == 'Short Term':
            fileappend = open(FileName, 'a')  # user save file
            fileappend.write("Portfolio: Stocks: 80%, Bonds: 15%, Cash: 5%, expected return 3 years 24% +/- 19%\t")
            fileappend.close()
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
        win = GraphWin("Low Risk", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Back"), (1.5, 6, 'Long Term'),
                  (1.5, 4.5, 'Short Term')]

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Low Risk Portfolio")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(5.25, 2.7), Point(9.725, 7.25))
        a.setFill("Light Steel Blue")
        a.setOutline("gold")
        a.draw(self.win)
        graph = Image(Point(7.5, 5), "10yeart.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(2.8, 2.7), Point(4.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(3.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(3.1, 2.5), "You're not a risk taker")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(3.3, 2.2), "I recommend a longer horizon")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return pmgmt

    def processButton(self, key):
        if key == 'Long Term':
            fileappend = open(FileName, 'a')  # user save file
            fileappend.write("Portfolio: Stocks: 40%, Bonds: 50%, Cash: 10%, expected return 12 years 8% +/- 2%\t")
            fileappend.close()
            self.win.close()
            newin = lrlt()
            while True:
                newin.run()
        if key == 'Short Term':
            fileappend = open(FileName, 'a')  # user save file
            fileappend.write("Portfolio: Stocks: 50%, Bonds: 40%, Cash: 10%, expected return 3 years 4% +/- 1%\t")
            fileappend.close()
            self.win.close()
            newin = lrst()
            while True:
                newin.run()
        elif key == "Back":
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class hrlt(VirtualBroker):  # final user screen
    def __init__(self):
        win = GraphWin("hrlt", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]  # back button now called home, return pmgmt

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "High Risk Long Term")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(3.7, 1), Point(9.3, 7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5, 4), "hrlt.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(0.8, 2.7), Point(2.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8, 2.5), "Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2, 2.2), "that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker

    def processButton(self, key):
        if key == "Home":  # back button now called home, return pmgmt
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class hrst(VirtualBroker):  # final user screen
    def __init__(self):
        win = GraphWin("hrst", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]  # back button now called home, return pmgmt

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Home":  # back button now called home
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "High Risk Short Term")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(3.7, 1), Point(9.3, 7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5, 4), "hrst.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(0.8, 2.7), Point(2.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8, 2.5), "Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2, 2.2), "that I generated for you!")
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


class lrlt(VirtualBroker):  # final user screen
    def __init__(self):
        win = GraphWin("lrlt", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Home":  # back button now called home, return pmgmt
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Low Risk Long Term")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(3.7, 1), Point(9.3, 7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5, 4), "lrlt.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(0.8, 2.7), Point(2.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8, 2.5), "Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2, 2.2), "that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker

    def processButton(self, key):
        if key == "Home":  # back button now called home, return pmgmt
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class lrst(VirtualBroker):  # final user screen
    def __init__(self):
        win = GraphWin("lrst", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createstockDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "gradient.gif")
        bg.draw(self.win)

    def __minidsplay(self):
        head = Rectangle(Point(9, 1), Point(9.5, 7))
        head.setFill('white')
        head.draw(self.win)

    def __createButtons(self):
        aSpecs = [(1, 1, "Home")]  # back button now called home, return pmgmt

        self.buttons = []
        for (cx, cy, label) in aSpecs:
            if label == "Home":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 2, 1, label))
        for b in self.buttons:
            b.activate()

    def __createstockDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Low Risk Short Term")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        a = Rectangle(Point(3.7, 1), Point(9.3, 7))
        a.setFill("black")
        a.draw(self.win)
        graph = Image(Point(6.5, 4), "lrst.gif")
        graph.draw(self.win)

    def __makeJerry(self):
        myrec = Rectangle(Point(0.8, 2.7), Point(2.8, 7.3))
        myrec.setFill("gold")
        myrec.draw(self.win)
        image = Image(Point(1.8, 5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(1.8, 2.5), "Here's the portfolio")
        text2.setTextColor('white')
        text2.setSize(10)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)
        text3 = Text(Point(2, 2.2), "that I generated for you!")
        text3.setTextColor('white')
        text3.setSize(10)
        text3.setFace("courier")
        text3.setStyle("bold")
        text3.draw(self.win)

    def setScene(self):
        return VirtualBroker

    def processButton(self, key):
        if key == "Home":  # back button now called home, return pmgmt
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


###################################################################################################
class MarketIndustryTrends(VirtualBroker):
    def __init__(self):
        # creates window for GUI
        win = GraphWin("Market/Industry Trends", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        # background image
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):

        # creates the list of buttons
        bsort = [(1, 1, "Back"), (3, 6.25, "S&P 500"), (3, 5, "Dow Jones"),
                 (3, 3.75, "NASDAQ"), (3, 2.5, "Russel Top 200")]
        self.buttons = []
        # creates the odd shaped buttons
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, .75, label))
        # activates all buttons
        for b in self.buttons:
            b.activate()

    def __makeJerry(self):
        # Creates the assistant Jerry
        c = Rectangle(Point(6.5, 2), Point(8.5, 7))
        c.setFill('black')
        c.setOutline('gold')
        c.setWidth(4)
        c.draw(self.win)
        image = Image(Point(7.5, 4.5), "myrodin.gif")
        image.draw(self.win)
        text2 = Text(Point(7.5, 1.5), "Please select a Market \n to view its index.")
        text2.setTextColor('white')
        text2.setSize(15)
        text2.setFace("courier")
        text2.setStyle("bold")
        text2.draw(self.win)

    def __createDisplay(self):
        # Creates Title
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Market/Industry Trends")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def setScene(self):
        # Back button calls on previous class
        return VirtualBroker

    def processButton(self, key):
        # selection of specific markets
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

class SandP500(VirtualBroker):
    # Displays the SandP500 data
    def __init__(self):
        # creates window for GUI
        win = GraphWin("SandP500", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, .75, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "S&P500")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5, 5), "sandp500.gif")
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
    # Creates the image for Nasdaq
    def __init__(self):
        # creates window for GUI
        win = GraphWin("Nasdaq", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, .75, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "NASDAQ")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5, 5), "nasdaq.gif")
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
    # Displays the index information for Dow Jones
    def __init__(self):
        # creates window for GUI
        win = GraphWin("DowJones", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, .75, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Dow Jones")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5, 5), "DowJones.gif")
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
    # Displays the index information for Russel Top 200
    def __init__(self):
        # creates window for GUI
        win = GraphWin("RusselTop200", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__graph()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, .75, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1.5, 8), Point(8.5, 9))
        head.setFill('white')
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Russel Top 200")
        title.draw(self.win)
        title.setSize(15)
        title.setStyle("bold")

    def __graph(self):
        graph = Image(Point(5, 5), "RusselTop200.gif")
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
class retirement(VirtualBroker):
    def __init__(self):
        # creates window for GUI, the initial page for all of the retirement planning subpages
        win = GraphWin("Retirement Planning", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createButtons()
        self.__createDisplay()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        # creates the background image, using the "wood" picture
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        # creates all of the buttons, setting up the subsequent pathways
        bsort = [(1, 1, "Back"), (4, 1.5, "51-70 Years Old"), (4, 3.5, "31-50 Years Old"), (4, 5.5, "18-30 Years Old")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        # creates the display for the retirement planning page
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Age Evaluation")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        ageInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        ageInput.setFill('white')
        ageInput.setOutline('gold')
        ageInput.draw(self.win)
        ageText = Text(Point(3.8, 7.2), "How old are you?")
        ageText.draw(self.win)
        ageText.setSize(18)
        ageText.setFace('courier')

    def __makeJerry(self):
        # creates Jerry, the financial advisor
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        # abstract class that allows for a back button
        return VirtualBroker

    def processButton(self, key):
        # allows the buttons to be pressed and moved to the next page in the pathway
        if key == '18-30 Years Old':
            global age
            age = 1
            self.win.close()
            newin = income()
            while True:
                newin.run()
        elif key == '31-50 Years Old':
            age = 2
            self.win.close()
            newin = income()
            while True:
                newin.run()
        elif key == '51-70 Years Old':
            age = 3
            self.win.close()
            newin = income()
            while True:
                newin.run()
        elif key == 'Back':
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class income(VirtualBroker):
    def __init__(self):
        # creates window for Income GUI
        win = GraphWin("Income Inquiry", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 1.5, "Greater than $132,000"), (4, 3.5, "Between $50,001 and $132,000"),
                 (4, 5.5, "$50,000 or less")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Income Evaluation")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        incomeInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        incomeInput.setFill('white')
        incomeInput.setOutline('gold')
        incomeInput.draw(self.win)
        incomeText = Text(Point(3.8, 7.2), "What is your yearly income?")
        incomeText.draw(self.win)
        incomeText.setSize(18)
        incomeText.setFace('courier')

    def __makeJerry(self):
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        return retirement

    def processButton(self, key):
        if key == "Greater than $132,000":
            global income1
            income1 = 1
            self.win.close()
            newin = employment()
            while True:
                newin.run()
        elif key == "Between $50,001 and $132,000":
            income1 = 2
            self.win.close()
            newin = employment()
            while True:
                newin.run()
        elif key == "$50,000 or less":
            income1 = 3
            self.win.close()
            newin = employment()
            while True:
                newin.run()
        elif key == 'Back':
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class employment(VirtualBroker):
    def __init__(self):
        # creates window for Employment GUI
        win = GraphWin("Employment Evaluation", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Back"), (4, 1.5, "Self-Employed"), (4, 3.5, "Employed: Employer NO 401K Match"),
                 (4, 5.5, "Employed: Employer 401K Match")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Back":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Employment Evaluation")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        employmentInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        employmentInput.setFill('white')
        employmentInput.setOutline('gold')
        employmentInput.draw(self.win)
        employmentText = Text(Point(3.8, 7.2), "What is your employment status?")
        employmentText.draw(self.win)
        employmentText.setSize(15)
        employmentText.setFace('courier')

    def __makeJerry(self):
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        return income

    def processButton(self, key):
        if key == "Employed: Employer 401K Match":
            self.win.close()
            newin = FourO()
            while True:
                newin.run()
        elif key == "Employed: Employer NO 401K Match":
            self.win.close()
            newin = RothIRA()
            while True:
                newin.run()
        elif key == "Self-Employed":
            self.win.close()
            newin = IRA()
            while True:
                newin.run()
        elif key == 'Back':
            self.win.close()
            newin = self.prevScene()
            while True:
                newin.run()


class FourO(VirtualBroker):
    def __init__(self):
        # creates window for  401K GUI
        win = GraphWin("401K", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Home")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Home":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "401(K)")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        FourOInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        FourOInput.setFill('white')
        FourOInput.setOutline('gold')
        FourOInput.draw(self.win)
        FourOText = Text(Point(3.8, 7.2), "You should choose a 401(K)!")
        FourOText.draw(self.win)
        FourOText.setSize(18)
        FourOText.setFace('courier')
        benefit = Rectangle(Point(1, 6), Point(6.75, 2))
        benefit.setFill('white')
        benefit.setOutline('gold')
        benefit.draw(self.win)
        benefitText = Text(Point(4, 4), """
-A 401(k) is a retirement savings plan\n
sponsored by an employer.\n
-It lets workers save and invest a piece\n
of their paycheck before taxes are taken out.\n
-Taxes aren’t paid until the money is withdrawn\n
from the account.""")
        benefitText.draw(self.win)
        benefitText.setSize(8)
        benefitText.setFace('courier')
        benefitText.setStyle('bold')

    def __makeJerry(self):
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        return income

    def processButton(self, key):
        if key == "Home":
            self.win.close()
            fileappend = open(FileName, 'a')  # calls global variable FileName
            fileappend.write("Retirement: " + '401(k)' + '\t')
            fileappend.close()
            newin = VirtualBroker()
            while True:
                newin.run()


class RothIRA(VirtualBroker):
    def __init__(self):
        # creates window for Roth IRA GUI
        win = GraphWin("Roth IRA", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Home")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Home":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Roth IRA")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        RothInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        RothInput.setFill('white')
        RothInput.setOutline('gold')
        RothInput.draw(self.win)
        RothText = Text(Point(3.8, 7.2), "You should choose a Roth IRA!")
        RothText.draw(self.win)
        RothText.setSize(16)
        RothText.setFace('courier')
        benefit = Rectangle(Point(1, 6), Point(6.75, 2))
        benefit.setFill('white')
        benefit.setOutline('gold')
        benefit.draw(self.win)
        benefitText = Text(Point(4, 4), """
-A Roth IRA is a retirement plan under US law\n
that is generally not taxed.\n
-The Roth IRA's main difference from retirement\n
plans is that tax breaks are granted on the money\n
withdrawn from the plan during retirement.\n
-Direct contributions to a Roth IRA may be \n
withdrawn tax and penalty-free at any time.""")
        benefitText.draw(self.win)
        benefitText.setSize(8)
        benefitText.setFace('courier')
        benefitText.setStyle('bold')

    def __makeJerry(self):
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        return income

    def processButton(self, key):
        if key == "Home":
            self.win.close()
            fileappend = open(FileName, 'a')  # calls global variable FileName
            fileappend.write("Retirement: " + 'Roth IRA' + '\t') # Adds type of retirement plan
            fileappend.close()
            newin = VirtualBroker()
            while True:
                newin.run()


class IRA(VirtualBroker):
    def __init__(self):
        # creates window for IRA GUI
        win = GraphWin("Traditional IRA", 700, 500)
        win.setCoords(0, 0, 10, 10)
        win.setBackground("slategray")
        self.win = win
        self.__bgimg()
        self.__createDisplay()
        self.__createButtons()
        self.__makeJerry()
        self.prevScene = self.setScene()

    def __bgimg(self):
        bg = Image(Point(5, 5), "wood.gif")
        bg.draw(self.win)

    def __createButtons(self):
        bsort = [(1, 1, "Home")]
        self.buttons = []
        for (cx, cy, label) in bsort:
            if label == "Home":
                self.buttons.append(Button(self.win, Point(cx, cy), 1, 1, label))
            else:
                self.buttons.append(Button(self.win, Point(cx, cy), 4, 1, label))
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        head = Rectangle(Point(1, 8), Point(9, 9))
        head.setFill('white')
        head.setOutline('gold')
        head.setWidth(4)
        head.draw(self.win)
        title = Text(Point(5, 8.5), "Traditional IRA")
        title.draw(self.win)
        title.setSize(28)
        title.setFace('courier')
        title.setStyle('bold')
        IRAInput = Rectangle(Point(1, 7.5), Point(6.75, 6.75))
        IRAInput.setFill('white')
        IRAInput.setOutline('gold')
        IRAInput.draw(self.win)
        IRAText = Text(Point(3.9, 7.2), "You should choose a traditional IRA!")
        IRAText.draw(self.win)
        IRAText.setSize(14)
        IRAText.setFace('courier')
        benefit = Rectangle(Point(1, 6), Point(6.75, 2))
        benefit.setFill('white')
        benefit.setOutline('gold')
        benefit.draw(self.win)
        benefitText = Text(Point(4, 4), """
-A Traditional IRA, or individual retirement \n
arrangement, is held at banks or brokerages \n
and can be invested in an assortment of \n
stocks,mutual funds and indices. \n
-IRA’s are tax deferred savings plans, meaning\n
that the money you invest is larger than other\n
post-tax savings plans.""")
        benefitText.draw(self.win)
        benefitText.setSize(8)
        benefitText.setFace('courier')
        benefitText.setStyle('bold')

    def __makeJerry(self):
        jerry = Rectangle(Point(7, 1.5), Point(9, 6.5))
        jerry.setFill('black')
        jerry.setOutline('gold')
        jerry.setWidth(4)
        jerry.draw(self.win)
        image = Image(Point(8, 4), "myrodin.gif")
        image.draw(self.win)

    def setScene(self):
        return income

    def processButton(self, key):
        if key == "Home":
            self.win.close()
            fileappend = open(FileName, 'a')  # calls global variable FileName # Adds retirement plan
            fileappend.write("Retirement: " + 'Traditional IRA' + '\t')
            fileappend.close()
            newin = VirtualBroker()
            while True:
                newin.run()

###################################################################################################


Welcome()  # calls start
if __name__ == '__main__':
    virtualB = VirtualBroker()
    virtualB.run()

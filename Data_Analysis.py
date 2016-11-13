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

if __name__ == '__main__':
    theCalc = Data_Analysis() #name change from sortsearch
    theCalc.run()

        
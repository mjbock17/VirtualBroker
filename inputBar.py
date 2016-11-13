    def inputBar(self):    ###Need to create a textbox before using a 
        index = "" ###Blank Message
        while True:
            p = self.win.getKey() ###Gets key pressed. Replace win with object
            if p == "Return":
                return index
            if p == "BackSpace":
                index = index[0:len(index) -1] ###Removes last item
                self.text.setText(message + " " + index)
                continue
            index = index + str(p) ###Adds String
            self.text.setText(message + " " + index) ###Replace self.text with made textbox

from tkinter import *

class MyApp:  ### (1)
    def __init__(self, myParent):  ### (1a)
        self.myContainer1 = Frame(myParent)
        self.myContainer1.pack()
        
        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"
        self.button1.pack()

root = Tk()
myapp = MyApp(root)  ### (2)
root.mainloop()  ### (3)

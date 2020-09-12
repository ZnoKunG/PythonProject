from tkinter import *

def sayHelloWorld():
    print("Hello World")

MainWindow = Tk()
button = Button(MainWindow,text = "Click me 1",command = sayHelloWorld).grid(row=0,column=1)
button2 = Button(MainWindow,text = "Click me 2",command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow,text = "Click me 3",command = sayHelloWorld).grid(row=0,column=2)
MainWindow.mainloop()
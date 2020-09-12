from tkinter import *

def sayHelloWorld():
    print("Hello World")

MainWindow = Tk()
button = Button(MainWindow,text = "Click me 1",command = sayHelloWorld,width=20,height=20).grid(row=2,column=1)
button2 = Button(MainWindow,text = "Click me 2",command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow,text = "Click me 3",command = sayHelloWorld).grid(row=0,column=2)
label = Label(MainWindow,text = "Hello World",width=20,fg = "red",bg = "#ffc000").grid(row=0,column=1)
MainWindow.mainloop()
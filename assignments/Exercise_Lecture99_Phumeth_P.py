from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if bmi >= 30:
        rangeBmi = "อ้วนมาก"
    elif bmi >= 25.0:
        rangeBmi = "อ้วน"
    elif bmi >= 23.0:
        rangeBmi = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        rangeBmi = "น้ำหนักปกติ เหมาะสม"
    elif bmi <= 18.5:
        rangeBmi = "ผอมเกินไป"
    labelResult.configure(text=bmi)
    labelResult2.configure(text=rangeBmi)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow,text="")
labelResult2.grid(row=3,column=1)

MainWindow.mainloop()
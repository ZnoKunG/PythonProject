from tkinter import *
import math

def calculate(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if BMI >=30.0:
        labelResult.configure(text='อ้วนมาก')
    elif 25.0 <= BMI < 30:
        labelResult.configure(text='อ้วน')
    elif 23.0 <= BMI < 25:
        labelResult.configure(text='น้ำหนักเกิน')
    elif 18.6 <= BMI < 23:
        labelResult.configure(text='น้ำหนักปกติ เหมาะสม')
    elif BMI < 18.6:
        labelResult.configure(text='ผอมเกินไป')


MainWindow = Tk()
labelProgramName = Label(MainWindow,text = "   โปรแกรมคำนวณ BMI    ",anchor=CENTER)
labelProgramName.grid(row=0,column=0)
labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.) :")
labelHeight.grid(row=1,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=1,column=1)
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.) :")
labelWeight.grid(row=2,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=2,column=1)
calculateButton = Button(text = "คำนวณ")
calculateButton.grid(row=3,column=0)
calculateButton.bind('<Button-1>',calculate)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=3,column=1)
MainWindow.mainloop()
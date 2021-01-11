import tkinter as tk
from forex_python.converter import CurrencyRates

c = CurrencyRates()

def USD_to_THB():
    USD = int(ent_currency.get())
    result = c.convert("USD","THB", USD)
    lbl_result["text"] = f"{round(result,2)} THB"

window = tk.Tk()
window.title("Converting Currency Program")
frame = tk.Frame( master = window )
ent_currency = tk.Entry(master = frame, width = 12)
lbl_usd = tk.Label(master = frame, text = "USD")

ent_currency.grid(row=0,column = 0)
lbl_usd.grid(row=0,column=1)

btn_convert = tk.Button(master=window, text = "\N{RIGHTWARDS BLACK ARROW}",command = USD_to_THB)
lbl_result = tk.Label(master=window, text = "THB")

frame.grid(row=0,column=0,padx=0)
btn_convert.grid(row=0,column=1,pady=10)
lbl_result.grid(row=0,column=2,padx=10)

window.mainloop()
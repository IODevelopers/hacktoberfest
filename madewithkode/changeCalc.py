'''A Python Program to calculate change after item purchase'''
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Change Calculator") # title
root.resizable(0, 0) # if you want it resizeable, just remove this whole line

Price_sv = tk.StringVar()
ammount_sv = tk.StringVar()

def onReset(*event):
    Price_sv.set("")
    ammount_sv.set("")



def OnSubmit(*event):
    Price = Price_sv.get()
    ammount = ammount_sv.get()
    Price = int(Price)
    ammount = int(ammount)
    change = ammount - Price
    if ammount < Price:
        mb.showerror("Error", "You do not have enough money to purchase Product!")
    elif ammount == Price:
        mb.showerror("Error", "You have no change!")
    else:
        mb.showerror("Change", "your change is: \n "+ str(change) +" Naira")
        return


#add GUI
Pricelabel = tk.Label(root, text="Item Price: ").grid(row=0, column=0, padx=10, pady=10, sticky='w')
Priceentry = tk.Entry(root, textvariable=Price_sv).grid(row=0, column=1, padx=10, pady=1-0)

ammountlabel = tk.Label(root, text="Customer Paid: ").grid(row=1, column=0, padx=10, pady=10, sticky='w')
ammountentry = tk.Entry(root, textvariable=ammount_sv).grid(row=1, column=1, padx=10, pady=10)

submitButton = tk.Button(root, text="Submit", command=OnSubmit).grid(row=2, column=0, padx=10, pady=10, sticky='w')
resetbutton = tk.Button(root, text="Reset", command=onReset).grid(row=2, column=1, padx=10, pady=10, sticky='e')

root.mainloop()

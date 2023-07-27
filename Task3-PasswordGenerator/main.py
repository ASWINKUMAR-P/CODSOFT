from tkinter import *
from tkinter import messagebox
import random


def generate(size,sym,num,low,upp):
    if size.get()=="":
        messagebox.showerror("Error","Please enter the length of the password")
        return
    try:
        size = int(size.get())
    except:
        messagebox.showerror("Error","Please enter a valid length")
        return
    if size>15:
        messagebox.showerror("Error","Please enter a length less than 15")
        return
    allchar=""
    if sym.get()==1:
        allchar+="!@#$%^&*()_+"
    if num.get()==1:
        allchar+="1234567890"
    if low.get()==1:
        allchar+="abcdefghijklmnopqrstuvwxyz"
    if upp.get()==1:
        allchar+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(allchar)==0:
        messagebox.showerror("Error","Please select atleast one option")
        return
    password=random.sample(allchar,size)
    password="".join(password)
    result.set(password)
    
window = Tk()
window.title("Password Generator")
window.resizable(False, False)

Label(window, text="Password Generator", font=("Times New Roman", 20, "bold"),anchor="center").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
Label(window, text="Enter the length of the password to be generated: ", font=("Times New Roman", 15)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
size = Entry(window, font=("Times New Roman", 15), width=5)
size.grid(row=1, column=1, padx=10, pady=10, sticky="w")
sym = IntVar()
Checkbutton(window, text="Include Symbols", font=("Times New Roman", 15),variable=sym).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")
num = IntVar()
Checkbutton(window, text="Include Numbers", font=("Times New Roman", 15),variable=num).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")
low = IntVar()
Checkbutton(window, text="Include Lowercase Characters", font=("Times New Roman", 15),variable=low).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")
upp = IntVar()
Checkbutton(window, text="Include Uppercase Characters", font=("Times New Roman", 15),variable=upp).grid(row=5, column=0,  columnspan=2,padx=10, pady=10, sticky="w")
Button(window, text="Generate Password", font=("Times New Roman", 15),command = lambda:generate(size,sym,num,low,upp)).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="w")
Label(window, text="The generated password is:- ",font=("Times New Roman", 15)).grid(row=7, column=0, padx=10, pady=10, sticky="w")
result = Entry(window, text="",font=("Times New Roman", 15),width=20,state="readonly")
result.grid(row=7, column=1, padx=10, pady=10, sticky="w")

window.mainloop()
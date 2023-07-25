import tkinter as tk

display="0"

def button_click(number):
    global display
    if display == "0":
        display = ""
    if len(display)!=0 and display[-1] in "+-*/" and number=="0":
        return
    display += str(number)
    screen.config(text=display)

def button_clear():
    global display
    display = "0"
    screen.config(text=display)

def button_equal():
    global display
    try:
        display = str(eval(display))
    except:
        display = "Math Error"
    screen.config(text=display)

def button_delete():
    global display
    display = display[:-1]
    screen.config(text=display)


calc = tk.Tk()
calc.title("Calculator")
calc.resizable(False, False)
screen = tk.Label(calc, width=40,text="0",fg="#ffffff",height =2,borderwidth=5,bg="black",anchor="se")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Button(calc, text="AC", width=10, pady=20, bg="red", fg="white", command=lambda:button_clear()).grid(row=1, column=0)
tk.Button(calc, text="DEL", width=10, pady=20, bg="black", fg="white", command=lambda:button_delete()).grid(row=1, column=1)
tk.Button(calc, text=".", width=10, pady=20, bg="black", fg="white",command=lambda:button_click(".")).grid(row=1, column=2)
tk.Button(calc, text="/", width=10, pady=20, bg="white", fg="black",command=lambda:button_click("/")).grid(row=1, column=3)

tk.Button(calc, text="7", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("7")).grid(row=2, column=0)
tk.Button(calc, text="8", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("8")).grid(row=2, column=1)
tk.Button(calc, text="9", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("9")).grid(row=2, column=2)
tk.Button(calc, text="*", width=10, pady=20, bg="white", fg="black",command=lambda:button_click("*")).grid(row=2, column=3)

tk.Button(calc, text="4", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("4")).grid(row=3, column=0)
tk.Button(calc, text="5", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("5")).grid(row=3, column=1)
tk.Button(calc, text="6", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("6")).grid(row=3, column=2)
tk.Button(calc, text="-", width=10, pady=20, bg="white", fg="black",command=lambda:button_click("-")).grid(row=3, column=3)

tk.Button(calc, text="1", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("1")).grid(row=4, column=0)
tk.Button(calc, text="2", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("2")).grid(row=4, column=1)
tk.Button(calc, text="3", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("3")).grid(row=4, column=2)
tk.Button(calc, text="+", width=10, pady=20, bg="white", fg="black",command=lambda:button_click("+")).grid(row=4, column=3)

tk.Button(calc, text="(", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("(")).grid(row=5, column=0)
tk.Button(calc, text="0", width=10, pady=20, bg="black", fg="white",command=lambda:button_click("0")).grid(row=5, column=1)
tk.Button(calc, text=")", width=10, pady=20, bg="black", fg="white",command=lambda:button_click(")")).grid(row=5, column=2)
tk.Button(calc, text="=", width=10, pady=20, bg="blue", fg="white", command=lambda:button_equal()).grid(row=5, column=3)

calc.mainloop()
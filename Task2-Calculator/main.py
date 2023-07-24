import tkinter as tk

calc = tk.Tk()
calc.title("Calculator")
calc.resizable(False, False)
tk.Label(calc, width=40, borderwidth=5,bg="black").grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Button(calc, text="C", width=10, pady=20).grid(row=1, column=0)
tk.Button(calc, text=".", width=10, pady=20).grid(row=1, column=1)
tk.Button(calc, text="%", width=10, pady=20).grid(row=1, column=2)
tk.Button(calc, text="/", width=10, pady=20).grid(row=1, column=3)

tk.Button(calc, text="7", width=10, pady=20).grid(row=2, column=0)
tk.Button(calc, text="8", width=10, pady=20).grid(row=2, column=1)
tk.Button(calc, text="9", width=10, pady=20).grid(row=2, column=2)
tk.Button(calc, text="*", width=10, pady=20).grid(row=2, column=3)

tk.Button(calc, text="4", width=10, pady=20).grid(row=3, column=0)
tk.Button(calc, text="5", width=10, pady=20).grid(row=3, column=1)
tk.Button(calc, text="6", width=10, pady=20).grid(row=3, column=2)
tk.Button(calc, text="-", width=10, pady=20).grid(row=3, column=3)

tk.Button(calc, text="1", width=10, pady=20).grid(row=4, column=0)
tk.Button(calc, text="2", width=10, pady=20).grid(row=4, column=1)
tk.Button(calc, text="3", width=10, pady=20).grid(row=4, column=2)
tk.Button(calc, text="+", width=10, pady=20).grid(row=4, column=3)

tk.Button(calc, text="(", width=10, pady=20).grid(row=5, column=0)
tk.Button(calc, text="0", width=10, pady=20).grid(row=5, column=1)
tk.Button(calc, text=")", width=10, pady=20).grid(row=5, column=2)
tk.Button(calc, text="=", width=10, pady=20).grid(row=5, column=3)

calc.mainloop()

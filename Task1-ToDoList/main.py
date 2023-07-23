import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
import sqlite3

def add(task):
    pass

def remove(id):
    pass

home=tk.Tk()
home.geometry('500x500')
home.resizable(False,False)
home.title("Task manager")

mydb = sqlite3.connect('todolist.db')
cur = mydb.cursor()
try:
    cur.execute("create table task(id integer primary key autoincrement,task text,status text)")
except:
    pass

frame=ttk.Frame(home)
frame.pack(fill=BOTH,expand=1)

my_canvas=tk.Canvas(frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar=ttk.Scrollbar(frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

main_frame=ttk.Frame(my_canvas)
my_canvas.create_window((0,0),window=main_frame,anchor="nw")

head = tk.Label(main_frame,text="Task Manager",font=("Impact", 20),background="blue",anchor="center",width=40).grid(row=0,column=0,columnspan=2)
tk.Label(main_frame,text="").grid(row=1,column=0,columnspan=2)
task = tk.Label(main_frame,text="Pending Task",font=("Impact", 18),anchor="w").grid(row=2,column=0,sticky="w",padx=20)
tk.Label(main_frame,text="").grid(row=3,column=0,columnspan=2)

query = "select * from task where status='pending'"
cur.execute(query)
tasks = cur.fetchall()

rowcount = 4
rowindex = 1

for task in tasks:
    tk.Label(main_frame,text=str(rowindex)+". "+task[1],font=("Times New Roman", 18)).grid(row=rowcount,column=0,sticky="w",padx=20)
    tk.Button(main_frame,text="Done",font=("Times New Roman", 18),width=7,background="blue",command=lambda:remove(task[0])).grid(row=rowcount,column=1,sticky="w",padx=20)
    tk.Label(main_frame,text="").grid(row=rowcount+1,column=0,columnspan=2)
    rowcount+=2
    rowindex+=1

tk.Label(main_frame,text="Add a task",font=("Impact", 18),anchor="w").grid(row=rowcount,column=0,columnspan=2,sticky="w",padx=20)
tk.Label(main_frame,text="").grid(row=rowcount+1,column=0,columnspan=2)
tk.Label(main_frame,text="Enter the task:-",font=("Times New Roman", 18)).grid(row=rowcount+2,column=0,sticky="w",padx=20)
task = tk.Entry(main_frame,width=16,font=("Times New Roman",16)).grid(row=rowcount+2,column=1,sticky="w",padx=20)
tk.Label(main_frame,text="").grid(row=rowcount+3,column=0,columnspan=2)
tk.Button(main_frame,text="Add",font=("Times New Roman", 18),width=5,background="blue",command=lambda:add(task)).grid(row=rowcount+4,column=0,sticky="w",padx=20)
home.mainloop()
    
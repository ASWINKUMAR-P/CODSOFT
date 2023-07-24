import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
import sqlite3
from PIL import Image, ImageTk


def add(new_task):
    query = "insert into task(task,status) values('"+new_task+"','pending')"
    cur.execute(query)
    mydb.commit()
    messagebox.showinfo("Success","Task added successfully")
    createMainFrame(main_frame,cur)

def remove(id):
    query = "update task set status='done' where id='"+str(id)+"'"
    cur.execute(query)
    mydb.commit()
    messagebox.showinfo("Success","Task removed successfully")
    createMainFrame(main_frame,cur)

def createMainFrame(main_frame,cur):

    for widget in main_frame.winfo_children():
        widget.destroy()
        
    tk.Label(main_frame,text="Task Manager",font=("Impact", 25),background="purple",anchor="center",width=30).grid(row=0,column=0,columnspan=2)
    tk.Label(main_frame,text="").grid(row=1,column=0,columnspan=2)
    tk.Label(main_frame,text="Add a task",font=("Times New Roman", 18,"bold")).grid(row=2,column=0,sticky="w",padx=20)
    tk.Label(main_frame,text="").grid(row=3,column=0,columnspan=2)
    tk.Label(main_frame,text="Enter the task:-",font=("Times New Roman", 18)).grid(row=4,column=0,sticky="w",padx=20)
    new_task = tk.Entry(main_frame,width=20,font=("Times New Roman",16))
    new_task.grid(row=4,column=1,sticky="w",padx=20)
    tk.Label(main_frame,text="").grid(row=5,column=0,columnspan=2)
    tk.Button(main_frame,text="Add",font=("Times New Roman", 18),width=5,background="purple",command=lambda:add(new_task.get())).grid(row=6,column=0,sticky="w",padx=20)
    tk.Label(main_frame,text="").grid(row=7,column=0,columnspan=2)
    tk.Label(main_frame,text="Pending Task" ,font=("Times New Roman", 18,"bold"),anchor="w").grid(row=8,column=0,sticky="w",padx=20)
    tk.Label(main_frame,text="").grid(row=9,column=0,columnspan=2)

    query = "select * from task where status='pending'"
    cur.execute(query)
    tasks = cur.fetchall()
    rowcount = 10
    rowindex = 1

    for task in tasks:
        tk.Label(main_frame,text=str(rowindex)+". "+task[1],font=("Times New Roman", 18)).grid(row=rowcount,column=0,sticky="w",padx=20)
        delete_button=tk.Button(main_frame,text="Remove",font=("Times New Roman", 18),command=lambda id=task[0]:remove(id))
        delete_button.grid(row=rowcount,column=1)
        rowcount+=1
        rowindex+=1

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

createMainFrame(main_frame,cur)

home.mainloop()
mydb.close()
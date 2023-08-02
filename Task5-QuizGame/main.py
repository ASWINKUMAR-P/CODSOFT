from questions import questions
from tkinter import *
from tkinter import messagebox
import random

def playagain(window):
    window.destroy()
    home()

def resultpage(window):
    window.destroy()
    window = Tk()
    window.title("Quiz Game") 
    window.resizable(False, False)
    window.geometry("600x500")
    global score
    Label(window, text="").grid(row=0, column=0)
    Label(window, text="Python Quiz Game", font=("Times New Roman", 20,"bold underline"), borderwidth=3, anchor="center",width=35).grid(row=1, column=0)
    Label(window, text="").grid(row=2, column=0)
    Label(window, text="").grid(row=3, column=0)
    Label(window, text="").grid(row=4, column=0)
    Label(window, text="").grid(row=5, column=0)
    Label(window, text="Result:", font=(" Times New Roman", 20, "bold")).grid(row=6, column=0)
    Label(window, text="").grid(row=7, column=0)
    Label(window, text=" Your Score: " + str(score) + "/5", font=("Times New Roman", 15, "bold")).grid(row=8, column=0)
    Label(window, text="").grid(row=9, column=0)
    Button(window, text="Play Again", font=("Times New Roman", 15), command=lambda: playagain(window)).grid(row=10, column=0)



def checkanswer(window, q, answer, Options, button, qnum):
    if answer.get() == "None":
        messagebox.showerror("Error", "Please select an option")
        return
    
    correct_answer = q["answer"]
    selected_answer = answer.get()

    for i in range(4):
        if correct_answer == q["options"][i]:
            correct_option = i+1
            break
    
    for i in range(4):
        if selected_answer == q["options"][i]:
            selected_option = i+1
            break
    
    if correct_option == selected_option:
        Options[correct_option-1].config(text=str(correct_option) + ". " + q["options"][correct_option-1] + " \u2713", fg="green")
        global score
        score += 1
    else:
        Options[correct_option-1].config(text=str(correct_option) + ". " + q["options"][correct_option-1] + " \u2713", fg="green")
        Options[selected_option-1].config(text=str(selected_option) + ". " + q["options"][selected_option-1] + " x", fg="red")
    if qnum < 4:
        button.config(text="Go to next Question", command=lambda: starttest(window, qnum+1))
    else:
        button.config(text="Go to Result Page", command=lambda: resultpage(window))


def starttest(window, qnum):
    try:
        if window.winfo_exists() == True:
            window.destroy()
    except:
        pass
    
    questpage = Tk()
    questpage.title("Quiz Game") 
    questpage.resizable(False, False)
    questpage.geometry("600x500")
    question = questions[qnum]
    
    Label(questpage, text="").grid(row=0, column=0, columnspan=2)
    Label(questpage, text="Python Quiz Game", font=("Times New Roman", 20,"bold underline"), borderwidth=3, anchor="center").grid(row=1, column=0, columnspan=2)
    Label(questpage, text="").grid(row=2, column=0, columnspan=2)
    Label(questpage, text=" ").grid(row=3, column=0, sticky="w")
    Label(questpage, text=question["question"], font=("Times New Roman", 15, "bold"), wraplength=598, justify="left", width=50, anchor="w").grid(row=3, column=1, sticky="w")
    Label(questpage, text="").grid(row=4, column=0, columnspan=2)
    Label(questpage, text=" ").grid(row=5, column=0, sticky="w")
    Label(questpage, text="Options:", font=("Times New Roman", 15, "bold")).grid(row=5, column=1, sticky="w")
    Label(questpage, text="").grid(row=6, column=0, columnspan=2)        
    
    answer = StringVar()
    answer.set("None")
    
    Label(questpage, text=" ").grid(row=7, column=0)
    Label(questpage, text=" ").grid(row=8, column=0)
    Label(questpage, text=" ").grid(row=9, column=0)
    Label(questpage, text=" ").grid(row=10, column=0)
    
    Options = []
    for i in range(4):
        Options.append(Radiobutton(questpage, text=str(i+1) + ". " + question["options"][i], font=("Times New Roman", 15), variable=answer, value=question["options"][i], wraplength=500, justify="left"))
        Options[i].grid(row=7+i, column=1, sticky="w")        
    
    Label(questpage, text=" ").grid(row=11, column=0, columnspan=2)
    button = Button(questpage, text="Submit", font=("Times New Roman", 15), command=lambda: checkanswer(questpage, question, answer, Options, button, qnum))
    button.grid(row=12, column=0, columnspan=2)
    
    questpage.mainloop()


score = 0

def home():

    global questions
    questions = random.sample(questions, 5)
    
    window = Tk()
    window.title("Quiz Game")
    window.resizable(False, False)
    
    Label(window, text="").grid(row=0, column=0)
    Label(window, text="Welcome to the Python Quiz Game!", font=("Times New Roman", 20, "bold underline"), borderwidth=3).grid(row=1, column=0, columnspan=2)
    Label(window, text="").grid(row=2, column=0, columnspan=2)
    Label(window, text=" ").grid(row=3, column=0)
    Label(window, text="Instructions:", font=("Times New Roman", 15, "bold")).grid(row=3, column=1, sticky="w")
    Label(window, text="").grid(row=4, column=0)
    Label(window, text=" ").grid(row=5, column=0)
    Label(window, text="1. There are 5 questions in this quiz.", font=("Times New Roman", 15)).grid(row=5, column=1, sticky="w")
    Label(window, text=" ").grid(row=6, column=0)
    Label(window, text="2. Each question has 4 options.", font=("Times New Roman", 15)).grid(row=6, column=1, sticky="w")
    Label(window, text=" ").grid(row=7, column=0)
    Label(window, text="3. You have to select one option out of the 4 options.", font=("Times New Roman", 15)).grid(row=7, column=1, sticky="w")
    Label(window, text=" ").grid(row=8, column=0)
    Label(window, text="4. You can't change your answer once you click submit button    ", font=("Times New Roman", 15)).grid(row=8, column=1, sticky="w")
    Label(window, text=" ").grid(row=9, column=0)
    Label(window, text="5. Your result will be displayed at the end of the test", font=("Times New Roman", 15)).grid(row=9, column=1, sticky="w")
    Label(window, text="").grid(row=10, column=0, columnspan=2)
    Button(window, text="Start Quiz", font=("Times New Roman", 15, "bold"), anchor="center", bg="blue", fg="white", command=lambda: starttest(window, 0)).grid(row=11, column=0, columnspan=2)
    Label(window, text="").grid(row=12, column=0, columnspan=2)
    
    window.mainloop()

home()

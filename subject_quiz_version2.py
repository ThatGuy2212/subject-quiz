import tkinter as tk
from tkinter import messagebox
import random


    
def math_quiz():
    # Define questions and answers for math quiz
    questions = {
        "Is -5 an integer?": "Yes",
        "The product of two positive numbers is NOT positive.": "No",
        "Two lines with positive slopes can be perpendicular.": "No",
        "What is 1.92÷3": "0.64",
        "What is the value of Pi to four individual decimal places?": "3.1416",
        "What is the name of a triangle that has two sides of the same length?": "Isosceles",
        "What is the net prime number following the number 7? ": "7",
        "What unit is one-hundredth of a meter?": "Centimetre",
        "What maths term means as correct and exact as possible?": "Accurate",
        "What is the last month of the year with 31 days?": "December"
    }

    score = 0
    for q, a in random.sample(list(questions.items()), len(questions)):
        ans = messagebox.askquestion("Question", q)
        if ans == "yes":
            messagebox.showinfo("Result", "Correct!")
            score += 1
        else:
            messagebox.showinfo("Result", "Incorrect!")
    messagebox.showinfo("Final Score", "You scored {} out of {}.".format(score, len(questions)))

def history_quiz():
    # Define questions and answers for history quiz
    questions = {
        "What is considered the largest empire in history?": "The Mongol Empire",
        "Who sent Christopher Columbus to explore the New World?": "King Ferdinand of Spain",
        "Where did Albert Einstein live before moving to the United States?": "Germany",
        "During which war was a Christmas Truce called?": "World War 1",
        "Who was the first person in the world to land on the moon": "Neil Armstrong",
        "How old was Queen Elizabeth II when she was crowned the Queen of England?": "27",
        "Who was the first Emperor of Rome?": "Augustus",
        "Who is the king of the Olympian gods in Greek mythology?": "Zeus",
        "Which ancient figure is often considered the founder of Western philosophy?": "Socrates",
        "How old was King Tutankhamun when he died?": "19"
    }

    for q, a in random.sample(list(questions.items()), len(questions)):
        ans = input(q + " ")
        if ans == a:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

def geography_quiz():
    # Define questions and answers for geography quiz
    questions = {
        "What is the name of the tallest mountain in the world?": "Mount Everest",
        "Which country has the largest population in the world?": "China",
        "What is the capital of Mexico?": "Mexico City",
        "What is the name of the largest country in the world?": "Russia",
        "What country has the most natural lakes?": "Canada",
        "What is the name of the tallest mountain in Canada?": "Mount Logan",
        "What country does the Rhine River run through?": "Germany",
        "What is the name of the driest continent on Earth?": "Antarctica",
        "In which European city was the first organized marathon held?": "Athens",
        "What city is known as the Glass Capital of the World?": "Toledo"
    }

    for q, a in random.sample(list(questions.items()), len(questions)):
        ans = input(q + " ")
        if ans == a:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    



# Create the GUI

def choose_subject():
    def start_quiz():
        choice = subject_var.get()
        if choice == "Math":
            math_quiz()
        elif choice == "History":
            history_quiz()
        elif choice == "Geography":
            geography_quiz()
        else:
            messagebox.showinfo("Invalid Choice", "Please select a subject.")
    
    root = tk.Tk()
    root.title("Quiz")
    
    subject_var = tk.StringVar()
    subject_var.set("")

    subject_label = tk.Label(root, text="Choose a subject:")
    subject_label.pack()

    subjects = ["Math", "Science", "History", "Geography"]
    for subject in subjects:
        rb = tk.Radiobutton(root, text=subject, variable=subject_var, value=subject)
        rb.pack()

    start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
    start_button.pack()

    root.mainloop()

# Call the choose_subject() function to start the quiz
choose_subject()

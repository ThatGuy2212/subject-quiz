import tkinter as tk
from tkinter import messagebox
from random import shuffle
from datetime import date


def math_quiz():
    # Define questions and answers for math quiz
    questions = {

        # REMINDER TO CHANGE QUESTIONS TO MULTIPLE CHOICE
        "Is -5 an integer?": "Yes",
        "The product of two positive numbers is NOT positive.": "No",
        "Two lines with positive slopes can be perpendicular.": "No",
        "What is 1.92÷3": "0.64",
        "What is the value of Pi to four individual decimal places?": "3.1416",
        "What is the name of a triangle that has two sides of the same length?": "Isosceles",
        "What is the net prime number following the number 7? ": "11",
        "What unit is one-hundredth of a meter?": "Centimeter",
        "What maths term means as correct and exact as possible?": "Accurate",
        "What is the last month of the year with 31 days?": "December"
    }

    score = 0
    shuffle(list(questions.items()))

    # Ask each question and check answer
    for question, correct_answer in questions:
        answer = messagebox.askstring(f"{question}")
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!")
            score += 1
        else:
            messagebox.showinfo(f"Incorrect! The correct answer was {correct_answer}, not {answer}!")

    # Show final score
    messagebox.showinfo("Final Score", f"You scored {score} out of {len(questions)}.")


def history_quiz():
    # Define questions and answers for history quiz
    questions = {
        
        # REMINDER TO CHANGE QUESTIONS TO MULTIPLE CHOICE
        "What is considered the largest empire in history?": "The Mongol Empire",
        "Who sent Christopher Columbus to explore the New World?": "King Ferdinand of Spain",
        "Where did Albert Einstein live before moving to the United States?": "Germany",
        "During which war was a Christmas Truce called?": "World War 1",
        "Who was the first person in the world to land on the moon": "Neil Armstrong",
        "How old was Queen Elizabeth II when she was crowned the Queen of England?": "25",
        "Who was the first Emperor of Rome?": "Augustus",
        "Who is the king of the Olympian gods in Greek mythology?": "Zeus",
        "Which ancient figure is often considered the founder of Western philosophy?": "Socrates",
        "How old was King Tutankhamun when he died?": "18"
    }

    score = 0
    shuffle(list(questions.items()))

    # Ask each question and check answer
    for question, correct_answer in questions:
        answer = messagebox.askstring(f"{question}")
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!")
            score += 1
        else:
            messagebox.showinfo(f"Incorrect! The correct answer was {correct_answer}, not {answer}!")

    # Show final score
    messagebox.showinfo("Final Score", f"You scored {score} out of {len(questions)}.")


def science_quiz():
    # Define questions and answers for geography quiz
    questions = {

        # REMINDER TO CHANGE QUESTIONS TO MULTIPLE CHOICE

        "What does DNA stand for?": "Deoxyribonucleic acid",
        "How many bones are in the human body?": "206",
        "At what temperature are Celsius and Fahrenheit equal?": "-40",
        "What is the biggest planet in our solar system?": "Jupiter",
        "What is the only letter not to appear on the periodic table?": "J",
        "What do the letters in the word laser stand for?": "Light Amplification by Stimulated Emission of Radiation",
        "How many bones do sharks have?": "0",
        "What does a Geiger Counter measure?": "Radiation",
        "What metal is the best conductor of electricity?": "Silver",
        "What is sphenopalatine ganglioneuralgia the scientific term for?": "Brain freeze",
        "What is the fastest land animal in the world?": "Cheetah"
    }

    score = 0
    shuffle(list(questions.items()))

    # Ask each question and check answer
    for question, correct_answer in questions:
        answer = messagebox.askstring(f"{question}")
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!")
            score += 1
        else:
            messagebox.showinfo(f"Incorrect! The correct answer was {correct_answer}, not {answer}!")

    # Show final score
    messagebox.showinfo("Final Score", f"You scored {score} out of {len(questions)}.")


def geography_quiz():
    # Define questions and answers for geography quiz, using a dictionary
    QUESTIONS = {
        # REMINDER TO CHANGE QUESTIONS TO MULTIPLE CHOICE
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

    score = 0
    shuffle(list(QUESTIONS.items()))

    # Ask each question and check answer
    for question, correct_answer in QUESTIONS:
        answer = messagebox.askstring(f"{question}")
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!")
            score += 1
        else:
            messagebox.showinfo(f"Incorrect! The correct answer was {correct_answer}, not {answer}!")

    # Show final score
    messagebox.showinfo("Final Score", f"You scored {score} out of {len(QUESTIONS)}.")


def choose_subject():
    # Create the GUI for choosing a subject
    root = tk.Tk()
    root.title("Quiz")

    # Choose subject label
    subject_label = tk.Label(root, text="Choose a subject:")
    subject_label.pack()

    # Radiobuttons for each subject
    subjects = ["Math", "Science", "History", "Geography"]
    subject_var = tk.StringVar()
    for subject in subjects:
        rb = tk.Radiobutton(root, text=subject, variable=subject_var, value=subject)
        rb.pack()

    # Start quiz button
    start_button = tk.Button(root, text="Start Quiz", command=lambda: start_quiz(subject_var.get()))
    start_button.pack()

    root.mainloop()


def start_quiz(subject):
    # Call the appropriate quiz function based on chosen subject
    if subject == "Math":
        math_quiz()
    elif subject == "History":
        history_quiz()
    elif subject == "Science":
        science_quiz()
    elif subject == "Geography":
        geography_quiz()
    else:
        messagebox.showinfo("Invalid entry, please try again.")


# Call the choose_subject() function to start the quiz
choose_subject()

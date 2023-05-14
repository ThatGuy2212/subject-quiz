from tkinter import *

import random

class Quiz:
    """ Authors: Gray, Harper, Garner, Robins; Date: 2 December 2012
    Purpose: This class manages a (text only) multi-choice quiz. It will be extended in future versions with a
    graphical user interface, and access to files of multiple questions and answers. This class is supported by the
    class Question. Instances of Question represent the individual questions (and answers of the quiz). In this
    version of the program there are only two questions. """
    
    
    def math_quiz():
        # Define questions and answers for math quiz
        questions = {
            "What is 2 + 2?": "4",
            "What is 7 x 3?": "21",
            "What is 8 / 2?": "4",
            "What is 1.92÷3": "0.64",
            "What is the value of Pi to four individual decimal places?": "3.1416",
            "What is the name of a triangle that has two sides of the same length?": "Isosceles",
            "What is the net prime number following the number 7? ": "7",
            "What unit is one-hundredth of a meter?": "Centimetre",
            "What maths term means as correct and exact as possible?": "Accurate",
            "What is the last month of the year with 31 days?": "December"
        }

        for q, a in random.sample(list(questions.items()), len(questions)):
            ans = input(q + " ")
            if ans == a:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
    
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
            "What is the capital of Senegal?": "Dakar",
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
    

        
    def take_quiz(self):
        """ This method is the main driver for the quiz. It loops through questions,
            presents each one and its possible answers. It then calls the process_answer method
            passing in a reference to the current question.
            """
        for q in self.questions: # for each question object in the list of questions
            print( q.question ) # print the question
            
            for i in range(len(q.answers)): # print the possible answers
                print("\t" + str(i ) + "\t" + q.answers[i])
                print()
                self.process_answer(q) # get answer from user and give appropriate response
        
    def process_answer(self, q):
        """ This method reads in the user's answer (should be an int in the range 0 to the number
        of possible answers). It gives an appropriate response to the user's answer.
        The while loop continues until the user inputs an int that is in range. Once they do
        their answer is checked against the correct one to see if it matches.
        Remember input comes in as a string and must be converted to int.
        """
        user_answer = -1
        # keeps looping until user's input is an int in range
        while not 0 <= user_answer < len(q.answers):
            a = input("Please type the number of your answer here: ")
        try:
            user_answer = int(a) # if input is not an int we go to the except clause
        
            if not 0 <= user_answer < len(q.answers):
                # input is not in range no further action is taken (the while loop will repeat)
                print("\nThat was out of range\n")
                
            elif user_answer == q.answers.index(q.answer):
                # input is equal to the index of the correct answer (the while loop will end)
                print("\nWell Done!!\n")
            else:
                # input not equal to the index of the correct answer (the while loop will end)
                print("\nIncorrect, the answer is " + q.answer + "\n")
            
        except ValueError:
            # if user's input is not an int this executes (anticipating errors is good design!)
            print("\nThat was not a sensible input. Integers only please.\n")

score = 0


root = Tk()
root.title("Subject Quiz")

button1 = Button



root.mainloop()

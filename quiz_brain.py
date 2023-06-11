class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def more_questions(self):
        # To check if the quiz has more questions

        return self.question_no < len(self.questions)
    
    def next_question(self):
        # Moves onto the next question by incrementing the question number

        self.current_question = self.questions[self.question_no]
        self.question_no += 1

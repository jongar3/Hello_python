class QuizBrain:
    def __init__(self, lista):
        self.question_list = lista
        self.question_number = 0
        self.correct_answer = 0
        self.wrong_answer = 0

    def _check_answer(self, user_input):
        if user_input == self.question_list[self.question_number - 1].answer.title():
            print("You got it right!")
            self.correct_answer += 1
        else:
            print("Wrong Answer.")
            self.wrong_answer += 1
        print(f"The answer was: {self.question_list[self.question_number-1].answer.title()}")
        print(f"Your score is: {self.correct_answer}/{self.question_number}")

    def next_question(self):
        actual_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input=input(f'Question #{self.question_number}: {actual_question.text} type: (True/False): ').title()
        self._check_answer(user_input)

    def still_has_questions(self):
        if len(self.question_list)> self.question_number:
            return True
        else:
            return False
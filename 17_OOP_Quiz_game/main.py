from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
list_question=[]

for dictionary_question in question_data:
    list_question.append(Question(dictionary_question["text"], dictionary_question["answer"]))

quiz= QuizBrain(list_question)
while quiz.still_has_questions():
    quiz.next_question()
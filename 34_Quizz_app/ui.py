THEME_COLOR = "#375362"
from tkinter import *
import pathlib
import html
import time
BASE_PATH = pathlib.Path(__file__).parent
IMAGES_PATH = BASE_PATH / "images"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.after_id = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=320, height=400, bg="white")
        self.question_text = self.canvas.create_text(160, 200, text="Some Question Text", width=300, fill=THEME_COLOR, font=("Arial", 19, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=50)

        true_image = PhotoImage(file=IMAGES_PATH / "true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file=IMAGES_PATH / "false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        """Fetch the next question from the quiz."""
        self.canvas.config(bg="white")
        self.after_id=None
        self.__update_score()
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.quiz.next_question()
            q_text = html.unescape(self.quiz.current_question.text)
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        """Handle the True button press."""
        self.__give_feedback("True")
    def false_pressed(self):
        """Handle the False button press."""
        self.__give_feedback("False")
    def __give_feedback(self, user_answer):
        """Check the user's answer and provide feedback."""
        if self.after_id is None:

            if self.quiz.check_answer(user_answer):
                self.canvas.config(bg="green") 
            else:
                self.canvas.config(bg="red")
            self.after_id= self.window.after(1000, self.get_next_question)
            self.__update_score()

    def __update_score(self):
        self.score_label.config(text= f"Score: {self.quiz.score}")
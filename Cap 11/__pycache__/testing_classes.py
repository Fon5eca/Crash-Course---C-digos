#Clase para administrar una encuesta.

class Survey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(f"The question is: '{self.question}'")

    def store_answer(self, answer_to_add):
        self.responses.append(answer_to_add)

    def show_responses(self):
        print(self.responses)

q1 = Survey("What is your favorite animal?")
class Question:
    def __init__(self, question, difficult, answer):
        self.question = question
        self.difficult = difficult
        self.answer = answer
        self.points = int(difficult) * 10
        self.asked = False
        self.user_amswer = None

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.answer == self.user_amswer

    def build_question(self):
        return f"Вопрос: {self.question}\nСложность {self.difficult}"

    def build_possitive_feedback(self):
        return f"Ответ верный, получено {self.points} баллов"

    def build_negative_feedback(self):
        return f"Ответ неверный, верный ответ {self.answer}"


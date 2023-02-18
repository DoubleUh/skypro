import json
import random
from question import Question

questions = []

with open("question.json", encoding="utf-8") as file:
    questions_data = json.load(file)

for question_data in questions_data:
    question = Question(question_data["q"], question_data["d"], question_data["a"])
    questions.append(question)

random.shuffle(questions)

print("Игра начинается")
print()
for question in questions:
    print(question.build_question())
    user_answer = input()
    question.user_amswer = user_answer
    if question.is_correct():
        print(question.build_possitive_feedback())
    else:
        print(question.build_negative_feedback())
    question.asked = True

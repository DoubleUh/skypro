import json


def load_questions():
    with open("questions.json", encoding="utf-8") as f:
        return json.load(f)


def show_field(questions):
    for category, question_data in questions.items():
        print(category.ljust(17), end="")
        for price, question in question_data.items():
            if not question["asked"]:
                print(price.ljust(7), end="")
            else:
                print("".ljust(7), end="")
        print()



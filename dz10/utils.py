import json

def load_from_file():
    with open("candidates.json", encoding='utf-8') as file:
        data = json.load(file)

    return data

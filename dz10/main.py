from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Я страничка"

@app.route('/profile/')
def page_profile():
    return "Профиль пользователя"

app.run(debug=True)

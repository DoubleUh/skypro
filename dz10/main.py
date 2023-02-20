from flask import Flask
from utils import load_from_file

app = Flask(__name__)

candidates = load_from_file()


@app.route("/")
def page_index():
    result_string = '<pre>'
    for candidate in candidates:
        result_string += f'{candidate["name"]}<br>{candidate["position"]}' \
                         f'<br>{candidate["skills"]}<br><br>'
    result_string += '</pre>'
    return result_string


@app.route('/candidate/<int:id>')
def page_candidate(id):
    result_string = ''
    for candidate in candidates:
        if candidate["id"] == id:
            result_string += f'<img src="{candidate["picture"]}"><br><br>' \
                             f'<pre>{candidate["name"]}<br>{candidate["position"]}<br>' \
                             f'{candidate["skills"]}</pre>'
    return result_string

@app.route('/skill/<skill>')
def page_skill(skill):
    result_string='<pre>'
    for candidate in candidates:
        if skill in candidate["skills"].lower().replace(' ','').split(','):

            result_string += f'{candidate["name"]}<br>{candidate["position"]}<br>' \
                             f'{candidate["skills"]}<br><br>'
    result_string += '</pre>'
    return result_string

app.run(debug=True)

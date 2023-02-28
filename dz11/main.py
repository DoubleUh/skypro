from flask import Flask, render_template
import utils



app = Flask(__name__)

candidates = utils.load_candidates_from_json('candidates.json')

@app.route("/")
def index_page():
    return render_template('index.html', candidates = candidates)

@app.route("/candidate/<int:id>")
def candidate_page(id):
    candidate = utils.get_candidate(id)
    return render_template('candidate.html', candidate = candidate,
                           skills = candidate['skills'].lower().split(', '))

@app.route("/search/<candidate_search>")
def search_candidate(candidate_search):
    candidates = utils.get_candidates_by_name(candidate_search)
    return render_template('search.html', candidates = candidates,
                           len_candidates = len(candidates))
@app.route("/skill/<skill_name>")
def skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates,
                           len_candidates = len(candidates),
                           skill = skill_name)

app.run(debug=True)
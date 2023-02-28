import json

__candidates = []

def load_candidates_from_json(path):
    global __candidates
    with open(path, encoding='utf-8') as file:
        __candidates = json.load(file)
    return __candidates


def get_candidate(candidate_id):
    for candidate in __candidates:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }
    return {'not_found':'Ушел на обед'}

def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __candidates if candidate_name.lower() in candidate['name'].lower()]

def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __candidates:
        skill = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skill:
            candidates.append(candidate)
    return candidates



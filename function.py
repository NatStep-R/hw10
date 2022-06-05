import json


def load_data():
    """получаем данные из файла"""
    with open('candidates.json', 'r', encoding='utf=8') as file:
        data = json.load(file)

    return data


def data_all_candidates():
    """получаем строчку со всеми кондидатами"""
    candidates = load_data()
    candidates_list = []
    result_str = ""
    for candidate in candidates:
        candidates_list.append((candidate["name"],  candidate["position"], candidate["skills"]))
    for i in candidates_list:
        result_str += f'Имя кандидата - {i[0]}\nПозиция кандидата - {i[1]}\nНавыки: {i[2]}\n\n'
    return result_str


def get_candidates_by_skill(needed_skill):
    """получаем кандидатов по нужному скилу сразу в строчку"""
    needed_candidates = []
    result_str = ""
    candidates = load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if needed_skill.lower() in skills:
            needed_candidates.append((candidate["name"],  candidate["position"], candidate["skills"]))
            continue
    for i in needed_candidates:
        result_str += f'Имя кандидата - {i[0]}\nПозиция кандидата - {i[1]}\nНавыки: {i[2]}\n\n'
    return result_str


def get_candidate_by_id(id):
    """получаем кандидата по айди тоже сразу в строчку"""
    candidates = load_data()
    result_str = ""
    for candidate in candidates:
        if candidate["id"] == id:
            result_str += f'<img src=\"{(candidate["picture"])}\">\n'
            result_str += f'''
            Имя кандидата - {candidate["name"]}\n
            Позиция кандидата - {candidate["position"]}\n
            Навыки: {candidate["skills"]}'''

    return result_str

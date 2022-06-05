from flask import Flask
import function

app = Flask(__name__)


@app.route('/')
def page_all_data():
    result_str = function.data_all_candidates()
    return "<pre>" + result_str + "</pre>"


@app.route('/candidates/<int:id>')
def page_candidate_by_id(id):
    result_str = function.get_candidate_by_id(id)
    return "<pre>" + result_str + "</pre>"


@app.route('/skills/<needed_skill>')
def page_candidates_by_skill(needed_skill):
    result_str = function.get_candidates_by_skill(needed_skill.lower())
    return "<pre>" + result_str + "</pre>"


if __name__ == '__main__':
    app.run()
